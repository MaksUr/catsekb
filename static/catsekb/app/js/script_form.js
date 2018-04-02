document.addEventListener("DOMContentLoaded", disabledShelterDistance);

var formShelter = document.documentElement.querySelectorAll('.shelter_distance'),
    formLocation = document.documentElement.querySelectorAll('.location_status');

for (i = 0; i <= formLocation.length - 1; i++) {
	formLocation[i].addEventListener('click', disabledShelterDistance.bind(this, i));
}

function disabledShelterDistance(i) {
	if (formLocation[2].checked == true || formLocation[0].checked == true) {
		for(i = 0; i <= formShelter.length - 1; i++) {
			formShelter[i].disabled = '';
		} 
	} else {
		for(i = 0; i <= formShelter.length - 1; i++) {
			formShelter[i].disabled = 'disable';
		} 
	}
}