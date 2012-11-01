# RPI Classlist Parser
# By Tim Treese (RCSID treest)
# 11.1.2012
# For Software Design and Documentation project: HiProfessor

# Usage: 


import re
import sys
import HTMLParser
import hpdb

# Turns None into '' for the database's sanity
def dayTranslate(day):
  if day is None:
    return ''
  else:
    return day

# Deals with Nones by making them a recognizeable and unlikely time
def timeTranslate(time):
  if time is None:
    return '12:34:56AM'
  elif time=='** TBA **':
    return '12:34:56AM'
  elif time=='* TBA *':
    return '12:34:56AM'
  else:
    return time

# The Regex that does the magic. Group listing identified below
classRE = re.compile('(?P<CRN>[0-9]{5}) (?P<DEPT>[A-Z]{4})-(?P<CNum>[0-9]{4})(?:-(?P<sec>[0-9]{2}))</span>.</TD>.<TD>(?:.<span[^>]*>(?P<Title>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Type>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Creds>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<grtp>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Days>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<StartTime>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<EndTime>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Instructor>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final1>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final2>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final3>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final4>[^<]*)</span>)?',re.DOTALL)
#so groups are:
# CRN
# DEPT
# CNum (course number)
# sec
# Title
# Type
# Creds
# grtp
# Days
# StartTime
# EndTime
# Instructor
# Final1 (can be building/room or first of three capacities)
# Final2 (can be first or second of three capacities)
# Final3
# Final4 (will be None of building/room not provided)


# Now begins the imperative part of the program. Open the file and read it into a string:
if argc!=2:
  print "USAGE: ",argv[0]," <file of classlist>"
f = open(sys.argv[1])
schedule = f.read()

# Partition the whole string by "View TextBooks" (i.e. partitions into lines)..
# Then each line (i.e. element of 'ls') is either just nonsense, a class listing, or a section listing.
partitioner = re.compile('View TextBooks')
ls = partitioner.split(schedule)
# HTMLParser used to unescape (i.e. '&amp' -> '&')
h = HTMLParser.HTMLParser()
for i in ls:
  #Check if it is a class listing
  #TODO: If it's not a class listing (i.e. if res is None), then check if it is a meeting listing (i.e. another meeting for the previous class).
  res = classRE.search(i)
  if res is not None:
#    print res.groups()
    if res.group('Days') is None:
      days=('* TBD *',None,None,None,None)
    else:
      days=(re.search("(?: *)(.)(?: *)(.)?(?: *)(.)?(?: *)(.)?(?: *)(.)?",res.group('Days'))).groups()
    hpdb.add_class(res.group('CRN'),h.unescape(res.group('Title')),res.group('DEPT'),res.group('CNum'),res.group('sec'),res.group('Creds'))
    if res.group('Final4') is None:
      hpdb.add_meeting("* TBD *","* TBD *",res.group('Type'),days[0],res.group('CRN'),timeTranslate(res.group('StartTime')),timeTranslate(res.group('EndTime')),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))
    else:
      t1 = re.search("(.*?) (.*)",res.group('Final1'))
      if t1 is None:
        building = "* TBA *"
        room = "* TBA *"
      else:
        building=t1.group(1)
        room=t1.group(2)
      hpdb.add_meeting(building,room,res.group('Type'),days[0],res.group('CRN'),timeTranslate(res.group('StartTime')),timeTranslate(res.group('EndTime')),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))
