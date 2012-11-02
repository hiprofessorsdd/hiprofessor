#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;
 



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
  </head>"""

print  '<body onload="initialize()">'


print """<div id="map_canvas" style="Float:right; width:60%;  height:96% ;margin:10px"></div>
        <object style="overflow:hidden" width="38%" height="80%" data="/cgi-bin/search.cgi"></object>"""
print """  </body>
</html>"""


