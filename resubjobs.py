#! /usr/bin/python

# Author: Tian Haolai
# Mail: tianhl@ihep.ac.cn
# Date: 2009.03.18

def test(fileName):

  fi = open(fileName, 'r')
  jobList = fi.readlines()
  fi.close()

  errList = []
  import commands
  import os
  jobList = filter(lambda j:  os.path.isfile(j[:-1]), jobList)
  for eachJob in jobList:
    d,f = os.path.split(eachJob[:-1])

    os.chdir(d)
    output = commands.getoutput('dp -q ' + f)
    print output
    

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2 :
    print 'arguments error'
    sys.exit()
  
  test(sys.argv[1]) 
