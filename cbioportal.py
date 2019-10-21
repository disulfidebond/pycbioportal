class CbioportalObj:
    def __init__(self, serverURL, outputString = "output", outputDF = pd.DataFrame()):
        self.serverURL = serverURL
        self.outputString = outputString
        self.outputDF = outputDF
        
    def specifyQuery(self, s):
        # setter method
        self.serverURL = self.serverURL + s
        
class CbioportalDF(CbioportalObj):
    # returns pandas DF of output
    def getCaseList(self):
        import requests
        import pandas as pd
        import numpy
        r = requests.get(self.serverURL, headers={"Content-Type" : "application/text"})
        if not r.ok:
            print("Error with " + str(self.queryString))
        else:
            print("Success")
            dataString = str(r.content)
            dataString_list = dataString.split('\\n')
            dataListItems = [x.split('\\t') for x in dataString_list]
            dataFrameHeaders = dataListItems[0]
            dataList = dataListItems[1:]
            dataFrameIDs = [x for x,y in enumerate(dataFrameHeaders)]
            dataFrameHeaderDict = dict(zip(dataFrameIDs, dataFrameHeaders))
            df = pd.DataFrame(dataList)
            self.outputDF = df.rename(columns=dataFrameHeaderDict)
    def getOutputDF(self):
        return self.outputDF

class CbioportalStr(CbioportalObj):
    # returns string of output
    def getCaseList(self):
        import requests
        r = requests.get(self.serverURL, headers={"Content-Type" : "application/text"})
        if not r.ok:
            print("Error with " + str(self.queryString))
        else:
            print("Success")
            dataInput = str(r.content)
            self.outputString = dataInput
    def getOutputStr(self):
        return self.outputString


