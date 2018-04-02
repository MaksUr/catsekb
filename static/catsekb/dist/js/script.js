"use strict";

var topNav = document.querySelector('.top_nav'), 
 	burger = document.querySelector('.burger'), 
 	mobileList =  document.querySelector('.mobile_list'), 
 	body = document.getElementsByTagName('body'), 
 	catFindBlock = document.querySelectorAll('.cat_find_block'), 
	openNextMenu = document.querySelectorAll('.open_next_menu');
	  
document.addEventListener("DOMContentLoaded", documentReady);

function documentReady() {
	toggleHandler(burger);
	hoverSupport();
	mobileOrDesktopMenu();
}

function hoverSupport() {
	if( !( matchMedia( '(hover: none)' ).matches ) ) {
  		document.body.classList.add('can-hover');
	}

	if(body[0].classList.contains('can-hover') === false) {
		for (var i = 0; i <= openNextMenu.length - 1; i++) {
			openNextMenu[i].addEventListener('click', showMenu.bind(this, i));
		}

		for (i = 0; i <= catFindBlock.length - 1; i++) {
			catFindBlock[i].addEventListener('click', showNameCat.bind(this, i));
		}
	} 
}

function mobileOrDesktopMenu() {
	var widthScreen = document.documentElement.clientWidth;

	if (widthScreen < 751) {
		burger.addEventListener('click', openedMobileMenu);
	} else {
		window.addEventListener('scroll', openedTopMenu.bind(this, 325));
	}
}

function openedTopMenu(scrollValue) {		
	var scrolled =  window.pageYOffset || document.documentElement.scrollTop;
	
	if (scrolled >= scrollValue) {
		topNav.classList.add('top_nav_opened'); 
	} else {
		topNav.classList.remove('top_nav_opened'); 
	}		
}

function openedMobileMenu() {
	mobileList.classList.toggle('open'); 
	body[0].classList.toggle('overY');
}

function showNameCat(numberCat) {
	catFindBlock[numberCat].classList.toggle('cat_find_view');
}

function showMenu(i) {
	openNextMenu[i].nextElementSibling.classList.toggle('menu_opening_view');
}

function toggleHandler(toggle) {
	toggle.addEventListener("click", function(event) {
		event.preventDefault();
		(this.classList.contains("is-active") === true) ? this.classList.remove("is-active") : this.classList.add("is-active");
	});
}
 

