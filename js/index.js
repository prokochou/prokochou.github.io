$(function(){
	//image source
	var imgArray = new Array();
	
	imgArray[0]="images/about/marathon3.jpg";
	imgArray[1]="images/about/piano.jpg";
	imgArray[2]="images/about/drum.png";
	imgArray[3]="images/about/speech.jpg";

	//timer
	var thisID=0;

	window.setInterval(function(){
		if(thisID==0){
			$('.about-photo').css('width','250px');
			$('.about-photo').attr('src', imgArray[thisID]);
		}else{
			$('.about-photo').css('width','500px');
			$('.about-photo').attr('src', imgArray[thisID]);
		}

		thisID++;
		if(thisID==3) thisID=0;//repeat from start
	},5000);

});

