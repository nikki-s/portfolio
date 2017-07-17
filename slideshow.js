initSlideShows();

function initSlideShows() {
	var slideshows = document.querySelectorAll('.slideshow');

	for (var i = 0; i < slideshows.length; i++) {
		var slides = slideshows[i].querySelectorAll('.slide');
		for (var j = 1; j < slides.length; j++) {
    		slides[j].style.display = 'none';
		}
		slides[0].style.display = 'block';
	}	
}

function nextSlide(event) {
	jumpToSlide(event, 1);
}

function prevSlide(event) {
	jumpToSlide(event, -1);
}

function jumpToSlide(event, step) {
	var allSlides = event.target.parentNode.querySelectorAll('.slide');

	for (i = 0; i < allSlides.length; i++) {
		if(allSlides[i].style.display == 'block') {
			allSlides[i].style.display = 'none';
			allSlides[ (allSlides.length + i + step) % allSlides.length ].style.display = 'block';
			return;
		}
	}
}
