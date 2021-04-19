// JavaScript Document
$(document).ready(function(){
	$(".content-wrap").css("padding-top", $(".top-head").height());
	$(".th-nav").css("top", $(".top-head").height());
	
	$('.th-menu').click(function(e){
		e.stopPropagation();
		$(this).toggleClass('active');
		$('.th-nav').toggleClass('active');
		$('body').toggleClass('menu-active');
	});
	
	$('.thn-main').click(function(){
		$(this).children('.thn-subnav').toggleClass('active');
	});
	
	$('body').click(function(){
		$('this').removeClass('menu-active');
		$('.th-nav').removeClass('active');		
	});
});


$(window).resize(function(){
	$(".content-wrap").css("padding-top", $(".top-head").height());
	$(".th-nav").css("top", $(".top-head").height());
});

$(function(){
	var nav = $('.top-head').length;
	if(nav <= 0){
		//do nothing
	} else {
		var offset = $('.top-head').offset().top;	
		
		var sticky = function(){
			var sticky = $(window).scrollTop(); 
			if (sticky > offset) {
				$('.top-head').addClass('sticky');
			}
			else {
				$('.top-head').addClass('sticky');
			}
		}
		
		sticky();
		$(window).scroll(function(){
			sticky();	
		});
	}
});



$(document).ready(function(){
	var maxL = 50;
	$('.ap-title').each(function () {
		var text = $(this).text();
		if(text.length > maxL) {
			var begin = text.substr(0, maxL),
			end = text.substr(maxL);
			$(this).html(begin)
			.append($('<span class="readmore"/>').html('more...'))
			.append($('<div class="hidden" />').html('end'));
		}
	});
	// $(document).on('click', '.readmore', function (e) {
	// 			// $(this).next('.readmore').fadeOut("400");
	// 			e.stopPropagation();
	// 			$(this).next('.hidden').slideToggle(400);
	// 		})        
});



$(document).ready(function(){ 
	var minVal = 1, maxVal = 20; // Set Max and Min values
// Increase product quantity on cart page
$(".increaseQty").on('click', function(){
	var $parentElm = $(this).parents(".qtySelector");
	$(this).addClass("clicked");
	setTimeout(function(){
		$(".clicked").removeClass("clicked");
	},100);
	var value = $parentElm.find(".qtyValue").val();
	if (value < maxVal) {
		value++;
	}
	$parentElm.find(".qtyValue").val(value);
});
// Decrease product quantity on cart page
$(".decreaseQty").on('click', function(){
	var $parentElm = $(this).parents(".qtySelector");
	$(this).addClass("clicked");
	setTimeout(function(){
		$(".clicked").removeClass("clicked");
	},100);
	var value = $parentElm.find(".qtyValue").val();
	if (value > 1) {
		value--;
	}
	$parentElm.find(".qtyValue").val(value);
});
});



$(document).ready(function(){
	$('.slider-for').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: false,
		fade: true,
		asNavFor: '.slider-nav'
	});
	$('.slider-nav').slick({
		slidesToShow: 4,
		slidesToScroll: 1,
		asNavFor: '.slider-for',
		dots: false,
		arrows: false,
		focusOnSelect: true
	});
});

$(document).ready(function(){
	$('.homeslider').slick({
		dots: true,
		arrows: false,
		infinite: true,
		speed: 300,
		slidesToShow: 1,
		adaptiveHeight: true,
		autoplay: true,
	});
	
	$('.prosliders').slick({
		dots: false,
		arrows: false,
		infinite: false,
		speed: 300,
		slidesToShow: 5,
		slidesToScroll: 1,
		responsive: [
		{
			breakpoint: 1200,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				dots: true,
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
				dots: true,
			}
		},
		{
			breakpoint: 640,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
				dots: true,
			}
		}
		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
		]
	});
	
	 // tabbed content
    // http://www.entheosweb.com/tutorials/css/tabs.asp
    $(".tab_content").hide();
    $(".tab_content:first").show();

    /* if in tab mode */
    $("ul.tabs li").click(function() {

    	$(".tab_content").hide();
    	var activeTab = $(this).attr("rel"); 
    	$("#"+activeTab).fadeIn();		

    	$("ul.tabs li").removeClass("active");
    	$(this).addClass("active");

    	$(".tab_drawer_heading").removeClass("d_active");
    	$(".tab_drawer_heading[rel^='"+activeTab+"']").addClass("d_active");
    	$('.prosliders').slick('setPosition');
    });
    /* if in drawer mode */
    $(".tab_drawer_heading").click(function() {

    	$(".tab_content").hide();
    	var d_activeTab = $(this).attr("rel"); 
    	$("#"+d_activeTab).fadeIn();

    	$(".tab_drawer_heading").removeClass("d_active");
    	$(this).addClass("d_active");

    	$("ul.tabs li").removeClass("active");
    	$("ul.tabs li[rel^='"+d_activeTab+"']").addClass("active");
    	$('.prosliders').slick("setPosition", 0);
    });


	/* Extra class "tab_last" 
	   to add border to right side
	   of last tab */
	   $('ul.tabs li').last().addClass("tab_last");

	});

$(window).resize(function(){
	$("ul.tabs li").click(function() {
		$('.prosliders').slick("setPosition", 0);
	});
});

$(function(){
	$('.lw-list a').click(function(){
		$('.lw-list a').removeClass('active');
		$(this).addClass('active');
	});
	$('.signup-btn').click(function(){
		$('#lw-login-form').css('left','-200%');
		$('#lw-signup-form').css('left','0');
	});
	$('.login-btn').click(function(){
		$('#lw-signup-form').css('left','200%');
		$('#lw-login-form').css('left','0');
	});	
	
});

$(function(){
	var scrollPos = 0;
	// Only one of these modals should show at a time.
	$('#myModal2').on('show.bs.modal', function (e) {
	  $('#myModal').modal('hide');
	  $('body').css({
	    overflow: 'hidden',
	    position: 'fixed',
	    top : -scrollPos
	  });
	}).on('hide.bs.modal', function (e) {
	  $('#myModal').modal('show').on('hidden.bs.modal', function (e) {
	    $('body').css({
	      overflow: '',
	      position: '',
	      top: ''
	    }).scrollTop(scrollPos);
		});
	});

	jQuery(document).on('click','[data-toggle*=modal]',function(){
	  jQuery('[role*=dialog]').each(function(){
	    switch(jQuery(this).css('display')){
	      case('block'):{jQuery('#'+jQuery(this).attr('id')).modal('hide'); break;}
	    }
	  });
	});
});


$(document).ready(function(){ 
	$(window).scroll(function(){ 
		if ($(this).scrollTop() > 100) { 
			$('#scroll').fadeIn(); 
		} else { 
			$('#scroll').fadeOut(); 
		} 
	}); 
	$('#scroll').click(function(){ 
		$("html, body").animate({ scrollTop: 0 }, 600); 
		return false; 
	}); 

	$(".toggle-password").each(function(){
		$(this).click(function() {
		  $(this).toggleClass("fa-eye-slash fa-eye");
		  var input = $($(this).attr("toggle"));
		  if (input.attr("type") == "password") {
		    input.attr("type", "text");
		  } else {
		    input.attr("type", "password");
		  }
		});
	});
});

