var nav_bar = document.querySelector('.nav_bar');
var top_nav = document.querySelector('.top_nav');
var burger = document.querySelector('.burger');
var mobile_list =  document.querySelector('.mobile_list');
var body = document.getElementsByTagName('body');
var cat_find_block = document.querySelectorAll('.cat_find_block');
var open_next_menu = document.querySelectorAll('.open_next_menu');
var widthScreen = document.documentElement.clientWidth;

document.addEventListener("DOMContentLoaded", ready);

const canHover = !(matchMedia('(hover: none)').matches);

function ready() {
	if(canHover) {
  		document.body.classList.add('can-hover');
	}

	if(body[0].classList.contains('can-hover') == false) {
		for (i = 0; i <= open_next_menu.length - 1; i++) {
			open_next_menu[i].addEventListener('click', view_menu_opening.bind(this, i));
		}

		for (i = 0; i <= cat_find_block.length - 1; i++) {
			cat_find_block[i].addEventListener('click', view_name.bind(this, i));
		}
	} 
	
	if (widthScreen < 751) {
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

function view_menu_opening(i) {
	open_next_menu[i].nextElementSibling.classList.toggle('menu_opening_view')
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


var formShel = document.documentElement.querySelectorAll('.shelter_distance');
var formLoc = document.documentElement.querySelectorAll('.location_status');

for (i = 0; i <= formLoc.length - 1; i++) {
			formLoc[i].addEventListener('click', elemBlock.bind(this, i));
		}


function elemBlock(i) {
	if (formLoc[1].checked == false) {
	for(i = 0; i <= formShel.length - 1; i++) {
		formShel[i].disabled = 'disable';
	} 
	} else {
		for(i = 0; i <= formShel.length - 1; i++) {
			formShel[i].disabled = '';
		}
	}
}

