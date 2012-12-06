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
crn = form.getvalue("info")
if cgi.FieldStorage().has_key("day"):
	days = form.getvalue("day", "")
	if type(days) == type(''):
		days = [days];
	days = days + ['']*(5-len(days))
	starttime = form.getvalue("shour", "") +":"+ form.getvalue("sminute","00")+":00"
	endtime = form.getvalue("ehour", "") +":"+ form.getvalue("eminute","00")+":00"
	instructor = form.getvalue("instr", "")
	building = form.getvalue("building", "")
	room = form.getvalue("roomno", "")
	user = hpdb.check_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"))
	hpdb.add_office_hours(crn,building,room,starttime,endtime,instructor,days[0],days[1],days[2],days[3],days[4],user);

info = hpdb.get_full_info(crn);

print '<html>'
print '<body>'
print '<style type="text/css">'
print 'body{'
print '  width:80%; height: auto; margin-left: auto; margin-right:auto;padding: 20px; border: 1px solid black; color:C40000; font-family:verdana; font-size:12px'
print '}'
print '</style>'
print '<b><big>'+info[0][4]+' '+str(info[0][5])+' - '+info[0][6]+'</b></big><br/>';
print '<b><big>Section Number</big></b>'
print info[0][16];
print '<br/><b><big>Credit Hours</big></b>'
print info[0][15];
print '<br/><b><big>CRN</big></b>'
print crn;
print '<hr/>'
for i in info:
	print '<b><big>Type</big></b>'
	print i[9]
	print '<br/><b><big>Location</big></b>'
	print i[2] + ' ' + i[3]
	print '<br/><b><big>Days</big></b>'
	for j in i[10:14]:
		print j
	print '<br/><b><big>Start Time</big></b>'
	print i[7]
	print '<br/><b><big>End Time</big></b>'
	print i[8]
	print '<br/>'
officehours = hpdb.get_office_hours(crn);
if len(officehours) != 0:
	print '<hr/>'
	for oh in officehours:  
		print '<b><big>Office Hours Added by RCSID</big></b>'
		print oh[10]	
		print '<br/><b><big>Instructor</big></b>'
		print oh[4]	
		print '<br/><b><big>Location</big></b>'
		print oh[0] + ' ' + oh[1]
		print '<br/><b><big>Days</big></b>'
		for o in oh[5:9]:
			print o
		print '<br/><b><big>Start Time</big></b>'
		print oh[2]	
		print '<br/><b><big>End Time</big></b>'
		print oh[3]
		print '<br/>'

print '<hr/>'
print '<form name="back" action="search.cgi">'
print '<button name="back" type="submit">Back to Search</button>';
print '</form>'
print '</body>'
print '</html>'

