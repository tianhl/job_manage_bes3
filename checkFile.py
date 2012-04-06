#! /ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5
def checkFiles(fileList):
  import ROOT
  ROOT.gSystem.Load('/afs/ihep.ac.cn/bes3/offline/sw/dist/boss/6.5.0/InstallArea/i386_linux26/lib/libRootEventData.so')
  def checkDST(fname):
    try:
      f = ROOT.TFile(fname)
      t = f.Get('Event')
      if (t.GetEntries()==0):
        return True
    except BaseException, e:
      print 'ERROR: ', fname ,':  ' ,e
      return True
  
  errlist = filter(lambda f: checkDST(f), fileList)
  print 'Check Files: ', len(fileList)
  print 'Error Files: ', len(errlist)
  return errlist
  


def scanFiles(directoryName, postfix):
  import os
  fileList = map(lambda f: os.path.join(directoryName, f), os.listdir(directoryName)) #list directory
  fileList = filter(lambda f: os.path.isfile(f) and\
     os.path.splitext(os.path.split(f)[1])[1].lower()[1:] == postfix, fileList) # remove no file and no root file
  return fileList


if __name__ == '__main__':
  import sys
  import os
  if len(sys.argv) < 3 :
    print 'arguments error'
    print 'checkFile.py fileNamePostfix dirName'
    sys.exit()

  dir_name = os.path.normpath(os.path.abspath(sys.argv[2]))
  postfix = sys.argv[1]
  print dir_name
  fileList = scanFiles(dir_name,postfix )
  errList = checkFiles(fileList)

  ef = open(os.path.join(dir_name, 'errorFile.txt'), 'w')
  ef.writelines(errList)
  ef.close()
  print 'log file is: ', os.path.join(dir_name, 'errorFile.txt')

