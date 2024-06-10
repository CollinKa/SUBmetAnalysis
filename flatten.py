"""
The goal of this file is to flatten the default submet root tree.
To use Uproot properly, each entry should associate with event rater that pulse.

I only extract data from pul_chX(pulse-based) and put them back to the corresponding evnet array

"""


import ROOT
from array import array  
import re

#get the number event for the current file

filelocation = "/Users/haoliangzheng/subMETData/beamOn/Jun9/r00008"

fileName = 1 

file = ROOT.TFile.Open(f"{filelocation}/board{fileName}.root")

if not file or file.IsZombie():
    print("Error opening file.")

else:
    HA_Hist_List = []
    WA_Hist_List = []
    iEveMax = -1 #used to find the max evnet number

    keys = file.GetListOfKeys()
    for key in keys:
        obj = key.ReadObj()
        keyINChFolder=obj.GetListOfKeys()
        
        for subKey in keyINChFolder:
            SUBobj = subKey.ReadObj()
            SubName = SUBobj.GetName()

            if SubName.startswith("pul_"):
                #iEveMax = -1 #used to find the max evnet number
                #for entry in range(SUBobj.GetEntries()):
                #    iEveNum=SUBobj.iEve
                #    if iEveMax <= iEveNum:
                #        iEveMax = iEveNum
                SUBobj.GetEntry(SUBobj.GetEntries()-1)
                print(SUBobj.GetName())
                print(SUBobj.iEve)
                if iEveMax <= SUBobj.iEve:
                    iEveMax = SUBobj.iEve


        print(f"the max event {iEveMax}")




