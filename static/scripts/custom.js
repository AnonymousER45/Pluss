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

	$('.thn-main').click(function(e){
		e.stopPropagation();
		$(this).children('.thn-subnav').toggleClass('active');
	});

	$('body').click(function(e){
		$('this').removeClass('menu-active');
		$('.th-nav').removeClass('active');
		$('.thn-subnav').removeClass('active');
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
	var maxL = 22;
	$('.ap-title').each(function () {
		var text = $(this).text();
		if(text.length > maxL) {
			var begin = text.substr(0, maxL),
			end = text.substr(maxL);
			$(this).html(begin)
			.append($('<span class="readmore"/>').html('...'))
			.append($('<div class="hidden" />').html('end'));
		}
	});

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
		arrows: true,
		infinite: false,
		speed: 300,
		slidesToShow: 5,
		slidesToScroll: 1,
		autoplay: true,
		responsive: [
		{
			breakpoint: 1200,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
			}
		},
		{
			breakpoint: 600,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
			}
		}
		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
		]
	});

	$('.complete-combos').slick({
		dots: false,
		arrows: true,
		infinite: false,
		speed: 300,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		responsive: [
		{
			breakpoint: 1200,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
			}
		},
		{
			breakpoint: 600,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
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
    	$('.complete-combos').slick('setPosition');
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
    	$('.complete-combos').slick("setPosition", 0);
    });


	/* Extra class "tab_last"
	   to add border to right side
	   of last tab */
	   $('ul.tabs li').last().addClass("tab_last");

	});

$(window).resize(function(){
	$("ul.tabs li").click(function() {
		$('.prosliders').slick("setPosition", 0);
		$('.complete-combos').slick("setPosition", 0);
	});
});

$(document).ready(function(){
	$('.product-add-wishtlist').click(function () {
		$(this).toggleClass('wishlisted');
		})
	});
	$('.product-add-wishtlist wishlisted').click(function () {
	});

// $(function(){
// 	$('.lw-list a').click(function(){
// 		$('.lw-list a').removeClass('active');
// 		$(this).addClass('active');
// 	});
// 	$('.signup-btn').click(function(){
// 		$('#lw-login-form').css('left','-200%');
// 		$('#lw-signup-form').css('left','0');
// 	});
// 	$('.login-btn').click(function(){
// 		$('#lw-signup-form').css('left','200%');
// 		$('#lw-login-form').css('left','0');
// 	});
// 	$('.reg-here a').click(function(){
// 		$('.signup-btn').trigger("click");
// 	});
// });



$(document).ready(function(){
	var divHeight = $('.product-details .content').height();
	if(divHeight > 199){
		$('.product-details .content').after('<div class="show-more"><a href="javascript:void(0)">Show more</a></div>');
	}
	$(".show-more a").on("click", function() {
    var $this = $(this);
    var $content = $this.parent().prev("div.content");
    var linkText = $this.text().toUpperCase();

    if(linkText === "SHOW MORE"){
        linkText = "Show less";
        $content.addClass("showContent", 400);
    } else {
        linkText = "Show more";
        $content.removeClass("showContent", 400);
        $content.addClass("hideContent", 400);
    };

    $this.text(linkText);
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

$(document).ready(function(){
	var coll = document.getElementsByClassName("collapsible");
	var i;

	for (i = 0; i < coll.length; i++) {
	  coll[i].addEventListener("click", function() {
	    this.classList.toggle("active");
	    var content = this.nextElementSibling;
	    if (content.style.display === "block") {
	      content.style.display = "none";
	    } else {
	      content.style.display = "block";
	    }
	  });
	}
});

$(document).ready(function(){
	$('#cod').click(function(){
		$('.cod-wrap').slideToggle();
	})

});



$(document).ready(function(){
	$('.digit-group').find('input').each(function() {
		$(this).attr('maxlength', 1);
		$(this).on('keyup', function(e) {
			var parent = $($(this).parent());

			if(e.keyCode === 8 || e.keyCode === 37) {
				var prev = parent.find('input#' + $(this).data('previous'));

				if(prev.length) {
					$(prev).select();
				}
			} else if((e.keyCode >= 48 && e.keyCode <= 57) || (e.keyCode >= 65 && e.keyCode <= 90) || (e.keyCode >= 96 && e.keyCode <= 105) || e.keyCode === 39) {
				var next = parent.find('input#' + $(this).data('next'));

				if(next.length) {
					$(next).select();
				} else {
					if(parent.data('autosubmit')) {
						parent.submit();
					}
				}
			}
		});
	});
});


$(document).ready(function(){
var items = $(".filled-orders .fo-item");
    var numItems = items.length;
    var perPage = 3;

    items.slice(perPage).hide();

    $('#pagination-container').pagination({
        items: numItems,
        itemsOnPage: perPage,
        prevText: "&laquo;",
        nextText: "&raquo;",
        onPageClick: function (pageNumber) {
            var showFrom = perPage * (pageNumber - 1);
            var showTo = showFrom + perPage;
            items.hide().slice(showFrom, showTo).show();
        }
    });
});

// Gift Modal
$('#gift-modal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

// confirm-order-modal
$('#confirm-order-modal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

// confirm-order-modal
$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

// confirm-order-modal
$('#myModal1').on('shown.bs.modal', function () {
  $('#myInput').focus()
})

// checkbox
function toggleCheck(){
	var x = document.getElementById("checkbox").checked;
	if(x == true){
		document.getElementById("checkbox").checked = false;
	}else{
		document.getElementById("checkbox").checked = true;
	}
}

function toggleCheck1(){
	var x = document.getElementById("checkbox1").checked;
	if(x == true){
		document.getElementById("checkbox1").checked = false;
	}else{
		document.getElementById("checkbox1").checked = true;
	}
}
document.querySelectorAll('.product-add-wishtlist').forEach(item => {
	item.addEventListener('click', function(){
		if (window.location.href == window.location.origin+'/' || window.location.href == window.location.origin+'/#')
		{
			product_id = Number(item.parentNode.firstElementChild.href.split('/').slice(-1));
		}
		else{
			product_id = window.location.href.split('/').slice(-1)[0].replace('#','');
		}
		user_id = document.getElementById("user_id").value;

		if (item.className === 'product-add-wishtlist wishlisted'){
			removeFromWishList();
		}
		else{
			addToWishList();
		}
		function addToWishList(){
			$.ajax({
				type: 'POST',
				url: '/django/api/add_to_wishlist/',
				data: {
					"product_id": product_id,
					  "id": user_id, 
				},
				success: function(data){
				  alert("Item added to wishlist");
				}
			});
		}
		function removeFromWishList(){
			$.ajax({
				type: 'POST',
				url: '/django/api/remove_from_wishlist/',
				data: {
					"product_id": product_id,
					"id": user_id, 
				},
				success: function(data){
				  alert("Item Removed to wishlist");
				}
			});
		}
		
	})
  })
