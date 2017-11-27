var preview_photo = document.querySelector('.preview_photo');

var increase_photo = document.querySelector('.increase_photo');

var close_increase_photo = document.querySelector('.close_increase');

var btn_prev = document.querySelector('.prev_photo');

var btn_next = document.querySelector('.next_photo');

var images = document.querySelectorAll('.item_photo');

var body = document.getElementsByTagName('body');

var mobile_list =  document.querySelector('.mobile_list');

var burger = document.querySelector('.burger');

var n = 0;

close_increase_photo.addEventListener('click', exit);

preview_photo.addEventListener('click', increase);

btn_prev.onclick = function() {
	images[n].classList.toggle('active');

	n--;
	
	if (n < 0) {
		n = images.length - 1;
	}

	images[n].classList.toggle('active');
	}

btn_next.onclick = function() {
	images[n].classList.toggle('active');

	n++;

	if (n >= images.length) {
		n = 0;
	}
	images[n].classList.toggle('active');
}

function exit() {
	increase_photo.classList.remove('vissible');
	top_nav.classList.remove('top_nav_increase_photo');
	burger.classList.add('vis');
	burger.classList.remove('no-vis');
	close_increase_photo.classList.add('no-vis');
	close_increase_photo.classList.remove('vis');
	body[0].classList.remove('overY');
}

function increase() {
	increase_photo.classList.add('vissible');
	top_nav.classList.add('top_nav_increase_photo');
	burger.classList.add('no-vis');
	burger.classList.remove('vis');
	close_increase_photo.classList.remove('no-vis');
	close_increase_photo.classList.add('vis');
	body[0].classList.add('overY');

}

