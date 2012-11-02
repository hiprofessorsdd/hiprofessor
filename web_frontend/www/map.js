var map;

function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng(42.729267,-73.679489),
		zoom: 17,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"),
		mapOptions);
 }

function dropTag(){
	var Lat = document.forms["LatLngForm"]["Lat"].value;
	var Lng = document.forms["LatLngForm"]["Lng"].value;
	if(isNaN(Lat) || isNaN(Lng)){
		alert("Latitude: [-90, 90], Longitude: [-180,180].");
		return false;
	}
	if(Lat < -90 || Lat > 90 || Lng < -180 || Lng > 180){
		alert("Latitude: [-90, 90], Longitude: [-180,180].");
		return false;
	}
	var point = new google.maps.LatLng(Lat, Lng);
	var mark = new google.maps.Marker({
		position: point,
		animation: google.maps.Animation.DROP,
		title:"Gay"
	});
	mark.setMap(map);
	mark.setMap(map);
	courseInfoWindow = new google.maps.InfoWindow({content: 'You are Gay and you should feel Gay!'});
	google.maps.event.addListener(mark, 'click', function() {courseInfoWindow.open(map,mark);});
	return false;
}

// Generate a random pair of numbers Rand times, and drop the tag
// In range: SW to NE: 42.728865 to 42.731915, -73.683867 to -73.672775
function randTags(){
	var LatDiff = 42.731915 - 42.728865;
	var LngDiff = -73.672775 - -73.683867;
	var Rand = document.forms["RandForm"]["Rand"].value;
	for(var i = 0; i < Rand; i++){
		var RandLat = LatDiff * Math.random() + 42.728865;
		var RandLng = LngDiff * Math.random() + -73.683867;
		var point = new google.maps.LatLng(RandLat, RandLng);
		var mark = new google.maps.Marker({
		position: point,
		animation: google.maps.Animation.DROP,
		title:"Gay"
		});
		mark.setMap(map);
	}
	return false;
}
