document.addEventListener("DOMContentLoaded", shelDisDisable);

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