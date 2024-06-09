"""
the goal of this file is to check the realtionship between area, height, wight.

Where is the saturation?

"""


import ROOT
from array import array  
import re
import numpy as np

filelocation = "/Users/haoliangzheng/subMETData/beamOn/Jun07/r00003"

fileName = 1 

file = ROOT.TFile.Open(f"{filelocation}/board{fileName}.root")

if not file or file.IsZombie():
    print("Error opening file.")

else:

    HA_Hist_List = []
    WA_Hist_List = []

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

                #WidthData = []
                #AreaData = []
                #heightData = []

                HeightArea = ROOT.TH2F(f"HeightArea{SubName}", f"height vs Area {SubName}; height; area", 50, 0, 4000, 50, 0, 2000000)
                WidthArea = ROOT.TH2F(f"WidthArea{SubName}", f"Width vs Area {SubName}; Width; area", 50, 0, 4000, 50, 0, 2000000)
                #loop over the pulse data in each channels
                for entry in range(SUBobj.GetEntries()):
                    SUBobj.GetEntry(entry)
                    #heightData.append(SUBobj.height)
                    #WidthData.append(SUBobj.width)
                    #AreaData.append(SUBobj.area)
                    HeightArea.Fill(SUBobj.height,SUBobj.area)
                    WidthArea.Fill(SUBobj.width,SUBobj.area)

                
                #n_points = len(heightData)
                #HeightArea.FillN(n_points, heightData, AreaData ,np.ones(len(heightData))) #weird bug: TypeError: could not convert argument 2 (could not convert argument to buffer or nullptr)
                #WidthArea.FillN(n_points, WidthData, AreaData, np.ones(len(heightData)))

                HA_Hist_List.append(HeightArea)
                WA_Hist_List.append(WidthArea)
            
    
    canvas1 = ROOT.TCanvas("canvas1", "Scatter Plot", 800, 1000)
    canvas1.Divide(2,5)
    for num in range(10):
        canvas1.cd(num+1)
        HA_Hist_List[num].Draw()

    canvas2 = ROOT.TCanvas("canvas2", "Scatter Plot", 8000, 10000)
    canvas2.Divide(2,5)
    for num in range(10):
        canvas2.cd(num+1)
        WA_Hist_List[num].Draw()

    #canvas1.SaveAs("HA.png")
    #canvas2.SaveAs("WA.png")

    # Open the ROOT file
    output_file = ROOT.TFile("multiple_canvases_output.root", "RECREATE")

    # Write both canvases to the file
    canvas1.Write()
    canvas2.Write()

    # Close the ROOT file
    output_file.Close()
    #canvas1.Draw()







                    

