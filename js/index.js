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
		//get screen width
		var width = $(window).width(); 

		if(thisID==0){
			$('.about-photo').css('width','250px');
			$('.about-photo').attr('src', imgArray[thisID]);
		}else{
			console.log(width);
			if (width>375){
				$('.about-photo').css('width','500px');
			}else{
				$('.about-photo').css('width','300px');
			}
			console.log(thisID)
			$('.about-photo').attr('src', imgArray[thisID]);
		}

		thisID++;
		if(thisID==3) thisID=0;//repeat from start
	},5000);

});

