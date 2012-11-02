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
	        src = "map.js"> 
	</script>
  </head>
  <body onload="initialize()">
    <div id="map_canvas" style="Float:right; width:75%; height:100%"></div>
	<div id="some_text" style="Float:left; width: 180px; height: 80px; margin: 5px; padding: 5px; border: 1px solid black;"><b>HiProfessor</b><br>
	RPI, SW to NE: 42.728865 to 42.731915, -73.683867 to -73.672775<br><br>
	<form name = "LatLngForm" action="maps.html" onsubmit ="return dropTag();">
	<input type = "text" name = "Lat" autofocus placeholder="Latitude">
	<input type = "text" name = "Lng" placeholder = "Longitude">
	<input type = "submit" value= "Drop the Tag">
	</form>
	
	<br>
	<form name = "RandForm" action = "maps.html" onsubmit ="return randTags();">
	<input type = "text" name = "Rand" autofocus placeholder="# of Random Tags">
	<input type = "submit" value = "Rand That Shit Up!">
	</form>
	<br/>
	Search by Department
	<form action="pagejs.cgi" onsubmit="return searchResults();">
	<select name="dropdown">
	<?php
	// Connecting, selecting database
	$dbconn = pg_connect("host=localhost dbname=postgres user=ubuntu")
	    or die('Could not connect: ' . pg_last_error());

	// Performing SQL query
	$query = 'SELECT DISTINCT dept FROM classes ORDER BY(dept)';
	$result = pg_query($query) or die('Query failed: ' . pg_last_error());

	// Printing results in HTML
	while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
	    foreach ($line as $col_value) {
		echo "<option value=\"$col_value\">$col_value</option>\n";
	    }
	}

	// Free resultset
	pg_free_result($result);

	// Closing connection
	pg_close($dbconn);
	?>
	</select>
	<input type="submit" value="Search"/>
	</form>	
	</div>
  </body>
</html>

