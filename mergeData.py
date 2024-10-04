


import ROOT
from array import array  
import re
import numpy as np

#filelocation = "/Users/haoliangzheng/subMETData/beamOn/Jun9/r00008"
fileNum = "11"
filelocation = f"/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000{fileNum}"
myDict ={}


#fileName = 1 
for fileName in range(8):

    fileName = fileName+1

    #debug only lookin to board 1
    #if fileName > 2:
    #    break

    file = ROOT.TFile.Open(f"{filelocation}/board{fileName}.root")

    if not file or file.IsZombie():
        print("Error opening file.")

    else:

        keys = file.GetListOfKeys()
        # Iterate over the keys and find TTree objects
        for key in keys:
            obj = key.ReadObj()

            keyINChFolder=obj.GetListOfKeys()

            #sub key is channel based information that connected to the same board
            for subKey in keyINChFolder:
                SUBobj = subKey.ReadObj()
                SubName = SUBobj.GetName()

                if SubName.startswith("pul_"):
                    chanNum=SubName.split("ch")
                    chanNum = chanNum[-1]

                    #WidthData = []
                    #AreaData = []
                    #heightData = []

                    #loop over the pulse data in each channels
                    for entry in range(SUBobj.GetEntries()):
                        #print(SUBobj.GetEntries())
                        #print(entry)
                        
                        SUBobj.GetEntry(entry) #each entry is associate with a single pulse
                        #print(f"fiEve:{SUBobj.iEve}")
                        if f"{SUBobj.iEve}" not in myDict:
                            myDict[f"{SUBobj.iEve}"] = {
                                'height':[],
                                'TCtime':[],
                                'board':[],
                                'chan':[],
                                'eventID':[]
                            }
                        
                        myDict[f"{SUBobj.iEve}"]['height'].append(SUBobj.height)
                        myDict[f"{SUBobj.iEve}"]['TCtime'].append(SUBobj.TCtime)
                        myDict[f"{SUBobj.iEve}"]['board'].append(int(fileName))
                        myDict[f"{SUBobj.iEve}"]['chan'].append(int(chanNum))
                        myDict[f"{SUBobj.iEve}"]['eventID'].append(int(SUBobj.iEve))


                        #test less entry only first five pulse
                        #if SUBobj.iEve > 5:
                        #    break
                        

    

#check the dict(test finished)
print("height")
print(myDict["0"]["height"])
print("height")
print(myDict["1"]["height"])
print("board")
print(myDict["0"]["board"])
print("chan")
print(myDict["0"]["chan"])
print("TCtime")
print(myDict["0"]["TCtime"])
print("eventID")
print(myDict["0"]["eventID"])


#bring the vectors into root file

#branches

height = ROOT.std.vector('Double_t')()
board = ROOT.std.vector('int')()
chan = ROOT.std.vector('int')()
TCtime = ROOT.std.vector('Double_t')()
evenID = ROOT.std.vector('int')()


# Function to create the branches in the new tree
def create_branches(output_tree,height,board,chan,TCtime,evenID):
    output_tree.Branch("chan", chan)
    output_tree.Branch("height", height)
    output_tree.Branch("board", board)
    output_tree.Branch("TCtime", TCtime)
    output_tree.Branch("evenID", evenID)

outname = f"SubMetflat{fileNum}_" + ".root"
output_file = ROOT.TFile(outname, "RECREATE")
output_tree = ROOT.TTree("t", "A flat, lightweight tree for MilliQan sim data")

create_branches(output_tree,height,board,chan,TCtime,evenID)


def populate(dataDict,height,board,chan,TCtime,evenID):
    

    keys=dataDict.keys() #associate with event
    for key in keys:  #loop over the data inside a same event
        height.clear()
        board.clear()
        chan.clear()
        TCtime.clear()
        evenID.clear()
        EventData=dataDict[key]
        #get the number of pulse in the event
        #print(EventData["height"])
        NumPulse=len(EventData["height"])
        for J in range(NumPulse):
            height.push_back(EventData["height"][J])
            chan.push_back(EventData["chan"][J])
            board.push_back(EventData["board"][J])
            TCtime.push_back(EventData["TCtime"][J])
            evenID.push_back(EventData["eventID"][J])
            
        output_tree.Fill()


populate(myDict,height,board,chan,TCtime,evenID)





output_file.Write()
output_file.Close()


                    

