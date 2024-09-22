import ROOT as r
import os



#Method for finding Dt
#take the event based data and return Dt
def Dt(heightD,ChanNum,boardNum,TCtimeD):
    
    dummyTime1 = -1
    dummyTime2 = -1
    dummyboard1 = -1
    dummyboard2 = -1
    board1LarPulseNum = 0
    board2LarPulseNum = 0
    #board1Skip = False #dynamic tag for first pulse at board 1. The bunchIndex == 0 did the the job
    board2Skip = False #dynamic tag for first pulse at board 1
    

    Dt = []

    buchIndex = -1

    # Zip the  datasets and sort by the TCtime
    sorted_data = sorted(zip(TCtimeD,heightD,boardNum,ChanNum), key=lambda x: x[0])
    for TCtime,height,board,Chan, in sorted_data:
        if height > 3000:
            buchIndex += 1
            #first pulse for each bunch needs to be a layer 1
            if Chan % 2 != 0:
                board1LarPulseNum += 1
                if buchIndex ==0:
                    dummyTime1 = TCtime
                    dummyboard1 = board
                    Chan1 = Chan
                    #board1Skip=True #might be useless. The bunchIndex == 0 did the the job
                
            
            elif  Chan % 2 == 0:
                board2LarPulseNum += 1
                if buchIndex > 0  and TCtime < (dummyTime1 + 400) and board2Skip == False:  #buchIndex > 0 means layer 1 has hit
                    dummyTime2 = TCtime
                    dummyboard2 = board
                    Chan2 = Chan
                    board2Skip=True


                    
            
            #require less than 6 large pulse within one pulse bunch time interval. (attempt to get clean beam muon event) not sure 6 is good enough
            if TCtime > (dummyTime1 + 400) and (board2LarPulseNum + board1LarPulseNum < 20) and (dummyboard2 == dummyboard1) and buchIndex >= 1 and dummyTime1 > 0:
                print(f"dummyTime2 {dummyTime2}")
                print(f"dummyTime1 {dummyTime1}")
                print(f"board2LarPulseNum {board2LarPulseNum}")
                print(f"board1LarPulseNum {board1LarPulseNum}")
                print(f"Chan1 {Chan1}")
                print(f"Chan2 {Chan2}")
                      
                Dt.append(dummyTime2-dummyTime1)
                #reset data for next muon bunch
                dummyTime1 = -1
                dummyTime2 = -1
                dummyboard1 = -1
                dummyboard2 = -1
                board1LarPulseNum = 0
                board2LarPulseNum = 0
                buchIndex = 0
                board2Skip == False

                #check if the first pulse in the next bunch is associate with layer1
                if Chan % 2 != 0:
                    board1LarPulseNum += 1
                    if buchIndex ==0:
                        dummyTime1 = TCtime
                        dummyboard1 = board
                        Chan1 = Chan




        
    return Dt

#main function
file_names= [f"/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/SubMetflat9_.root"]
#load the file

for file_name in file_names:
    if not os.path.exists(file_name):
        print(f"File not found: {file_name}")
        continue  # Skip to the next file
     
    file = r.TFile.Open(file_name, "READ")
     # Get the tree
    tree = file.Get("t")
    #load the braches
    height = r.std.vector('Double_t')()
    board = r.std.vector('int')()
    chan = r.std.vector('int')()
    TCtime = r.std.vector('Double_t')()
    #evenID = r.std.vector('int')()
    tree.SetBranchAddress("chan", chan)
    tree.SetBranchAddress("height", height)
    tree.SetBranchAddress("board", board)
    tree.SetBranchAddress("TCtime", TCtime)
    #tree.Branch("evenID", evenID) #save for future if debug required

    DtSet = []#Dt for 8 beam muon bunches

    #GetEntries
    TotalEntries=tree.GetEntries()
    

    for index in range(TotalEntries):
        tree.GetEntry(index)

        DtReturn = Dt(height,chan,board,TCtime)
        if DtReturn != []: # empty list means the current event doesn't contain the data that can pass my tag
            DtSet.append(DtReturn)



print(DtSet)


#GetEntry()






    






