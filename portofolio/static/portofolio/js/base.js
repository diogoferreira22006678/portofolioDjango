$(document).ready(function(){
  
    // if the user scrolls
    $(window).scroll(function(){
        // get the height of each sections and store it in a variable
        var aboutHeight = $('#about').height();
        var projectsHeight = $('#projects').height();
        // get the difference between all the page and the about section and store it in a variable
        var contactHeight = 2 * projectsHeight;

        // get the scroll position of the window and store it in a variable
        var scrollPos = $(window).scrollTop();

        // if the scroll position is smaller then projects section turn the navbar color to blue 
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
            $('.scroll-up-btn').addClass("blue");
        }else{
            $('.navbar').removeClass("sticky");
            $('.scroll-up-btn').removeClass("blue");
        }

        if(scrollPos > aboutHeight){
            $('.navbar').addClass("blue-bg");
            $('.scroll-up-btn').addClass("blue");
        }else{
            $('.navbar').removeClass("blue-bg");
            $('.scroll-up-btn').removeClass("blue");
        }

        // if the scroll position is bigger then the projects section turn the navbar color to red
        if(scrollPos + 100 > projectsHeight){
            $('.navbar').addClass("red-bg");
            $('.scroll-up-btn').addClass("red");
        }else{
            $('.navbar').removeClass("red-bg");
            $('.scroll-up-btn').removeClass("red");
        }

        // if the scroll position is bigger then contact section turn the navbar color to green
        if(scrollPos > contactHeight){
            $('.navbar').addClass("green-bg");
            $('.scroll-up-btn').addClass("green");
        }else{
            $('.navbar').removeClass("green-bg");
            $('.scroll-up-btn').removeClass("green");
        }

        // show/hide scroll-up button
        if(this.scrollY > 500){
           $('.scroll-up-btn').addClass("show");
        }else{
           $('.scroll-up-btn').removeClass("show");
        }
    });

    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function(){
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });

    // toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

});



$(document ).ready(function() {
    $('.dropdown ul>li').click(function(){
      $('.dropdown ul>li').each(function(){
        $(this).removeClass('drop-selected');
      });
      $(this).toggleClass('drop-selected');
      $('.dropdown>span').text($(this).attr("val"))
    });
});

// Get all the dropdown links
const dropdownLinks = document.querySelectorAll('.menu .dropdown-link');

// get all the li from menu
const menuLinks = document.querySelectorAll('.menu li');

// if li doenst have a ul inside, then if user clicks on it, it will close the menu
menuLinks.forEach(link => {
    if(link.querySelector('ul') == null){
        link.addEventListener('click', () => {
            $('.menu-btn').click();
        });
    }
});

// Attach click event listener to each dropdown link
dropdownLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    // Prevent the default link behavior
    event.preventDefault();

    // Toggle the visibility of the dropdown menu
    const dropdown = link.nextElementSibling;
    dropdown.classList.toggle('active');
  });
});  

const dropdowns = document.getElementsByClassName('dropdown');

if(window.matchMedia("(max-width: 700px)").matches){
  // set the translateX of all dropdowns to 0
  for(let i=0; i<dropdowns.length; i++){
    dropdowns[i].style.transform = "translateX(0)";
  }
}