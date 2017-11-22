var nav_bar = document.querySelector('.nav_bar');

var top_nav = document.querySelector('.top_nav');

var mobile_menu = document.querySelector('.mobile_menu');

var mobile_list =  document.querySelector('.mobile_list');

var body = document.getElementsByTagName('body');

document.addEventListener("DOMContentLoaded", ready);

function ready() {
	var widthScreen = document.documentElement.clientWidth;

	if (widthScreen < 767) {
		console.log(widthScreen);
		colorAndHeight(true);
		mobile_menu.addEventListener('click', mobileNav);
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