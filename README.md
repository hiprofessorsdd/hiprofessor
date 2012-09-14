hiprofessor
===========

hiprofessor is a webapp (first-stage plans are RPI-specific) that will show students a map of class schedules and professor office hours.

The structure currently is:
./pull\_schedules
  Contains files for pulling and parsing the SIS schedule html file.
  Current progress is just a bash script to pull the .htm file.
  Future needs: a more robust script (python/perl) that parses the .htm file and pushes the results into the database (which doesn't yet exist)
