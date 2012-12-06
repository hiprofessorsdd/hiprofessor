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
		title:"Brian Rules"
	});
	mark.setMap(map);
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
		title:"Brian Rules"
		});
		mark.setMap(map);
	}
	return false;
}
function loadClass(Lat,Lng,build,room,dept,c_no,title,start,end,days,type,crn){
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
		title: dept+' '+c_no,
		info: '<html><body><div id="some_text" style="Float:left; width:auto; height: auto; margin: 5px; padding: 5px; border: 1px solid black; color:#C40000; font-family:verdana; font-size:15p    x; "><b>'+dept+" "+c_no+' - '+title+'</b><p style="font-size:12px">'+build+' '+room+'<br/>'+days+'<br/>'+start+' - '+end+'<br/>'+type+'</p><form name="full" action="info.cgi" target="frm" method="GET"><button name="info" type="submit" value="'+crn+'">View Full Info</button></form><form name="user" action="schedule.cgi" target="frm" method="GET"><button name="add" type="submit" value="'+crn+'">Add to Schedule</button></form><form name="oh" action="officehours.cgi" target="frm" method="GET"><button name="oh" type="submit" value="'+crn+'">Add Office Hours</button></form></div></body></html>'
	});
	mark.setMap(map);
	courseInfoWindow = new google.maps.InfoWindow();
	google.maps.event.addListener(mark, 'click', function() {
	courseInfoWindow.setContent(this.info);
	courseInfoWindow.open(map,this);});
	return false;
}
