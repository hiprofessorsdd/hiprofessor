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


print '<div id="map_canvas" style="Float:right; width:60%;  height:96% ;margin:10px"></div>'
print '<img style="Float:left;padding:1px" border="0" src="http://i.imgur.com/tsfcS.jpg" alt="HP" width="104" height="90">'
print '<div style="Float:left;padding: 10px;height:55px; color:#C40000; font-family:verdana; font-size:45px">'
print '<b>HiProfessor</b>'
print '</div>'
print '<object name="frm" style="overflow:hidden;Float:left" width="38%" height="83%" data="/cgi-bin/search.cgi"></object>'
print """  </body>
</html>"""


