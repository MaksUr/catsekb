var top_nav = document.querySelector('.top_nav');

var top_logo = document.querySelector('.top_logo');

var top_menu = document.querySelector('.top_menu');

var mobile_menu = document.querySelector('.mobile_menu');

var mobile_list =  document.querySelector('.mobile_list');

document.addEventListener("DOMContentLoaded", ready);

function ready() {
	var widthScreen = document.documentElement.clientWidth;

	if (widthScreen < 767) {
		console.log(widthScreen);
		colorAndHeight(true);
		mobile_menu.addEventListener('click', mobileNav);
	} else {
		window.addEventListener('scroll', go.bind(this, 250));
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
		top_nav.classList.add('top_nav_opened'); 
		top_logo.classList.add('top_logo_opened');
		top_menu.classList.add('top_menu_opened'); 
		
	} else {
		top_nav.classList.remove('top_nav_opened'); 
		top_logo.classList.remove('top_logo_opened');
		top_menu.classList.remove('top_menu_opened'); 	
	} 
}

function mobileNav() {
	mobile_list.classList.toggle('open');
	top_nav.classList.toggle('mobile_nav_opened'); 
}