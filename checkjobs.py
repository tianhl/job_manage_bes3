#! /usr/bin/python

# Author: Tian Haolai
# Mail: tianhl@ihep.ac.cn
# Date: 2009.03.18

def test(date, type):
  import os
#  env_str_list = os.environ['PACKAGE_POLICY_FOR_PROJECT_GAUDIROOT']
  env_str_list = os.environ['TESTRELEASEROOT']
#  directory = env_str_list[0:env_str_list.find('cmt/')] + 'run/' + type + '/'
  directory = env_str_list + '/run/bb_rec/'
  output_directory = directory + date
  if os.path.exists(output_directory) and os.path.isdir(output_directory):
    os.chdir(output_directory)
  else: 
    print output_directory + ' does not exist!'
    import sys
    sys.exit()

  fi = open(date + '.joblog', 'r')
  jobList = fi.readlines()
  fi.close()

  errList = []
  import commands
  jobList = filter(lambda j:  os.path.isfile(j[:-1]), jobList)
  nSucessfulJob = 0
  nErrorJob     = 0
  for eachJob in jobList:
    flag0 = False
    flag1 = False

    output = commands.getoutput('grep "ApplicationMgr       INFO Application Manager Finalized successfully" ' + eachJob[:-1])
    if output.find('ApplicationMgr       INFO Application Manager Finalized successfully') == -1:
      flag0 = True
        
    output = commands.getoutput('grep "ApplicationMgr       INFO Application Manager Terminated successfully" ' + eachJob[:-1])
    if output.find('ApplicationMgr       INFO Application Manager Terminated successfull') == -1:
      flag1 = True
    
    if(flag0 or flag1):
      nErrorJob += 1
      errList.append(eachJob[:-9] + '\n')
    else:
      nSucessfulJob += 1
 
  print 'Total jobs: ', jobList.__len__()
  print 'Sucessful jobs: ', nSucessfulJob 
  print 'Error jobs: ', nErrorJob 
  print 'Detail information: ', output_directory + '/' + data + '.joberr'

  fo = open(date + '.joberr', 'w')
  fo.writelines(errList)
  fo.close()

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3 :
    print 'arguments error, usage:'
    print 'checkJob.py data type. type include bb_rec, vertex and lumi'
    sys.exit()
 
  data = sys.argv[1] 
  type = sys.argv[2] 

  test(data, type) 
