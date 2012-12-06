#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;



print """
<!DOCTYPE html>
<html>
<p>
"""

arguments = cgi.FieldStorage()
crn=arguments.getvalue('crn','')
if crn is None:
  print "CLASS NOT FOUND by None"
elif crn=='':
  print "CLASS NOT FOUND by empty string"
else:
  clas=hpdb.get_class_by_crn(crn)
  print "Returned was ",clas


print "</p>"

print """  </body>
</html>"""


