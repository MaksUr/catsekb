var previewPhoto = document.querySelector('.preview_photo'),
	increasePhoto = document.querySelector('.increase_photo'),
    closeIncreasePhoto = document.querySelector('.close_increase'),
    previousPhotoButton = document.querySelector('.prev_photo'),
    followingPhotoButton = document.querySelector('.next_photo'),
    images = document.querySelectorAll('.item_photo'),
    body = document.getElementsByTagName('body'),
    burger = document.querySelector('.burger'),
    countImage = document.querySelector('.count_image'),
    catInBasket = document.querySelector('.cat_basket'),
    n = 0;


closeIncreasePhoto.addEventListener('click', hidePhoto);

previewPhoto.addEventListener('click', showPhoto);

previousPhotoButton.addEventListener("click", function() {
	images[n].classList.toggle('active');
	
	n--;
	
	if (n < 0) {
		n = images.length - 1;
	}
	images[n].classList.toggle('active');
	countImage.innerText = (n + 1) + ' / ' + images.length; 
});

followingPhotoButton.addEventListener("click", function() {
	images[n].classList.toggle('active');

	n++;

	if (n >= images.length) {
		n = 0;
	}
	images[n].classList.toggle('active');
	countImage.innerText = (n + 1) + ' / ' + images.length;
});

function hidePhoto() {
	increasePhoto.classList.remove('vissible');
	
	topNav.classList.remove('top_nav_increase_photo');
	
	burger.classList.toggle('vis');
	burger.classList.toggle('no-vis');
	
	closeIncreasePhoto.classList.add('no-vis');
	closeIncreasePhoto.classList.remove('vis');
	
	countImage.classList.add('no-vis');
	countImage.classList.remove('vis');
	
	catInBasket.classList.remove('not');
	
	body[0].classList.toggle('overY');
}

function showPhoto() {
	increasePhoto.classList.add('vissible');
	
	topNav.classList.add('top_nav_increase_photo');
	
	burger.classList.toggle('no-vis');
	burger.classList.toggle('vis');
	
	closeIncreasePhoto.classList.remove('no-vis');
	closeIncreasePhoto.classList.add('vis');

	countImage.classList.remove('no-vis');
	countImage.classList.add('vis');
	countImage.innerText = (n + 1) + ' / ' + images.length;

	catInBasket.classList.add('not');

	body[0].classList.toggle('overY');
}
