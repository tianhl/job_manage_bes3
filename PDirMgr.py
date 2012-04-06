#!/ihepbatch/bes/tianhl/programfiles/python25/bin/python2.5 

class PDirMgr:
  
  def scanfDir(self, dir):
    import os
    fileList = []
  
    for eachFile in os.listdir(dir):
      fileList.append(eachFile)
  
    return fileList
	    
