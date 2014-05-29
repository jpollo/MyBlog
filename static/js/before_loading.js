//$('#id_img_title').offset{ left:50% };


$(window).load(function () {
    var url = window.location.href;

    if (endWith(url, "blog") || endWith(url, "blog/")) {

//        alert("in index");
        var newPos = new Object();
        newPos.top = "" + $('.img_title').position().top;
        newPos.left = "-" + $('.img_title').width();
        $('.img_title').offset(newPos);
        $('.img_title').css({visibility: "visible"});
        rotate();

    } else {
//        alert("not in index");

        $('#id_img_title').css({textAlign: "center"});
        $('.img_title').css({visibility: "visible"});
    }

});


$(window).scroll(function(){
  if($(document).scrollTop() > 0)
{
//    if($('#header_nav').data('size') == 'big')
//    {
//        $('#header_nav').data('size','small');
//        $('#header_nav').stop().animate({
//            height:'40px'
//        },600);
//    }
//      alert("top");
      $('.blog_title').css({display: "none"});
      $('.section_header').addClass('fixed');
//      $('.blog_title').animate({display: "none"}, 600);
//      $('.blog_title').animate({height: '100px'}, 600);
//      $('.section_header').css({top:0});
}
else
  {
//    if($('#header_nav').data('size') == 'small')
//      {
//        $('#header_nav').data('size','big');
//        $('#header_nav').stop().animate({
//            height:'100px'
//        },600);
//      }
//      $('.blog_title').stop().animate({display:"true"}, 600);
      $('.section_header').removeClass('fixed');
      $('.blog_title').css({display: "true"});
  }
});


