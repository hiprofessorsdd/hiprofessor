#!/usr/bin/env python

import psycopg2
import operator

def add_class(crn,title,dept,course_no,section_no,credit_hours):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s,%s)",(crn,title,dept,course_no,section_no,credit_hours));
	conn.commit();
	cur.close();
	conn.close();

def add_meeting(location,room,meeting_type,day1,crn,start_time,end_time,prof_rcs='',day2='',day3='',day4='',day5=''):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("INSERT INTO meetings VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(location,meeting_type,day1,day2,day3,day4,day5,start_time,end_time,prof_rcs,crn,room));
	conn.commit();
	cur.close();
	conn.close();

def add_professor(fname,lname,rcsid = ''):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("INSERT INTO professors VALUES (DEFAULT,%s,%s,%s)",(fname,lname,rcsid));
	conn.commit();
	cur.close();
	conn.close();

#def add_office_hours(crn,):
#	conn = psycopg2.connect("dbname=postgres user=postgres password=h()wdyPr0f");
#	cur = conn.cursor();
#	cur.execute("INSERT INTO meetings VALUES (DEFAULT,%s,%s,%s)",(fname,lname,rcsid));
#	conn.commit();
#	cur.close();
#	conn.close();

def add_location(bname,lati,longi):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("INSERT INTO locations VALUES (%s,%s,%s)",(bname,lati,longi));
	conn.commit();
	for record in cur:
		print record
	cur.close();
	conn.close();

def get_departments():
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT DISTINCT dept FROM classes");
	conn.commit();
	depts = [];
	for record in cur:
		depts.append(record[0]);
	cur.close();
	conn.close();
	depts.sort();
	return depts
	
def get_classes():
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT title,dept,course_no FROM classes");
	conn.commit();
	classes = [];
	for record in cur:
		classes.append(record);
	cur.close();
	conn.close();
	sorted(classes,key=operator.itemgetter(2));
	return classes;
	
def get_professors():
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT lastname FROM professors");
	conn.commit();
	for record in cur:
		print record
	cur.close();
	conn.close();

def search_professors(serch):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT lastname FROM professors WHERE lastname ILIKE \%%s\%",(serch,));
	conn.commit();
	for record in cur:
		print record
	cur.close();
	conn.close();	

def search_class_title(serch):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT dept,course_no,section,title,crn FROM classes WHERE title ILIKE \'%%%s%%\'"%serch);
	conn.commit();
	classes = [];
	for record in cur:
		classes.append(record);
	cur.close();
	conn.close();	
	sorted(classes,key=operator.itemgetter(1));
	return classes;

def search_professors(serch):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT lastname FROM professors WHERE lastname ILIKE \%%s\%",(serch,));
	conn.commit();
	for record in cur:
		print record
	cur.close();
	conn.close();	
	
def search_by_dept(dept):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT dept,course_no,section,title,crn FROM classes WHERE dept LIKE %s",(dept,));
	conn.commit();
	classes = [];
	for record in cur:
		classes.append(record);
	cur.close();
	conn.close();
	sorted(classes,key=operator.itemgetter(1));
	return classes;

def get_class_location(crn):
	conn = psycopg2.connect("dbname=postgres user=ubuntu");
	cur = conn.cursor();
	cur.execute("SELECT l.latitude,l.longitude,l.building,m.room_no,c.dept,c.course_no,c.title,m.start_time,m.end_time,m.type \
			FROM locations l, meetings m, classes c\
			WHERE m.crn = %s AND c.crn = %s AND m.location ILIKE l.building",(int(crn),int(crn)));
	conn.commit();
	l = [];
	for c in cur:
		l.append(c);
	cur.close();
	conn.close();
	return l;	
