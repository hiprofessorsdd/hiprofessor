#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb
import operator
 
print "Content-type: text/html"
print

print """
<html>

<head><title>Search Results</title></head>

<body>"""
print """<div id="serch" style="width:80%; height: auto; margin-left: auto; margin-right:auto; padding: 20px; border: 1px solid black;font-family:verdana;color:C40000;font-size:18px;">
<h3> Classes Found </h3>
"""

form = cgi.FieldStorage()
department = form.getvalue("dept", "")
title = form.getvalue("title", "")
dept_classes = []
title_classes = []
classes = [];
if department !="" and title == "":
	classes = hpdb.search_by_dept(department)
elif title != "" and department == "":
	classes = hpdb.search_class_title(title)
elif department != "" and title != "":
	classes = hpdb.search_title_and_dept(title,department);
else:
	pass;
#	classes.extend(title_classes);	
#	classes.extend(dept_classes);

print """
<form name="dropdown" action="search.cgi" method="POST">
<select name="classcrn" size="%s">""" %str(max(1,min(25,len(classes))))
if len(classes) != 0:
	for c in classes:
		print '<option value="'+str(c[4])+'">'+c[0]+' '+str(c[1])+' '+str(c[2])+' - '+c[3]+'</option>'
else:
	print '<option value="0">None</option>'

print """</select>
<br/>
<input type="submit" value="View"/>
</form>
<hr/>"""

print '<form name="back" action="search.cgi">'
print '<button name="back" type="submit">Back to Search</button>';
print '</form>'

print """
</div>	
</body>
</html>
"""
