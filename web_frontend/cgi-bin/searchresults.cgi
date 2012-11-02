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
if department !="":
	dept_classes = hpdb.search_by_dept(department)
if title != "":
	title_classes = hpdb.search_class_title(title)
if len(title_classes) != 0 and len(dept_classes) !=0:
	classes = list(set(dept_classes) & set(title_classes));
	sorted(classes,key=operator.itemgetter(1));
else:
	classes.extend(title_classes);	
	classes.extend(dept_classes);
	sorted(classes,key=operator.itemgetter(1));

print """
<form name="dropdown" action="search.cgi" method="POST">
<select name="classcrn" size="%s">""" %str(min(20,len(classes)))
for c in classes:
	print '<option value="'+str(c[4])+'">'+c[0]+' '+str(c[1])+' '+str(c[2])+' - '+c[3]+'</option>'

print """</select>
<br/>
<input type="submit" value="View"/>
</form>
</div>	
</body>
</html>
"""
 
