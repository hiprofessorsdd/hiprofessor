# RPI Classlist Parser
# By Tim Treese (RCSID treest)
# 11.1.2012
# For Software Design and Documentation project: HiProfessor

# Usage: 


import re
import sys
import HTMLParser
import hpdb

#AM->PM / PM->AM
def AMPMNot(inp):
  if inp=='AM':
    return 'PM'
  elif inp=='PM':
    return 'AM'
  return ''

#adds an AM or a PM to the start time
def timeSetup(rawStartTime,rawEndTime):
  if rawStartTime is None or rawEndTime is None:
    StartTime=None
    EndTime=None
  else:
    #Finds the Hour part of a time
    HourFinder=re.compile('(.*?):.*')
    #Finds the AM/PM section of the time string
    AMPMFinder=re.compile('(?:.*)([AMP]{2})')
    StartHourRE=HourFinder.search(rawStartTime)
    EndHourRE=HourFinder.search(rawEndTime)
    if StartHourRE is None or EndHourRE is None:
      StartTime=rawStartTime
      EndTime=rawEndTime
    else:
      StartHour=StartHourRE.group(1)
      EndHour=StartHourRE.group(1)
      AMPM=AMPMFinder.search(rawEndTime)
      if AMPM is None:
        #If both times are valid strings but EndTime has no AM/PM, then we don't know what's up and return unmodified times
        StartTime=rawStartTime
      else :
        #If the hour of start is less than or the same than the hour of end, then it's probably in the same AM/PM, and the converse
        if StartHour<=EndHour:
          StartTime=rawStartTime+AMPM.group(1)
        else:
          StartTime=rawStartTime+AMPMNot(AMPM.group(1))
      EndTime=rawEndTime
  return (StartTime,EndTime)


# Turns raw string into array of 5 days
def daySetup(daySTR):
  if daySTR is None:
    return ('* TBD *',None,None,None,None)
  else:
    rc=(re.search("(?: *)(.)(?: *)(.)?(?: *)(.)?(?: *)(.)?(?: *)(.)?",res.group('Days'))).groups()
    if rc is None:
      return ('* TBD *',None,None,None,None)
  return rc

# Turns the raw BUILDING ROOM string into separate strings
def locSetup(locSTR):
  t1 = re.search("(.*?) (.*)",locSTR)
  if t1 is None:
    building = "* TBA *"
    room = "* TBA *"
  else:
    building=t1.group(1)
    room=t1.group(2)
  return (building,room)

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

meetingRE = re.compile('<TR [^>]*>(?:.<TD>.</TD>)+?.<TD>(?:.<span[^>]*>(?P<Title>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Type>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Creds>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<grtp>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Days>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<StartTime>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<EndTime>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Instructor>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final1>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final2>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final3>[^<]*)</span>)?.</TD>.<TD>(?:.<span[^>]*>(?P<Final4>[^<]*)</span>)?',re.DOTALL)



# Now begins the imperative part of the program. Open the file and read it into a string:
if len(sys.argv)!=2:
  print "USAGE: ",argv[0]," <file of classlist>"
f = open(sys.argv[1])
schedule = f.read()

# Partition the whole string by "View TextBooks" (i.e. partitions into lines)..
# Then each line (i.e. element of 'ls') is either just nonsense, a class listing, or a section listing.
partitioner = re.compile('View TextBooks')
ls = partitioner.split(schedule)
# HTMLParser used to unescape (i.e. '&amp' -> '&')
h = HTMLParser.HTMLParser()
prevMatch=''
for i in ls:
  #Check if it is a class listing
  #TODO: If it's not a class listing (i.e. if res is None), then check if it is a meeting listing (i.e. another meeting for the previous class).
  res = classRE.search(i)
  if res is not None:
    print res.group('DEPT')
    days=daySetup(res.group('Days'))
    (StartTime,EndTime)=timeSetup(res.group('StartTime'),res.group('EndTime'))

    hpdb.add_class(res.group('CRN'),h.unescape(res.group('Title')),res.group('DEPT'),res.group('CNum'),res.group('sec'),res.group('Creds'))
    prevMatch=res
    if res.group('Final4') is None:
      hpdb.add_meeting("* TBD *","* TBD *",res.group('Type'),days[0],res.group('CRN'),timeTranslate(StartTime),timeTranslate(EndTime),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))
    else:
      (building,room)=locSetup(res.group('Final1'))
      hpdb.add_meeting(building,room,res.group('Type'),days[0],res.group('CRN'),timeTranslate(StartTime),timeTranslate(EndTime),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))

  else:
    res = meetingRE.search(i)
    if res is not None:
      print "Found a new meeting for CRN ",prevMatch.group('CRN')," with info:\n",res.groups()
      days=daySetup(res.group('Days'))
      (StartTime,EndTime)=timeSetup(res.group('StartTime'),res.group('EndTime'))
      if prevMatch.group('Final4') is None:
        hpdb.add_meeting("* TBD *","* TBD *",res.group('Type'),days[0],prevMatch.group('CRN'),timeTranslate(StartTime),timeTranslate(EndTime),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))
      else:
        t1 = re.search("(.*?) (.*)",res.group('Final1'))
        (building,room)=locSetup(res.group('Final1'))
        print "Building/Room:",building,"/",room
        hpdb.add_meeting(building,room,res.group('Type'),days[0],prevMatch.group('CRN'),timeTranslate(StartTime),timeTranslate(EndTime),0,dayTranslate(days[1]),dayTranslate(days[2]),dayTranslate(days[3]),dayTranslate(days[4]))
