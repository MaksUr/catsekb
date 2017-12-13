var top_nav = document.querySelector('.top_nav'), 
 	burger = document.querySelector('.burger'), 
 	mobile_list =  document.querySelector('.mobile_list'), 
 	body = document.getElementsByTagName('body'), 
 	cat_find_block = document.querySelectorAll('.cat_find_block'), 
 	open_next_menu = document.querySelectorAll('.open_next_menu'), 
 	widthScreen = document.documentElement.clientWidth;

document.addEventListener("DOMContentLoaded", ready);
document.addEventListener("DOMContentLoaded", shelDisDisable);
var canHover = !(matchMedia('(hover: none)').matches);

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
		burger.addEventListener('click', mobileNav);

	} else {
		window.addEventListener('scroll', go.bind(this, 325));
	}
	
}

function go(val) {		
		var scrolled =  window.pageYOffset || document.documentElement.scrollTop;
		
		if (scrolled >= val) {
			top_nav.classList.add('top_nav_opened'); 
		}
		else {
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
	open_next_menu[i].nextElementSibling.classList.toggle('menu_opening_view');
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



var formShel = document.documentElement.querySelectorAll('.shelter_distance'),
    formLoc = document.documentElement.querySelectorAll('.location_status');

for (i = 0; i <= formLoc.length - 1; i++) {
	formLoc[i].addEventListener('click', shelDisDisable.bind(this, i));
}

function shelDisDisable(i) {
	if (formLoc[2].checked == true || formLoc[0].checked == true) {
		for(i = 0; i <= formShel.length - 1; i++) {
			formShel[i].disabled = '';
		} 
	} else {
		for(i = 0; i <= formShel.length - 1; i++) {
			formShel[i].disabled = 'disable';
		} 
	}
}

var artVisBut = document.documentElement.querySelectorAll('.art_vis'),
    art =  document.documentElement.querySelectorAll('.art');

for (i = 0; i <= artVisBut.length - 1; i++) {
    artVisBut[i].addEventListener('click', openArt.bind(this, i));
}

function openArt(i) {
    art[i].classList.toggle('open_art');
}