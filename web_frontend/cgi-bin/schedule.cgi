#!/usr/bin/env python
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import hpdb;
import os;

print "Content-type: text/html"
print
if cgi.FieldStorage().has_key("logout"):
	hpdb.clear_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"));
	print '<html><body>'
	print '<meta http-equiv="REFRESH" content="0;url=http://ec2-107-20-104-15.compute-1.amazonaws.com/cgi-bin/search.cgi">'
	print 'Logging out...'
	print '</body></html>'	
else:
	if cgi.FieldStorage().has_key("del"):
		u = hpdb.check_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"));		
		hpdb.delete_from_sched(u,cgi.FieldStorage().getvalue("del"));
	if cgi.FieldStorage().has_key("add"):
		u = hpdb.check_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"));		
		cgifield = cgi.FieldStorage()
		hpdb.add_to_sched(u,cgifield.getvalue("add"));
	print "<html>"
	print '<body id="serch" style="width:80%; height: auto; margin-left: auto; margin-right:auto; padding: 20px; border: 1px solid black;font-family:verdana;color:C40000;font-size:12px;">'
	user = hpdb.check_login(os.getenv("REMOTE_ADDR"),os.getenv("HTTP_USER_AGENT"))
	if user != "":
		sched = hpdb.get_sched(user);
		print "<p><big><big><b>Schedule for user "+user+":</b></big></big></p><hr/>";
		for s in sched:
			info = hpdb.get_class_location(s[1]);
			print "<big>"+info[0][4]+" "+str(info[0][5])+" - "+info[0][6]+"</big>";
			for i in info:
				print '<br/>'
				print i[2]+" "+i[3];
				print '<br/>'
				for d in i[10:14]:
					print d;
				print str(i[7])+" - "+str(i[8]);
				print i[9]
				print '<br/>'
			print '<form name="user" action="schedule.cgi" method="GET">'
			print '<button name="del" type="submit" value="%s">Delete</button>' % (s[1],);
			print "</form>"
	else:
		print "Login first please!"
	print '<hr/>'
	print '<form name="back" action="search.cgi">'
	print '<button name="back" type="submit">Back to Search</button>';
	print '</form>'
	print '</body></html>'
