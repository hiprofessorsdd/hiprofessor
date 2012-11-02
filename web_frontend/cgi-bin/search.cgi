#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;
import pycurl
import cStringIO
import os;
	
print "Content-type: text/html"
print


print """
<html>
<body>
<div id="some_text" style="width:80%; height: auto; margin-left: auto; margin-right:auto;padding: 20px; border: 1px solid black; color:C40000; font-family:verdana; font-size:40px">
<b>HiProfessor</b>
</div>
<br/>
"""
form = cgi.FieldStorage()
crn = form.getvalue("classcrn", "")

if crn!="":
	l = hpdb.get_class_location(crn)
	for loc in l:
		typ = ''
		if loc[9] == 'LEC':
			typ = 'Lecture'
		elif loc[9] == 'STU':
			typ = 'Studio'
		elif loc[9] == 'LAB':
			typ = 'Lab'
		elif loc[9] == 'REC':
			typ = 'Recitation'
		elif loc[9] == 'SEM':
			typ = 'Seminar'
		elif loc[9] == 'TES':
			typ = 'Test day'
		else:
			typ = loc[9]
			
		print """<script>
		parent.loadClass(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
		</script>""" % (loc[0],loc[1],'\''+loc[2]+'\'','\''+str(loc[3])+'\'','\''+loc[4]+'\'','\''+str(loc[5])+'\'','\''+loc[6]+'\'','\''+str(loc[7])+'\'','\''+str(loc[8])+'\'','\''+typ+'\'')
print """<div id="serch" style="width:80%; height: auto; margin-left: auto; margin-right:auto; padding: 20px; border: 1px solid black;font-family:verdana;color:C40000;font-size:18px;">"""
print """<form name="dropdown" action="searchresults.cgi" method="POST">

Department
<br/> 
<select name="dept" >
<option value="" selected="selected"></option>"""

depts = hpdb.get_departments()
for d in depts:
	print '<option value="'+d+'">'+d+'</option>'

print """</select>
<br/>
<br/>
Title <br>
<input type="text" name="title"><br>

<br/>
<input type="submit" value="Search"/>
</form>
<hr/>"""

if cgi.FieldStorage().has_key("ticket"):
	ticket = cgi.FieldStorage()["ticket"].value
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, 'https://cas-auth.rpi.edu/cas/serviceValidate')
	c.setopt(c.POSTFIELDS, 'ticket='+ticket+'&service=http://ec2-107-20-104-15.compute-1.amazonaws.com/cgi-bin/search.cgi')
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	if '<cas:user>' in buf.getvalue():
		print "Welcome user" + buf.getvalue() + "!"
	else:
		print """<form name="login" action="login.cgi">
		<input type="submit" value="Login"/>
		</form>"""
	buf.close()
else: 
	print """<form name="login" style="margin-left:auto;margin-right:auto" action="login.cgi">
	<input type="submit" value="Login"/>
</form>"""


print """</div>
</body>
</html>"""
