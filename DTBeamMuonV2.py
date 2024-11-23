"""
Notes
V1 9.22
issue: 
1.The program can only yell a little amount of data for DT. -> Need to introduce the Column, row layer
2.Instead of counting the number of pulse at two layer. I should use the number of unique channel. -> need to create new channel number that is unique for each channel(finished)


10.22
add the trigger time mean and sigma value in Dt()


11-19 
prepare to make Dt / channel data to do the fit
issue: the the default file doesn't come with channel number.
need to create channel number for each channel then procee


11-23
create channel number with ix(0-9) iy(0-7). Chan number = ix + iy*10

"""




import ROOT as r
import os
import numpy as np



#Method for finding Dt for data within a single muon bunch
def Dt(x,y,l,t,a = 0,cosmicVeto=False):
    data=zip(x,y,l,t)
    tl1 = 5000
    tl2 = 6000
    xl1 = -100
    xl2 = -200
    yl1 = -100
    yl2 = -200
    l1Hit = 0
    l2Hit = 0
    chanNo = -10

    if len(x) < 2: return [-100,0,-10]  #To find Dt we need at least two large pulses in the beam muon bunch. The second 0 means in the curent bunch there is no one hit per layer process
    if cosmicVeto:
        if (0 in x) or (9 in x) or (7 in y): return -100 
    
    #find the first pulse at each layer
    for x,y,l,t in data:
        if l == 1:
            l1Hit = 1
            if t < tl1:
                tl1 = t
                xl1 = x
                yl1 = y
                            
        if l == 2:
            l2Hit = 1
            if t < tl2:
                tl2 = t
                xl2 = x
                yl2 = y                 

    Da = ((xl1 - xl2)** 2)  +  ((yl1 - yl2)**2) 
    if Da ==0:
        chanNo = xl1 + yl1 * 10
    #if Da <= 5 and Da >= 2:
    if Da <= a:
        return [tl2 - tl1,l1Hit*l2Hit,chanNo]
    else: return [-100,0,-10]
    
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





file_names= ["/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00047_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00048_event.root","/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00049_event.root"]

#data collection window
hegithCut = 2500
areaCut = 0  #lower bound (as if doesn't exist)
#areaCut = 150000
#areaUpBound = 230000
areaUpBound = 23000000000 #upper bound (as if doesn't exist)

sig = 13 #standard deviation
MuonBunchTime = [310,785,1261,1741,2215,2694,3170,3645] # mean of 8 different muon bunches
BunchNumber = 0
Num1hitPL = 0 # count the number of one hit per layer process (at most 1 process per bunch)
numberOfProcessFile = 0

Dt_Chans = [[] for _ in range(80)]# Create 80 empty lists to save the Dt value for each channels

#histograms
r.gROOT.SetBatch(False)
c1 = r.TCanvas("c1", "c1", 800, 600)
histogram = r.TH1F("histogram", "Dt Histogram;Dt;number of pulse pair ", 60, -30, 30)
nhits = r.TH1F("nhits", f"nhits height > {hegithCut} & sigma {sig};num of pulse;number of event ", 30, 0, 30)



DtSet = []#Dt data from 8 beam muon bunches
twolayers = 0 #Count the number of data pairs that can be used to find Dt

for file_name in file_names:
    if not os.path.exists(file_name):
        print(f"File not found: {file_name}")
        continue  # Skip to the next file
     
    file = r.TFile.Open(file_name, "READ")
    # Get the tree
    tree = file.Get("tree")
    if not tree or not isinstance(tree, r.TTree):
        continue

    #load the braches
    height = r.std.vector('double')()
    time = r.std.vector('double')()
    area = r.std.vector('double')()
    ix = r.std.vector('int')()
    iy = r.std.vector('int')()
    il = r.std.vector('int')()

    tree.SetBranchAddress("h", height)
    tree.SetBranchAddress("t", time)
    tree.SetBranchAddress("ix", ix)
    tree.SetBranchAddress("iy", iy)
    tree.SetBranchAddress("il", il)
    tree.SetBranchAddress("a", area)

    numberOfProcessFile += 1
    


    #GetEntries
    TotalEntries=tree.GetEntries()
    

    for index in range(TotalEntries):
        tree.GetEntry(index)
        #collect location index and pulse time for data in 8 different bunches
        bunch1x = []
        bunch1y = []
        bunch1l = []
        bunch1t = []
        bunch2x = []
        bunch2y = []
        bunch2l = []
        bunch2t = []
        bunch3x = []
        bunch3y = []
        bunch3l = []
        bunch3t = []
        bunch4x = []
        bunch4y = []
        bunch4l = []
        bunch4t = []
        bunch5x = []
        bunch5y = []
        bunch5l = []
        bunch5t = []
        bunch6x = []
        bunch6y = []
        bunch6t = []
        bunch6l = []
        bunch7x = []
        bunch7y = []
        bunch7l = []
        bunch7t = []
        bunch8x = []
        bunch8y = []
        bunch8l = []
        bunch8t = []
        
        

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
        

        sorted_data = sorted(zip(time,height,ix,iy,il,area), key=lambda x: x[0])
        for t,h,x,y,l,a in sorted_data:
            if (t > MuonBunchTime[0] - sig) and (t < MuonBunchTime[0] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch1x.append(x)
                bunch1y.append(y)
                bunch1l.append(l)
                bunch1t.append(t)
                B1num += 1
                if l ==1 :B1l1E = True
                if l ==2 :B1l2E = True
                

            elif (t > MuonBunchTime[1] -sig) and (t < MuonBunchTime[1] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch2x.append(x)
                bunch2y.append(y)
                bunch2l.append(l)
                bunch2t.append(t)
                B2num += 1
                if l ==1 :B2l1E = True
                if l ==2 :B2l2E = True
            
            elif (t > MuonBunchTime[2] -sig) and (t < MuonBunchTime[2] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch3x.append(x)
                bunch3y.append(y)
                bunch3l.append(l)
                bunch3t.append(t)
                B3num += 1
                if l ==1 :B3l1E = True
                if l ==2 :B3l2E = True
            
            elif (t > MuonBunchTime[3] -sig) and (t < MuonBunchTime[3] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch4x.append(x)
                bunch4y.append(y)
                bunch4l.append(l)
                bunch4t.append(t)
                B4num += 1
                if l ==1 :B4l1E = True
                if l ==2 :B4l2E = True
            
            elif (t > MuonBunchTime[4] -sig) and (t < MuonBunchTime[4] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch5x.append(x)
                bunch5y.append(y)
                bunch5l.append(l)
                bunch5t.append(t)
                B5num += 1
                if l ==1 :B5l1E = True
                if l ==2 :B5l2E = True
            
            elif (t > MuonBunchTime[5] -sig) and (t < MuonBunchTime[5] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch6x.append(x)
                bunch6y.append(y)
                bunch6l.append(l)
                bunch6t.append(t)
                B6num += 1
                if l ==1 :B6l1E = True
                if l ==2 :B6l2E = True
            
            elif (t > MuonBunchTime[6] -sig) and (t < MuonBunchTime[6] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch7x.append(x)
                bunch7y.append(y)
                bunch7l.append(l)
                bunch7t.append(t)
                B7num += 1
                if l ==1 :B7l1E = True
                if l ==2 :B7l2E = True


            elif (t > MuonBunchTime[7] -sig) and (t < MuonBunchTime[7] + sig) and h > hegithCut and a > areaCut and a < areaUpBound:
                
                bunch8x.append(x)
                bunch8y.append(y)
                bunch8l.append(l)
                bunch8t.append(t)
                B8num += 1
                if l ==1 :B8l1E = True
                if l ==2 :B8l2E = True

        Dtl1,twoHit1,B1chan=Dt(bunch1x,bunch1y,bunch1l,bunch1t)
        Dtl2,twoHit2,B2chan=Dt(bunch2x,bunch2y,bunch2l,bunch2t)
        Dtl3,twoHit3,B3chan=Dt(bunch3x,bunch3y,bunch3l,bunch3t)
        Dtl4,twoHit4,B4chan=Dt(bunch4x,bunch4y,bunch4l,bunch4t)
        Dtl5,twoHit5,B5chan=Dt(bunch5x,bunch5y,bunch5l,bunch5t)
        Dtl6,twoHit6,B6chan=Dt(bunch6x,bunch6y,bunch6l,bunch6t)
        Dtl7,twoHit7,B7chan=Dt(bunch7x,bunch7y,bunch7l,bunch7t)
        Dtl8,twoHit8,B8chan=Dt(bunch8x,bunch8y,bunch8l,bunch8t)

        if (B1chan>=0): Dt_Chans[B1chan].append(Dtl1)
        if (B2chan>=0): Dt_Chans[B2chan].append(Dtl2)
        if (B3chan>=0): Dt_Chans[B3chan].append(Dtl3)
        if (B4chan>=0): Dt_Chans[B4chan].append(Dtl4)
        if (B5chan>=0): Dt_Chans[B5chan].append(Dtl5)
        if (B6chan>=0): Dt_Chans[B6chan].append(Dtl6)
        if (B7chan>=0): Dt_Chans[B7chan].append(Dtl7)
        if (B8chan>=0): Dt_Chans[B8chan].append(Dtl8)


        Num1hitPL += twoHit1
        Num1hitPL += twoHit2
        Num1hitPL += twoHit3
        Num1hitPL += twoHit4
        Num1hitPL += twoHit5
        Num1hitPL += twoHit6
        Num1hitPL += twoHit7
        Num1hitPL += twoHit8
        
        DtSet.append(Dtl1)
        DtSet.append(Dtl2)
        DtSet.append(Dtl3)
        DtSet.append(Dtl4)
        DtSet.append(Dtl5)
        DtSet.append(Dtl6)
        DtSet.append(Dtl7)
        DtSet.append(Dtl8)
        nhits.Fill(B8num+B7num+B6num + B5num + B4num + B3num + B2num + B1num)
        #count the number of bunch in the event
        if len(bunch1x) > 0: BunchNumber +=1
        if len(bunch2x) > 0: BunchNumber +=1
        if len(bunch3x) > 0: BunchNumber +=1
        if len(bunch4x) > 0: BunchNumber +=1
        if len(bunch5x) > 0: BunchNumber +=1
        if len(bunch6x) > 0: BunchNumber +=1
        if len(bunch7x) > 0: BunchNumber +=1
        if len(bunch8x) > 0: BunchNumber +=1


        if B1l1E & B1l2E: twolayers += 1
        if B2l1E & B2l2E: twolayers += 1
        if B3l1E & B3l2E: twolayers += 1
        if B4l1E & B4l2E: twolayers += 1
        if B5l1E & B5l2E: twolayers += 1
        if B6l1E & B6l2E: twolayers += 1
        if B7l1E & B7l2E: twolayers += 1
        if B8l1E & B8l2E: twolayers += 1
        

print(f"twolayers: {twolayers}")  
print(f"Number of bunches: {BunchNumber}")
print(f"Number of 1 hit per layer process: {Num1hitPL}")


print(len(DtSet)) 


#find the mean for each channel
MeanDtChanNo = r.TGraph(80)
for ChanNo, DtSetData in enumerate(Dt_Chans):
    if len(DtSetData) >0 : 
        mean = np.mean(DtSetData)
        
        MeanDtChanNo.SetPoint(ChanNo,ChanNo, mean) 
MeanDtChanNo.SetTitle("Chan & Dt mean;channel no;Dt(sample time) mean")
MeanDtChanNo.SetMarkerStyle(21)  # Solid square
MeanDtChanNo.SetMarkerSize(1.2)  # Marker size
MeanDtChanNo.SetMarkerColor(r.kRed)  # Marker color

for t in DtSet:
    if abs(t) < 2*sig: #from Dt() function, only the result that is less than abs(t) < 2*sig means 2 layer hit exist.
        histogram.Fill(t)

histogram.Draw()
c1.Update()
c1.Draw()
c1.SaveAs("1d_histogram.png")
output_file = r.TFile("DtV2_a164.root", "RECREATE")
histogram.Write()
nhits.Write()
canvas = r.TCanvas("canvas1", "My First Canvas", 800, 600)
MeanDtChanNo.Draw("AP")
canvas.Write()
print(f"numberOfProcessFile: {numberOfProcessFile}")

#GetEntry()






    






