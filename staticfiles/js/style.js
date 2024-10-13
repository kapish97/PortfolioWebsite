
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
});