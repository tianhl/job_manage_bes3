#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5

###############################################
###############################################
class PTrkJob:
#=============================================
  def __init__(self, iList = []):
    self.__jobList = []
    self.__statDic = {}
    self.setJobList(iList)
    jobList = self.getJobList()

    for eachJob in jobList:
      self.__statDic[eachJob] = 'N'

    self.update()  
    
	
  def update(self):
    qStat = self.__getStat()
    jobList = self.getJobList()

    for eachJob in jobList:
      try:
	qStat[eachJob]
      except:
	  self.__statDic[eachJob] = 'N'
      else:
        self.__statDic[eachJob] = qStat[eachJob]
  
#=============================================
  def getJobList(self):
    return self.__jobList

  def setJobList(self, iList):
    self.__clean()
    self.__jobList = iList

  def getStatDic(self):
    return self.__statDic

#=============================================
  def __clean(self):
    #print 'clean()'
    self.__jobList = []
    self.__statDic = {}
   
  def __getStat(self):
    import commands
    aList = commands.getoutput('qstat').split('\n')
    qStatDic = {}
    
    nl = 0
    for eachItem in aList:
      nl = nl + 1
      #print nl
      if nl <= 2:
	continue
 
      #print eachItem 
      itemList = eachItem.split()
      #print itemList
      temp = int(itemList[0].split('.')[0])
      qStatDic[temp] = itemList[4]

    return qStatDic  
#=============================================
###############################################
###############################################

def __test():
  aList = [191557, 191489, 123]
  #aPTrkJob = PTrkJob(aList)
  aPTrkJob = PTrkJob()
  print aPTrkJob.getStatDic()
  aPTrkJob.update()
  print aPTrkJob.getStatDic()
  
if __name__ == '__main__':
  __test()
