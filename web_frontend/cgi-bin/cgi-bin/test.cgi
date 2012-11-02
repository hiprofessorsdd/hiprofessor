#!/usr/bin/env python

import cgi
import os;
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;
import pycas;
import Cookie;

status, rid, cookie = pycas.login("https://cas-auth.rpi.edu","http://ec2-107-20-104-15.compute-1.amazonaws.com/cgi-bin/login.cgi");

print cookie

CAS_MSG = (
"CAS authentication successful.",
"PYCAS cookie exceeded its lifetime.",
"PYCAS cookie is invalid (probably corrupted).",
"CAS server ticket invalid.",
"CAS server returned without ticket while in gateway mode.",
)

print "Content-type: text/html"
print cookie
print
print """
<html>
<head>
<title>
castest.py
</title>
<style type=text/css>
td {background-color: #dddddd; padding: 4px}
</style>
</head>
<body>
<h2>pycas.py</h2>
<hr>
"""
#  Print browser parameters from pycas.login
if cgi.FieldStorage().has_key("ticket"):
	ticket = cgi.FieldStorage()["ticket"].value
else:
	ticket = ""

in_cookie = os.getenv("HTTP_COOKIE")

print """
<p>
<b>Parameters sent from browser</b>
<table>
<tr> <td>Ticket</td> <td>%s</td> </tr> 
<tr> <td>Cookie</td> <td>%s</td> </tr> 
</table>
</p>""" % (ticket,in_cookie)


#  Print output from pycas.login
print """
<p>
<b>Parameters returned from pycas.login()</b>
<table>
<tr><td>status</td><td> <b>%s</b> - <i>%s</i></td></tr>
<tr><td>id</td><td> <b>%s</b></td></tr>
<tr><td>cookie</td><td> <b>%s</b></td></tr>
</table>
</p>
</body></html>""" % (status,CAS_MSG[status],id,cookie)
