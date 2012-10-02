import re
import sys

class Section:
  CRN=0
  def __str__(self):
    return self.title+"\n"+self.CRN+" "+self.DEPT+"-"+self.num

print "filename is ",sys.argv[1]

#The regex that does all of the work:
#[0-9]{5} matches the CRN
#[A-Z]{4} matches the department
#[0-9]{4} matches the course number
#[0-9]{2} matches the section number, if any
#(.*?)(<span.*?>) moves you to the next field
#(/*?) is the next field
#(</span>) terminates this field
#repeat the final 3 steps to keep getting fields.
p = re.compile('([0-9]{5}) ([A-Z]{4})-([0-9]{4})(-([0-9]{2}))?(.*?)(<span.*?>)(.*?)(</span>)',re.DOTALL)

#The file passed in. Read it into one string in memory.
f = open(sys.argv[1])
schedule = f.read()

length=len(schedule)
loc=0
sections=[]
while True:
  sec = Section()
  m = p.search(schedule,loc)
  if not m:
    break
  loc=m.end()
  sec.CRN=m.group(1)
  sec.DEPT=m.group(2)
  sec.num=m.group(3)
  sec.sec=m.group(5)
  sec.title=m.group(8)
  print sec
  sections.append(sec)
print "Done!! Total length=",len(sections)
