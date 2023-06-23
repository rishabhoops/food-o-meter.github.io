from django.shortcuts import render,get_object_or_404, reverse,redirect
from foodOmeterApp.models import contact,Profile,Menu,Cart,CartItems,Order
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from .helper import send_forget_password_mail
import uuid
from instamojo_wrapper import Instamojo
from django.conf import settings

api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')

def index(request):
    menu=Menu.objects.all().order_by('id')
    if "product" in request.POST:
        if request.user.is_authenticated:
            p=int(request.POST['product'])
            product=Menu.objects.get(id=p)
            user=get_object_or_404(Profile, user = request.user)
            cart,created=Cart.objects.get_or_create(user=user,is_paid=False)
            cart_item,item_created=CartItems.objects.get_or_create(user=user,cart=cart,product=product,price=product.item_price)
            if not item_created:
                cart_item.qauntity+=1
            else:
                cart_item.qauntity=1
            cart_item.t_price=int(cart_item.qauntity)*int(product.item_price)
            cart_item.save()
            return render(request, 'index.html',{'menu':menu})
        else:
            return render(request,'login.html') 
    return render(request, 'index.html',{'menu':menu})

def aboutusPage(request):
    return render(request,'aboutus.html')

def contactusPage(request):
    context={}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mob_no=request.POST['mob_no']
        message=request.POST['message']
        cn=contact(name=name,email=email,mob_no=mob_no,message=message)
        cn.save()
        context['message']=f"Dear {name}, Thank You! For Time, We will connect you Soon"
    return render(request,'contact.html',context)

def servicePage(request):
    return render(request,'services.html')

def menuPage(request):
    menu=Menu.objects.all().order_by('id')
    if "product" in request.POST:
        if request.user.is_authenticated:
            p=int(request.POST['product'])
            product=Menu.objects.get(id=p)
            user=get_object_or_404(Profile, user = request.user)
            cart,created=Cart.objects.get_or_create(user=user,is_paid=False)
            cart_item,item_created=CartItems.objects.get_or_create(user=user,cart=cart,product=product,price=product.item_price)
            if not item_created:
                cart_item.qauntity+=1
            else:
                cart_item.qauntity=1
            cart_item.t_price=int(cart_item.qauntity)*int(product.item_price)
            cart_item.save()
            return render(request, 'menu.html',{'menu':menu})
        else:
            return render(request,'login.html')
    return render(request,'menu.html',{'menu':menu})

def loginPage(request):
    context={}
    if request.method =="POST":
        username=request.POST['email']
        password=request.POST['pass']
        
        check_user=authenticate(username=username,password=password)
        if check_user:
            login(request,check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin/')
            context.update({'message':"Login Successful"})
            return HttpResponseRedirect('/dashboard')
        else:
            context.update({'message':"Invalid Credentials"})
    return render(request,'login.html',context)

def register(request):
    context={}
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['mob_no']
        password=request.POST['pass']
        try:
            usr=User.objects.create_user(email,email,password)
            usr.first_name=name
            usr.save()
            profile=Profile(user=usr,contact=contact)
            profile.save()
            context['status']=f"User {name} Register Successfully!"
        except:
            context['error']=f"User Or email Already Exist!"
    return render(request,'register.html',context)

def check_user_exist(request):
    email=request.GET.get('usern')
    check=User.objects.filter(username=email)
    if len(check)==0:
        return JsonResponse({'status':0,'messsage':'Not Exist'})
    else:
        return JsonResponse({'status':1,'messsage':'Exist'})
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def Dashboard(request):
    login_user = get_object_or_404(User, id = request.user.id)
    context={}
    profile=Profile.objects.get(user__id=request.user.id)
    context['profile'] = profile
    order= Order.objects.filter(customer=profile,status=True)
    context['order']=order
    
    if "update_profile" in request.POST:
        name = request.POST.get('name')
        contact = request.POST.get('contact_number')
        add = request.POST.get('address')
       

        profile.user.first_name = name 
        profile.user.save()
        profile.contact_number = contact 
        profile.address = add 

        if "profile_pic" in request.FILES:
            pic = request.FILES['profile_pic']
            profile.profile_pic = pic
        profile.save()
        context['status'] = 'Profile updated successfully!'
        
    if "change_pass" in request.POST:
        c_password = request.POST.get('current_password')
        n_password = request.POST.get('new_password')
        print(c_password,n_password)
        check = login_user.check_password(c_password)
        if check==True:
            login_user.set_password(n_password)
            login_user.save()
            login(request, login_user)
            context['status'] = 'Password Updated Successfully!' 
        else:
            context['status'] = 'Current Password Incorrect!'
            
        
    return render(request,'dashboard.html',context)
    
def forget_password(request):
    context={}
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            if not User.objects.filter(username=email).first():
                context['message']='Email Does Not Exist'
                return render(request,'forget_password.html',context)
            
            user_obj=User.objects.get(username=email)
            token= str(uuid.uuid4())
            profile_obj=Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token=token
            profile_obj.save()
            send_forget_password_mail(user_obj,token)
            context['message']='Email Sent'
            return render(request,'forget_password.html',context)
                
    except Exception as e:
        print(e)
        
    return render(request,'forget_password.html')

def change_password(request,token):
    context={}
    try:
        profile_obj=Profile.objects.get(forget_password_token=token)
        print(profile_obj)
        if request.method == 'POST':
            new_password = request.POST.get('n_pass')
            confirm_password=request.POST.get('c_pass')
            user_id=request.POST.get('user_id')
            
            if user_id is None:
                context['message']='User Id Not Found'
                return render(request,f'/change_password/{token}/',context)
            
            if new_password != confirm_password:
                context={'user_id':profile_obj.id}
                context['password']='Password Does not Match'
                return render(request,f'/change_password/{token}/',context)
            
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return render(request,'login.html')
        
        context={'user_id':profile_obj.id}
        
        
    except Exception as e:
        print(e)
    return render(request,'change_password.html',context)



def cart(request):
    try:
        context={}
        total=0
        user=get_object_or_404(Profile, user = request.user)
        cart=CartItems.objects.filter(user=user)
        context['cart']=cart
        for i in cart:
            total+=int(i.t_price)
        context['total']=total
    except Exception as e:
        pass
    return render(request,'cart.html',context)

def checkout(request):
    try:
        context={}
        total=0
        user=get_object_or_404(Profile, user = request.user)
        cart=CartItems.objects.filter(user=user)
        context['cart']=cart
        product = []
        for i in cart:
            product.append(i.product.item_name)
            total+=int(i.t_price)
        context['total']=total
        order_obj,_=Order.objects.get_or_create( 
            item=product,                                   
            customer=get_object_or_404(Profile, user = request.user),
            status=False,
        )
        response=api.payment_request_create(
            amount = total,
            purpose= 'Order Process',
            buyer_name= user,
            email=request.user.email,
            redirect_url='http://127.0.0.1:8000/order-sucess/'
        )
        order_obj.payer_id=response['payment_request']['id']
        order_obj.instamojo_response=response
        order_obj.save()
        context['payment_url']= response['payment_request']['longurl']
    except Exception as e:
        print(e)
        pass
    return render(request,'checkout.html',context)


def order_sucess(request):
    payment_request_id=request.GET.get('payment_request_id')
    payment_status=request.GET.get('payment_status')
    payment_id=request.GET.get('payment_id')
    if payment_status == "Failed":
        return render(request,'payment_failed.html')
    order_obj=Order.objects.get(payer_id=payment_request_id)
    inv = f'INV0000-{payment_id}'
    order_obj.status=True
    order_obj.invoice_id=inv
    order_obj.save()
    user=get_object_or_404(Profile, user = request.user)
    cart=CartItems.objects.filter(user=user)
    cart.delete()
    return render(request,'payment_sucess.html')
    