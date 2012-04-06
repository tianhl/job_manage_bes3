#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5

############################################
############################################
class PSubJob:
#===========================================  
  def __init__(self):
    self.__jobList = []
    self.__subList = []
    self.__cmd = ''
    self.__trkFlag = False

    self.clear()
  
  def clear(self):
    self.__jobList = []
    self.__subList = []
    self.__cmdOutput = []
    self.__cmd = ''
  
  def do(self):
    self.__checkArg()
    self.__subJobs()
    
#===========================================  
  def getJobList(self):
    return self.__jobList
  
  def setJobList(self, iList):
    self.__jobList = iList
  
  def getSubList(self):
    if slef.getTrkFlag() == True:
      return self.__subList
    else:
      return ['NONE']

  def getCmd(self):
    return self.__cmd
  
  def setCmd(self, iCmd):
    self.__cmd = iCmd

  def getTrkFlag(self):
    return self.__trkFlag

  def setTrkFlag(self, flag):
    self.__trkFlag = flag
#===========================================  
  def __checkArg(self):
    flag = True
    if self.getJobList().__len__() == 0:
      print 'jobList zero!'
      flag = False 
    if self.getCmd().__len__() == 0:
      print 'command zero!'
      flag = False
    if flag == False:
      self.__del__()
  
  def __subJobs(self):    
    import commands
    jobList = self.getJobList()
    cmd = self.getCmd()
  
    for eachJob in jobList:
      jobCmd = cmd + eachJob
      #print jobCmd
      output = commands.getoutput(jobCmd)
      self.__cmdOutput.append(output)
      #print outPut
      if self.getTrkFlag() == True:
        try:
          temp = output.split('.')
          index = temp.index('torqmaui')
        except:
          print output
        else:	
          queueNumber = temp[index - 1]
          
          if queueNumber.isdigit() == False:
            #print queueNumber
            temp = ''
            for eachLetter in queueNumber:
              if eachLetter.isdigit():
                temp = temp +  eachLetter
            queueNumber = int(temp)    
            
          subJobItem = (queueNumber, eachJob)
          self.__subList.append(subJobItem)
	
#===========================================  
############################################
############################################
def __test():
  cmd = 'boss -q '
  from PDirMgr import PDirMgr
  aDirMgr = PDirMgr()
  dirName = 'jobOptions/'
  aFileList = aDirMgr.scanfDir(dirName)
  jobList = []
  for eachFile in aFileList:
    jobList.append(dirName + eachFile)
  #print jobList  
  aPSubJob = PSubJob()
  aPSubJob.setCmd(cmd)
  aPSubJob.setJobList(jobList)
  aPSubJob.setTrkFlag(True)
  aPSubJob.do()
  print aPSubJob.getSubList()
  
if __name__ == '__main__':
  __test()
