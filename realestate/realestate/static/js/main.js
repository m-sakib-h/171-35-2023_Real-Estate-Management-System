const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Message FadeOut
setTimeout(function (){
    $('#message').fadeOut('slow');
},3000)      //After 3000 msec or 3 sec it will be fade out