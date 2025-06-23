"""
The goal of this file is to find DT around same board


a = ((x / 2) + 1) * 2 
b = -1 if y < 4 , else 0
board number a + b



"""




import ROOT as r
import os
import numpy as np
import array
import sys
import statistics



#Method for finding Dt for data within a single muon bunch
def Dt(x,y,l,t,eventIndex,a = 0,cosmicVeto=True):
    data=zip(x,y,l,t)
    tl1 = []
    tl2 = []
    xl1 = []
    xl2 = []
    yl1 = []
    yl2 = []
    B1l1 =[] #pulse time at board 1 layer 1
    B1l2 =[] #pulse time at board 1 layer 2
    B2l1 =[]
    B2l2 =[]
    B3l1 =[]
    B3l2 =[]
    B4l1 =[]
    B4l2 =[]
    B5l1 = []
    B5l2 = []
    B6l1 = []
    B6l2 = []
    B7l1 = []
    B7l2 = []
    B8l1 = []
    B8l2 = []
    B9l1 = []
    B9l2 = []
    B10l1 = []
    B10l2 = []
    boardNestl1 = [[] for _ in range(10)]
    boardNestl2 = [[] for _ in range(10)]

    tL2_L1 = [[] for _ in range(10)]

    l1Hit = 0
    l2Hit = 0
    chanNo = -10

     
    #if cosmicVeto:
    #    if (0 in x) or (9 in x) or (7 in y): return tL2_L1
    
    #find the first pulse at each layer
    for x,y,l,t in data:
        print(f"x {x}")
        a = ((int(x) // 2) + 1) * 2 
        print(f"a {a}")
        if y < 4: b = -1
        else: b =0
        boardNum = a + b
        #print(f"boardNum {boardNum}")

        if l == 0:
            boardNestl1[int(boardNum-1)].append(t)
            l1Hit = 1
            xl1.append(x)
            yl1.append(y)
            tl1.append(t)

                            
        if l == 1:
            boardNestl2[int(boardNum-1)].append(t)
            l2Hit = 1
            xl2.append(x)
            yl2.append(y)
            tl2.append(t)
               
    #if (len(xl2) == 0) or (len(xl1) == 0): return [] , -100,-100
    #for x2,y2,t2 in zip(xl2,yl2,tl2):
    #    for x1,y1,t1 in zip(xl1,yl1,tl1):
    #        Da = ((x1 - x2)** 2)  +  ((y1 - y2)**2) 
    #        if Da <= a:
    #            tL2_L1.append(t2 - t1)

    for i, (subL1arr,subL2arr) in enumerate(zip(boardNestl1,boardNestl2)):
        if (len(subL1arr) == 0) or (len(subL2arr) == 0): continue
        for t1 in subL1arr:
            for t2 in subL2arr:
                tL2_L1[i].append(t2 - t1)


    return tL2_L1
        

    
#----------------------------------------------------------------------------------
#main function
"""
fileDit = "/Users/haoliangzheng/subMETData/beamOff/KUmergefile/merged"
file_names = []
for file in os.listdir(fileDit):
    if file.endswith(".root"):
        file_names.append(f"/Users/haoliangzheng/subMETData/beamOff/KUmergefile/merged/{file}")
#print(file_names)
"""

#file_names = ["/Users/haoliangzheng/subMETData/V3Data/SUBMET/merged/r00020_event.root"]
#file_names = ["/Users/haoliangzheng/subMETData/V3Data/SUBMET/r00020/merged_r00020_event.root"]
#file_names = [f"/Users/haoliangzheng/subMETData/V3Data/SUBMET/2025MayVer/r000{sys.argv[1]}_spill.root"]
file_names = [
    f"/Users/haoliangzheng/subMETData/V3Data/SUBMET/2025MayVer/r{index:05d}_spill.root"
    for index in range(20, 22)
]

#file_names= ["/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00047_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00048_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00049_event.root"]

#data collection window
hegithCut = 3000 #(for TDC height)

#areaCut = 0  #lower bound (as if doesn't exist)
areaCut = 150000
areaUpBound = 230000
widthBound = 100#(TDC)
TDCrmsabeV = 2 #(TDC)

#areaUpBound = 23000000000 #upper bound (as if doesn't exist)  

sig = 13 #standard deviation
MuonBunchTime = [311,786,1262,1742,2216,2694,3170,3600] # mean of 8 different muon bunches
BunchNumber = 0
Num1hitPL = 0 # count the number of one hit per layer process (at most 1 process per bunch)
numberOfProcessFile = 0

Dt_Chans = [[] for _ in range(80)]# Create 80 empty lists to save the Dt value for each channels

#histograms
r.gROOT.SetBatch(False)
c1 = r.TCanvas("c1", "c1", 800, 600)
B1Dt = r.TH1F("B1Dt", "Board 1 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B2Dt = r.TH1F("B2Dt", "Board 2 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B3Dt = r.TH1F("B3Dt", "Board 3 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B4Dt = r.TH1F("B4Dt", "Board 4 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B5Dt = r.TH1F("B5Dt", "Board 5 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B6Dt = r.TH1F("B6Dt", "Board 6 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B7Dt = r.TH1F("B7Dt", "Board 7 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B8Dt = r.TH1F("B8Dt", "Board 8 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B9Dt = r.TH1F("B9Dt", "Board 9 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)
B10Dt = r.TH1F("B10Dt", "Board 10 Dt(TDC);Dt;number of pulse pair ", 60, -30, 30)

hist_list = []
for i in range(10):
    hist = r.TH1F(f"DTboard{i+1}", f"Histogram board {i +1}", 60, -30, 30)
    hist_list.append(hist)



STDl1hist = r.TH1F("STDl1hist", "STD Histogram;std in TDC;number of events", 40, 0, 20)
STDl2hist = r.TH1F("STDl2hist", "STD Histogram;std in TDC;number of events", 40, 0, 20)

nhits = r.TH1F("nhits", f"nhits height > {hegithCut} & sigma {sig};num of pulse;number of event ", 30, 0, 30)



DtSet = []#Dt data from 8 beam muon bunches
stdL1 = []
stdL2 = []
twolayers = 0 #Count the number of data pairs that can be used to find Dt

for file_name in file_names:
    if not os.path.exists(file_name):
        print(f"File not found: {file_name}")
        continue  # Skip to the next file
     
    file = r.TFile.Open(file_name, "READ")
    print(f"processing file {file_name}")
    # Get the tree
    tree = file.Get("tree")
    if not tree or not isinstance(tree, r.TTree):
        continue

    #load the braches
    TDCheight = r.std.vector('double')()
    TDCtime = r.std.vector('double')()
    TDCwidth = r.std.vector('double')()
    area = r.std.vector('double')()

    ix = r.std.vector('unsigned short')()
    iy = r.std.vector('unsigned short')()
    il = r.std.vector('unsigned short')()
    RMSv = r.std.vector('double')()

    event_id = array.array('L', [0])

    tree.SetBranchAddress("pulse_area",area)
    tree.SetBranchAddress("pulse_volt_height", TDCheight)
    tree.SetBranchAddress("pulse_time_is", TDCtime)
    tree.SetBranchAddress("pulse_time_fwhm", TDCwidth)
    tree.SetBranchAddress("pulse_ix", ix)
    tree.SetBranchAddress("pulse_iy", iy)
    tree.SetBranchAddress("pulse_il", il)
    tree.SetBranchAddress("event_volt_rms_abe", RMSv)

    tree.SetBranchAddress("event_id", event_id)

    numberOfProcessFile += 1
    


    #GetEntries
    TotalEntries=tree.GetEntries()
    

    for index in range(TotalEntries):
        #print(f"entry index{index}")
        tree.GetEntry(index)

        #futher rejection of cosmic muon
        #if (0 in list(ix)) or (9 in list(ix)) or (7 in list(iy)): continue
        #else: print(f"current event is pass cosmic veto 2 {index}")


        #print(f"Entry {index}: evt = {event_id[0]}")  # Access the value from the buffer
        #collect location index and pulse time for data in 8 different bunches
        bunch1x = []
        bunch1y = []
        bunch1l = []
        bunch1t = []
        bunch1EventIdex = [] #FIXME: delete it later
        bunch2x = []
        bunch2y = []
        bunch2l = []
        bunch2t = []
        bunch2EventIdex = []
        bunch3x = []
        bunch3y = []
        bunch3l = []
        bunch3t = []
        bunch3EventIdex = []
        bunch4x = []
        bunch4y = []
        bunch4l = []
        bunch4t = []
        bunch4EventIdex = []
        bunch5x = []
        bunch5y = []
        bunch5l = []
        bunch5t = []
        bunch5EventIdex = []
        bunch6x = []
        bunch6y = []
        bunch6t = []
        bunch6l = []
        bunch6EventIdex = []
        bunch7x = []
        bunch7y = []
        bunch7l = []
        bunch7t = []
        bunch7EventIdex = []
        bunch8x = []
        bunch8y = []
        bunch8l = []
        bunch8t = []
        bunch8EventIdex = []
        
        

        #count the number of large pulse in each individual bunches
        B1num = 0 # number of larger pulse at bunch 1
        B2num = 0
        B3num = 0
        B4num = 0
        B5num = 0
        B6num = 0
        B7num = 0
        B8num = 0

        #count the one hit per layer process in each bunch
        twoHit1 = 0
        twoHit2= 0
        twoHit3= 0
        twoHit4= 0
        twoHit5= 0
        twoHit6= 0
        twoHit7= 0
        twoHit8= 0

        #which channel creates a = 0 data

        B1chan = -10 #channel for first bunch
        B2chan= -10
        B3chan= -10
        B4chan= -10
        B5chan= -10
        B6chan= -10
        B7chan= -10
        B8chan= -10


        #In a given muon bunch how likely we can see the there are large pulse at layer 1 and 2?
        B1l1E = False # large pulse existes at bunch 1 layer 1
        B1l2E = False
        B2l1E = False
        B2l2E = False
        B3l1E = False
        B3l2E = False
        B4l1E = False
        B4l2E = False
        B5l1E = False
        B5l2E = False
        B6l1E = False
        B6l2E = False
        B7l1E = False
        B7l2E = False
        B8l1E = False
        B8l2E = False
        

        sorted_data = sorted(zip(TDCtime,TDCheight,ix,iy,il,TDCwidth,RMSv,area), key=lambda x: x[0])
        for t,h,x,y,l,w,v,a in sorted_data:
            if (t > MuonBunchTime[0] - sig) and (t < MuonBunchTime[0] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #if (t > MuonBunchTime[0] - sig) and (t < MuonBunchTime[0] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch1x.append(x)
                bunch1y.append(y)
                bunch1l.append(l)
                bunch1t.append(t)
                bunch1EventIdex.append(event_id)
                B1num += 1
                if l ==0 :B1l1E = True
                if l ==1 :B1l2E = True
                
            elif (t > MuonBunchTime[1] -sig) and (t < MuonBunchTime[1] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[1] -sig) and (t < MuonBunchTime[1] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch2x.append(x)
                bunch2y.append(y)
                bunch2l.append(l)
                bunch2t.append(t)
                bunch2EventIdex.append(event_id)
                B2num += 1
                if l ==0 :B2l1E = True
                if l ==1 :B2l2E = True

            elif (t > MuonBunchTime[2] -sig) and (t < MuonBunchTime[2] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[2] -sig) and (t < MuonBunchTime[2] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch3x.append(x)
                bunch3y.append(y)
                bunch3l.append(l)
                bunch3t.append(t)
                bunch3EventIdex.append(event_id)
                B3num += 1
                if l ==0 :B3l1E = True
                if l ==1 :B3l2E = True

            elif (t > MuonBunchTime[3] -sig) and (t < MuonBunchTime[3] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[3] -sig) and (t < MuonBunchTime[3] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch4x.append(x)
                bunch4y.append(y)
                bunch4l.append(l)
                bunch4t.append(t)
                bunch4EventIdex.append(event_id)
                B4num += 1
                if l ==0 :B4l1E = True
                if l ==1 :B4l2E = True
            elif (t > MuonBunchTime[4] -sig) and (t < MuonBunchTime[4] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[4] -sig) and (t < MuonBunchTime[4] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch5x.append(x)
                bunch5y.append(y)
                bunch5l.append(l)
                bunch5t.append(t)
                bunch5EventIdex.append(event_id)
                B5num += 1
                if l ==0 :B5l1E = True
                if l ==1 :B5l2E = True
            
            elif (t > MuonBunchTime[5] -sig) and (t < MuonBunchTime[5] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[5] -sig) and (t < MuonBunchTime[5] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch6x.append(x)
                bunch6y.append(y)
                bunch6l.append(l)
                bunch6t.append(t)
                bunch6EventIdex.append(event_id)
                B6num += 1
                if l ==0 :B6l1E = True
                if l ==1 :B6l2E = True
            
            elif (t > MuonBunchTime[6] -sig) and (t < MuonBunchTime[6] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[6] -sig) and (t < MuonBunchTime[6] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch7x.append(x)
                bunch7y.append(y)
                bunch7l.append(l)
                bunch7t.append(t)
                bunch7EventIdex.append(event_id)
                B7num += 1
                if l ==0 :B7l1E = True
                if l ==1 :B7l2E = True

            elif (t > MuonBunchTime[7] -sig) and (t < MuonBunchTime[7] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV):
                #elif (t > MuonBunchTime[7] -sig) and (t < MuonBunchTime[7] + sig) and (h > hegithCut) and (w < widthBound) and (v < TDCrmsabeV) and (a > 150000):
                
                bunch8x.append(x)
                bunch8y.append(y)
                bunch8l.append(l)
                bunch8t.append(t)
                bunch8EventIdex.append(event_id)
                B8num += 1
                if l ==0 :B8l1E = True
                if l ==1 :B8l2E = True

        Dtl1=Dt(bunch1x,bunch1y,bunch1l,bunch1t,bunch1EventIdex)
        Dtl2=Dt(bunch2x,bunch2y,bunch2l,bunch2t,bunch2EventIdex)
        Dtl3=Dt(bunch3x,bunch3y,bunch3l,bunch3t,bunch3EventIdex)
        Dtl4=Dt(bunch4x,bunch4y,bunch4l,bunch4t,bunch4EventIdex)
        Dtl5=Dt(bunch5x,bunch5y,bunch5l,bunch5t,bunch5EventIdex)
        Dtl6=Dt(bunch6x,bunch6y,bunch6l,bunch6t,bunch6EventIdex)
        Dtl7=Dt(bunch7x,bunch7y,bunch7l,bunch7t,bunch7EventIdex)
        Dtl8=Dt(bunch8x,bunch8y,bunch8l,bunch8t,bunch8EventIdex)
        #print(f"Dtl1 {Dtl1}")
        #print(f"Dtl2 {Dtl2}")
        #print(f"Dtl3 {Dtl3}")
        #print(f"Dtl4 {Dtl4}")
        #print(f"Dtl5 {Dtl5}")
        #print(f"Dtl6 {Dtl6}")
        #print(f"Dtl7 {Dtl7}")
        #print(f"Dtl8 {Dtl8}")




        #merged_list = [b1DT + b2Dt + b3Dt  + b4Dt + b5Dt + b6Dt + b7Dt+ b8Dt+ b9Dt + b10Dt for b1DT,b2Dt, b3Dt, b4Dt, b5Dt,b6Dt,b7Dt,b8Dt,b9Dt,b10Dt  in zip(Dtl1, Dtl2, Dtl3, Dtl4, Dtl5, Dtl6, Dtl7, Dtl8)]
        
        dt_lists = [Dtl1, Dtl2, Dtl3, Dtl4, Dtl5, Dtl6, Dtl7, Dtl8]
        merged_list = [
            sum([dt[i] for dt in dt_lists], [])
            for i in range(10)
        ]
        for hist, data in zip(hist_list, merged_list):
            for dt in data:
                hist.Fill(dt)
    file.Close()




        

output_file = r.TFile("DtV4_a0.root", "RECREATE")


for hist in hist_list:
    hist.Write()

print(f"numberOfProcessFile: {numberOfProcessFile}")

#GetEntry()






    






