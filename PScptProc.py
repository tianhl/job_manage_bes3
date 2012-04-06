#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5

# Author: Tian Haolai
# Mail: tianhl@ihep.ac.cn
# Date: 2009.03.17

############################################
############################################
class PScptProc:
  def __init__(self):
    self.__srcScptName = 'srcScpt/run.mac'
    self.__dstScptName = 'test.txt'
    self.__srcLines = []
    self.__dstLines = []
    self.__repList = []

#===========================================
  def do(self):
    self.__init()
    
    for eachLine in self.__srcLines:
      #print self.scptProc(eachLine)
      self.__dstLines.append(self.scptProc(eachLine)) 

    self.__finalize()
    self.__clear()
    
  def scptProc(self, iLine = ''):
    print 'PScptProc.scptProc() must be reloaded'
    #print iLine
    return iLine
    pass
    
#===========================================
  def getSrcScptName(self):
    return self.__srcScptName

  def setSrcScptName(self, iName = ''):
    self.__srcScptName = iName

  def getDstScptName(self):
    return self.__dstScptName

  def setDstScptName(self, iName = ''):
    self.__dstScptName = iName

  def getRepTuple(self):
    aTuple = self.__repList
    return aTuple

  def setRepTuple(self, iTuple):
    if type(iTuple) == tuple:
      self.__repList = iTuple
    else:
      print 'error when setRepTuple()'
    
#===========================================
  def __init__(self):
    self.__srcLines = []
    self.__dstLines = []
    self.__repList = []
    
  def __init(self):
    srcFile = open(self.getSrcScptName(), 'r')
    self.__srcLines = srcFile.readlines()
    srcFile.close()

  def __finalize(self):
    #print self.__dstLines
    #print self.getDstScptName()
    dstFile = open(self.getDstScptName(), 'w')
    dstFile.writelines(self.__dstLines)
    dstFile.close()

  def __clear(self):
    self.__srcScptName = 'srcScpt/run.mac'
    self.__dstScptName = 'test.txt'
    self.__srcLines = []
    self.__dstLines = []
    self.__repList = []

############################################
############################################
def __test():
  aPScptProc = PScptProc()
  aPScptProc.setSrcScptName('srcScpt/run.mac')
  aPScptProc.setDstScptName('test.txt')
  aPScptProc.do()
  

if __name__ == '__main__':
  __test()
