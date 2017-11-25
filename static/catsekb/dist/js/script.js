var nav_bar = document.querySelector('.nav_bar');

var top_nav = document.querySelector('.top_nav');

var burger = document.querySelector('.burger');

var mobile_list =  document.querySelector('.mobile_list');

var body = document.getElementsByTagName('body');

const canHover = !(matchMedia('(hover: none)').matches);

if(canHover) {
  	document.body.classList.add('can-hover');
}

if(body[0].classList.contains('can-hover') == false) {
	var cat_find_block = document.querySelectorAll('.cat_find_block');

	for (i = 0; i <= cat_find_block.length - 1; i++) {
		cat_find_block[i].addEventListener('click', view_name.bind(this, i));
	}
}
document.addEventListener("DOMContentLoaded", ready);

function ready() {
	var widthScreen = document.documentElement.clientWidth;

	if (widthScreen < 766) {
		console.log(widthScreen);
		colorAndHeight(true);
		burger.addEventListener('click', mobileNav);

	} else {
		window.addEventListener('scroll', go.bind(this, 325));
	}
}

function go(val) {		
		var scrolled =  window.pageYOffset || document.documentElement.scrollTop;
		
		if (scrolled >= val) {
			colorAndHeight(true);
		}
		else {
			colorAndHeight(false);
		}		
	}

function colorAndHeight(bool) {
	if (bool) {
		nav_bar.classList.add('nav_bar_opened'); 
		top_nav.classList.add('top_nav_opened'); 
		
	} else {
		nav_bar.classList.remove('nav_bar_opened'); 
		top_nav.classList.remove('top_nav_opened'); 	
	} 
}

function mobileNav() {
	mobile_list.classList.toggle('open'); 
	body[0].classList.toggle('overY');
}


function view_name(i) {
	cat_find_block[i].classList.toggle('cat_find_view');
}


(function() {
 
  "use strict";
 
  var toggles = document.querySelectorAll(".burger");
 
  for (var i = toggles.length - 1; i >= 0; i--) {
    var toggle = toggles[i];
    toggleHandler(toggle);
  };
 
  function toggleHandler(toggle) {
    toggle.addEventListener( "click", function(e) {
      e.preventDefault();
      (this.classList.contains("is-active") === true) ? this.classList.remove("is-active") : this.classList.add("is-active");
    });
  }
 
})();