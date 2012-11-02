#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import psycopg2;
import hpdb;
 
print "Content-type: text/html"
print

print """

<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100%}
      body { height: 100%; margin: 0; padding: 0 }
      #map_canvas { height: 100%}
	  #some_text {height: 100%}
    </style>
    <script type="text/javascript"
            src="http://maps.googleapis.com/maps/api/js?key=AIzaSyAqZL5nSjN364_-Jl2sKtnU4C7BUnL45iU&sensor=false">
	</script>
    <script type = "text/javascript"
	        src = "/map.js"> 
	</script>
  </head>
  <body onload="initialize()">
    <div id="map_canvas" style="Float:right; width:75%; height:100%"></div>
	<div id="search" style="Float:left; width: 180px; height: 80px; margin: 5px; padding: 5px; border: 1px solid black;"><b>HiProfessor</b><br>
	RPI, SW to NE: 42.728865 to 42.731915, -73.683867 to -73.672775<br><br>
	<form name = "LatLngForm" action="map.cgi" onsubmit ="return dropTag();">
	<input type = "text" name = "Lat" autofocus placeholder="Latitude">
	<input type = "text" name = "Lng" placeholder = "Longitude">
	<input type = "submit" value= "Drop the Tag">
	</form>
	
	<br>
	<form name = "RandForm" action = "map.cgi" onsubmit ="return randTags();">
	<input type = "text" name = "Rand" autofocus placeholder="# of Random Tags">
	<input type = "submit" value = "Rand That Shit Up!">
	</form>"""
form = cgi.FieldStorage()
message = form.getvalue("dropdown", "(no message)")
print """
<form action="pagejs.cgi" onsubmit="return searchResults();">
<select name="dropdown">"""

depts = hpdb.get_departments()
for d in depts:
	print '<option value="'+d+'">'+d+'</option>'

print """</select>
<input type="submit" value="Search"/>
</form>	
"""
print message	

print """
	</div>
  </body>
</html>

"""
