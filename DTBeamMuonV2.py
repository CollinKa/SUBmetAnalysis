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



#Method for finding Dt
#take the event based data and return Dt

def Dt(x,y,l,t,a = 2):
    data=zip(x,y,l,t)
    tl1 = -100
    tl2 = -200
    xl1 = -100
    xl2 = -200
    yl1 = -100
    yl2 = -200
    ll1 = -100
    ll2 = -200
    print(len(x))
    if len(x) != 2: return -100
    
    for t,x,y,l in data:
        if l == 1:
            tl1 = t
            xl1 = x
            yl1 = y
            ll1 = l

            
        if l == 2:
            tl2 = t
            xl2 = x
            yl2 = y
            ll2 = l

    Da = ((xl1 - xl2)** 2)  +  ((yl1 - yl2)**2) + ((ll1 - ll2)**2)

    if Da <= a:
        return tl2 - tl1
    

#main function
file_names= ["/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root"]
#load the file
DtSet = []#Dt for 8 beam muon bunches

MuonBunchTime = [310,785,1261,1741,2215,2694,3170,3645]

for file_name in file_names:
    if not os.path.exists(file_name):
        print(f"File not found: {file_name}")
        continue  # Skip to the next file
     
    file = r.TFile.Open(file_name, "READ")
    # Get the tree
    tree = file.Get("tree")

    #load the braches
    height = r.std.vector('double')()
    chan = r.std.vector('int')()
    time = r.std.vector('double')()
    ix = r.std.vector('double')()
    iy = r.std.vector('int')()
    il = r.std.vector('double')()

    tree.SetBranchAddress("h", height)
    tree.SetBranchAddress("t", time)
    tree.SetBranchAddress("ix", ix)
    tree.SetBranchAddress("iy", iy)
    tree.SetBranchAddress("il", il)
    #tree.Branch("evenID", evenID) #save for future if debug required

    

    #GetEntries
    TotalEntries=tree.GetEntries()
    

    for index in range(TotalEntries):
        tree.GetEntry(index)
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
        hegithCut = 2500
        sorted_data = sorted(zip(time,height,ix,iy,il), key=lambda x: x[0])
        for t,h,x,y,l in sorted_data:
            if (t > MuonBunchTime[0] -13) and (t < MuonBunchTime[0] + 13) and h > hegithCut :
                
                bunch1x.append(x)
                bunch1y.append(y)
                bunch1l.append(l)
                bunch1t.append(t)
            elif (t > MuonBunchTime[1] -13) and (t < MuonBunchTime[1] + 13) and h > hegithCut :
                
                bunch2x.append(x)
                bunch2y.append(y)
                bunch2l.append(l)
                bunch2t.append(t)
            
            elif (t > MuonBunchTime[2] -13) and (t < MuonBunchTime[2] + 13) and h > hegithCut :
                
                bunch3x.append(x)
                bunch3y.append(y)
                bunch3l.append(l)
                bunch3t.append(t)
            
            elif (t > MuonBunchTime[3] -13) and (t < MuonBunchTime[3] + 13) and h > hegithCut :
                
                bunch4x.append(x)
                bunch4y.append(y)
                bunch4l.append(l)
                bunch4t.append(t)
            
            elif (t > MuonBunchTime[4] -13) and (t < MuonBunchTime[4] + 13) and h > hegithCut :
                
                bunch5x.append(x)
                bunch5y.append(y)
                bunch5l.append(l)
                bunch5t.append(t)
            
            elif (t > MuonBunchTime[5] -13) and (t < MuonBunchTime[5] + 13) and h > hegithCut :
                
                bunch6x.append(x)
                bunch6y.append(y)
                bunch6l.append(l)
                bunch6t.append(t)
            
            elif (t > MuonBunchTime[6] -13) and (t < MuonBunchTime[6] + 13) and h > hegithCut :
                
                bunch7x.append(x)
                bunch7y.append(y)
                bunch7l.append(l)
                bunch7t.append(t)


            elif (t > MuonBunchTime[7] -13) and (t < MuonBunchTime[7] + 13) and h > hegithCut :
                
                bunch8x.append(x)
                bunch8y.append(y)
                bunch8l.append(l)
                bunch8t.append(t)

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

#print(DtSet)

#print(DtSet)
r.gROOT.SetBatch(False)
c1 = r.TCanvas("c1", "c1", 800, 600)
histogram = r.TH1F("histogram", "Dt Histogram;Dt;number of pulse pair ", 60, -30, 30)
for t in DtSet:
    if t is not None:
        histogram.Fill(t)

histogram.Draw()
c1.Update()
c1.Draw()
c1.SaveAs("1d_histogram.png")


#GetEntry()






    






