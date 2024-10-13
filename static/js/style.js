
//window scroll
$(window).on("scroll",function(){

    var scrollTop = $(window).scrollTop();
    if(scrollTop>=100){
        $('body').addClass('fixed-header');
    }
    else{
        $('body').removeClass('fixed-header')
    }
});
  
//Document ready

$(document).ready(function(){
    //type animation
     new Typed('#type-it', {
        strings: ['Pythonista', 'Analyst','Learner'],
        typeSpeed: 100,
        loop: true
      });

    //owl carousel
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        autoplay:true,
        autoplayTimeout: 2000,
        responsive:{
            0:{
                items:1
            },
            900:{
                items:2
            }
        }
    })
});