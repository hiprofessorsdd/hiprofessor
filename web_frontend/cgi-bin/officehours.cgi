#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;
import pycurl
import cStringIO
import os;
	
print "Content-type: text/html"
print

form = cgi.FieldStorage()
crn = form.getvalue("oh", "")
print '<html>'
print '<body>'
print '<style type="text/css">'
print 'body{'
print '  width:80%; height: auto; margin-left: auto; margin-right:auto;padding: 20px; border: 1px solid black; color:C40000; font-family:verdana; font-size:14px'
print '}'
print '</style>'
user = hpdb.check_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"));

if user=='':
	print 'Please login to add office hours!'
	print '<hr/>'
else: 
	print '<form name="full" action="info.cgi" method="GET">'
	print 'Days'
	print '<br/>'
	print '<select name="day" multiple="multiple" size="5">'
	print '<option value="M" selected="selected">Monday</option>'
	print '<option value="T">Tuesday</option>'
	print '<option value="W">Wednesday</option>'
	print '<option value="R">Thursday</option>'
	print '<option value="F">Friday</option>'
	print '</select>'
	print '<br/>'
	print 'Start Time'
	print '<br/>'
	print '<select name="shour">'
	print '<option value="08">AM 8</option>'
	print '<option value="09">AM 9</option>'
	print '<option value="10">AM 10</option>'
	print '<option value="11">AM 11</option>'
	print '<option value="12">PM 12</option>'
	print '<option value="13">PM 1</option>'
	print '<option value="14">PM 2</option>'
	print '<option value="15">PM 3</option>'
	print '<option value="16">PM 4</option>'
	print '<option value="17">PM 5</option>'
	print '<option value="18">PM 6</option>'
	print '<option value="19">PM 7</option>'
	print '<option value="20">PM 8</option>'
	print '</select>'
	print '<select name="sminute">'
	print '<option value="00">00</option>'
	print '<option value="15">15</option>'
	print '<option value="30">30</option>'
	print '<option value="45">45</option>'
	print '</select>'
	print '<br/>'
	print 'End Time'
	print '<br/>'
	print '<select name="ehour">'
	print '<option value="08">AM 8</option>'
	print '<option value="09">AM 9</option>'
	print '<option value="10">AM 10</option>'
	print '<option value="11">AM 11</option>'
	print '<option value="12">PM 12</option>'
	print '<option value="13">PM 1</option>'
	print '<option value="14">PM 2</option>'
	print '<option value="15">PM 3</option>'
	print '<option value="16">PM 4</option>'
	print '<option value="17">PM 5</option>'
	print '<option value="18">PM 6</option>'
	print '<option value="19">PM 7</option>'
	print '<option value="20">PM 8</option>'
	print '</select>'
	print '<select name="eminute">'
	print '<option value="00">00</option>'
	print '<option value="15">15</option>'
	print '<option value="30">30</option>'
	print '<option value="45">45</option>'
	print '</select>'
	print '<br/>'
	print 'Building'
	print '<br/>'
	print '<select name="building" >'
	locs = hpdb.get_locations();
	for l in locs:
		print '<option value="'+l[0]+'">'+l[0]+'</option>'
	print '</select>'
	print '<br/>'
	print 'Instructor'
	print '<br/>'
	print '<input name="instr"/>'
	print '<br/>'
	print 'Room'
	print '<br/>'
	print '<input name="roomno"/>'
	print '<br/>'
	print '<button name="info" type="submit" value="'+crn+'">Submit</button>'
	print "</form>"
print '<hr/>'
print '<form name="back" action="search.cgi">'
print '<button name="back" type="submit">Back to Search</button>';
print '</form>'
print '</body>'
print '</html>'
