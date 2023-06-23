let searchForm=document.querySelector('.search-form');
document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    loginBox.classList.remove('active');
}

let loginBox=document.querySelector('.login-box');
document.querySelector('#login-btn').onclick = () => {
    loginBox.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

let navbar=document.querySelector('.navbar');
document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    loginBox.classList.remove('active');
    searchForm.classList.remove('active');
}

window.onscroll = () => {
    navbar.classList.remove('active');
    loginBox.classList.remove('active');
    searchForm.classList.remove('active');
}
let chage_pass=document.querySelector('#change-pass');
document.querySelector('#edit-pass').onclick = () => {
    chage_pass.classList.toggle('active');
    edit_profile.classList.remove('active');
}
let edit_profile=document.querySelector('#edit-profile');
document.querySelector('#edit').onclick = () => {
    edit_profile.classList.toggle('active');
    chage_pass.classList.remove('active');
}
let closeX=document.getElementById('close');
closeX.addEventListener('click',function(){
    edit_profile.classList.remove('active');
    
})
