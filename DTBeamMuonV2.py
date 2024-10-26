"""
Notes
V1 9.22
issue: 
1.The program can only yell a little amount of data for DT. -> Need to introduce the Column, row layer
2.Instead of counting the number of pulse at two layer. I should use the number of unique channel. -> need to create new channel number that is unique for each channel(finished)


10.22
add the trigger time mean and sigma value in Dt()


"""




import ROOT as r
import os



#Method for finding Dt for data within a single muon bunch
def Dt(x,y,l,t,a = 1):
    data=zip(x,y,l,t)
    tl1 = 5000
    tl2 = 6000
    xl1 = -100
    xl2 = -200
    yl1 = -100
    yl2 = -200

    if len(x) < 2 : return -100  #To find Dt we need at least two large pulses in the beam muon bunch.
    
    #find the first pulse at each layer
    for x,y,l,t in data:
        if l == 1:
            if t < tl1:
                tl1 = t
                xl1 = x
                yl1 = y
                            
        if l == 2:
            if t < tl2:
                tl2 = t
                xl2 = x
                yl2 = y                 

    Da = ((xl1 - xl2)** 2)  +  ((yl1 - yl2)**2) 
    if Da <= a:        
        return tl2 - tl1
    else: return -100 
    
#----------------------------------------------------------------------------------
#main function
file_names= ["/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root"]

#data collection window
hegithCut = 2500
sig = 13 #standard deviation
MuonBunchTime = [310,785,1261,1741,2215,2694,3170,3645] # mean of 8 different muon bunches

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

    #load the braches
    height = r.std.vector('double')()
    time = r.std.vector('double')()
    ix = r.std.vector('int')()
    iy = r.std.vector('int')()
    il = r.std.vector('int')()

    tree.SetBranchAddress("h", height)
    tree.SetBranchAddress("t", time)
    tree.SetBranchAddress("ix", ix)
    tree.SetBranchAddress("iy", iy)
    tree.SetBranchAddress("il", il)


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
        

        sorted_data = sorted(zip(time,height,ix,iy,il), key=lambda x: x[0])
        for t,h,x,y,l in sorted_data:
            if (t > MuonBunchTime[0] - sig) and (t < MuonBunchTime[0] + sig) and h > hegithCut :
                
                bunch1x.append(x)
                bunch1y.append(y)
                bunch1l.append(l)
                bunch1t.append(t)
                B1num += 1
                if l ==1 :B1l1E = True
                if l ==2 :B1l2E = True
                

            elif (t > MuonBunchTime[1] -sig) and (t < MuonBunchTime[1] + sig) and h > hegithCut :
                
                bunch2x.append(x)
                bunch2y.append(y)
                bunch2l.append(l)
                bunch2t.append(t)
                B2num += 1
                if l ==1 :B2l1E = True
                if l ==2 :B2l2E = True
            
            elif (t > MuonBunchTime[2] -sig) and (t < MuonBunchTime[2] + sig) and h > hegithCut :
                
                bunch3x.append(x)
                bunch3y.append(y)
                bunch3l.append(l)
                bunch3t.append(t)
                B3num += 1
                if l ==1 :B3l1E = True
                if l ==2 :B3l2E = True
            
            elif (t > MuonBunchTime[3] -sig) and (t < MuonBunchTime[3] + sig) and h > hegithCut :
                
                bunch4x.append(x)
                bunch4y.append(y)
                bunch4l.append(l)
                bunch4t.append(t)
                B4num += 1
                if l ==1 :B4l1E = True
                if l ==2 :B4l2E = True
            
            elif (t > MuonBunchTime[4] -sig) and (t < MuonBunchTime[4] + sig) and h > hegithCut :
                
                bunch5x.append(x)
                bunch5y.append(y)
                bunch5l.append(l)
                bunch5t.append(t)
                B5num += 1
                if l ==1 :B5l1E = True
                if l ==2 :B5l2E = True
            
            elif (t > MuonBunchTime[5] -sig) and (t < MuonBunchTime[5] + sig) and h > hegithCut :
                
                bunch6x.append(x)
                bunch6y.append(y)
                bunch6l.append(l)
                bunch6t.append(t)
                B6num += 1
                if l ==1 :B6l1E = True
                if l ==2 :B6l2E = True
            
            elif (t > MuonBunchTime[6] -sig) and (t < MuonBunchTime[6] + sig) and h > hegithCut :
                
                bunch7x.append(x)
                bunch7y.append(y)
                bunch7l.append(l)
                bunch7t.append(t)
                B7num += 1
                if l ==1 :B7l1E = True
                if l ==2 :B7l2E = True


            elif (t > MuonBunchTime[7] -sig) and (t < MuonBunchTime[7] + sig) and h > hegithCut :
                
                bunch8x.append(x)
                bunch8y.append(y)
                bunch8l.append(l)
                bunch8t.append(t)
                B8num += 1
                if l ==1 :B8l1E = True
                if l ==2 :B8l2E = True

        Dtl1=Dt(bunch1x,bunch1y,bunch1l,bunch1t)
        Dtl2=Dt(bunch2x,bunch2y,bunch2l,bunch2t)
        Dtl3=Dt(bunch3x,bunch3y,bunch3l,bunch3t)
        Dtl4=Dt(bunch4x,bunch4y,bunch4l,bunch4t)
        Dtl5=Dt(bunch5x,bunch5y,bunch5l,bunch5t)
        Dtl6=Dt(bunch6x,bunch6y,bunch6l,bunch6t)
        Dtl7=Dt(bunch7x,bunch7y,bunch7l,bunch7t)
        Dtl8=Dt(bunch8x,bunch8y,bunch8l,bunch8t)
        DtSet.append(Dtl1)
        DtSet.append(Dtl2)
        DtSet.append(Dtl3)
        DtSet.append(Dtl4)
        DtSet.append(Dtl5)
        DtSet.append(Dtl6)
        DtSet.append(Dtl7)
        DtSet.append(Dtl8)
        nhits.Fill(B8num+B7num+B6num + B5num + B4num + B3num + B2num + B1num)

        if B1l1E & B1l2E: twolayers += 1
        if B2l1E & B2l2E: twolayers += 1
        if B3l1E & B3l2E: twolayers += 1
        if B4l1E & B4l2E: twolayers += 1
        if B5l1E & B5l2E: twolayers += 1
        if B6l1E & B6l2E: twolayers += 1
        if B7l1E & B7l2E: twolayers += 1
        if B8l1E & B8l2E: twolayers += 1
        

print(f"twolayers: {twolayers}")  

print(len(DtSet)) 

for t in DtSet:
    if t is not None:
        histogram.Fill(t)

histogram.Draw()
c1.Update()
c1.Draw()
c1.SaveAs("1d_histogram.png")
output_file = r.TFile("DtV2.root", "RECREATE")
histogram.Write()
nhits.Write()


#GetEntry()






    






