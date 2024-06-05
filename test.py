"""
check light leak

goal check the entries of each channel for each board and pring them out

check the magnitude


To do:

sort the value based on channel number in each tgraph

adjust the postion of label?

"""

filelocation = "/Users/haoliangzheng/Desktop/SUBMET/0605_30min"

import ROOT
from array import array  
import re


def list_to_dict(lst):
    """Converts a list to a dictionary with indices as values."""
    return {value: index for index, value in enumerate(lst)}



def createTgraph(fileName):

    # Open the ROOT file
    file = ROOT.TFile.Open(f"{filelocation}/board{fileName}.root")



    #variable for making scatter plots without any cut
    Board_CH_values = []
    Entries_values = []


    #value with cut 1: Width > 1 and height > 10 
    Board_CH_values_1 = []
    Entries_values_1 = []
    NumPulse_Cut1_list = [] #list that used to save the number of pulse that pass cut1 in differnet channel



    #height_branch_data = ROOT.std.vector(float)() 




    # Check if the file is opened successfully
    if not file or file.IsZombie():
        print("Error opening file.")
    else:

        keys = file.GetListOfKeys()
        tree_names = []
        # Iterate over the keys and find TTree objects
        for key in keys:
            obj = key.ReadObj()

            keyINChFolder=obj.GetListOfKeys()

            #sub key is channel based information that connected to the same board
            for subKey in keyINChFolder:

                SUBobj = subKey.ReadObj()
                SubName = SUBobj.GetName()
                #print("working here?") #it crash in the following loop
                if SubName.startswith("pul_"):
                    print(SubName) #channel name
                    print(SUBobj.GetEntries()) #entries for the current channel
                    Board_CH_values.append(SubName)
                    Entries_values.append(SUBobj.GetEntries())

                    #cut 1
                    #Get the TBranch object get the branch data
                    

                    #SUBobj.SetBranchAddress("height", height_branch_data)
                

                    #Note: the entries for channel is pulse based. To check pulses in the same 
                    #example output
                    #follow the guide for loading the data https://www.youtube.com/watch?v=0wMbjYrtVk0
                    """
                    Entry 7574 : height 28.38874614594033 : event ID  35283

                    Entry 7575 : height 6.388746145940331 : event ID  35283
                    """



                    NumPulse_Cut1 = 0 # number of pulse in channel X that pass Width > 1 and height > 10 

                    for entry in range(SUBobj.GetEntries()):
                        
                        SUBobj.GetEntry(entry)
                        #print("Entry", entry, ":", "height" , SUBobj.height, ":" , "event ID " , SUBobj.iEve) #for learning only
                        #print(f"size of height data in entry {len(SUBobj.height)}") #error: 'float' has no len() -> meaning each entry have one pulse. This is different from the Milliqan data struture. And entry doesn't associate with Evnent index!
                        
                        
                        #count the number of pulse within specific channel and pass the following requirement Width > 1 and height > 10 
                        #def of cut 1
                        if SUBobj.width > 1 and SUBobj.height > 10:
                            NumPulse_Cut1 += 1
                    
                    NumPulse_Cut1_list.append(NumPulse_Cut1)
                    





                    
        x_mapping = list_to_dict(Board_CH_values)   #convert the channel list into Dict with index {1:Board_CH}
        x_indices = [x_mapping[x] for x in Board_CH_values]



        # Create the TGraph

        
        #print(x_indices)
        #print(Entries_values)
        graph = ROOT.TGraph(len(x_indices), array('d', x_indices), array('d', Entries_values))
        graph.SetTitle(f"board{fileName} Chan vs entries; channel num;Entries")
        canvas = ROOT.TCanvas("canvas", "Scatter Plot", 800, 600)
        graph.Draw("AB")


        # Customize x-axis labels to display original string values
        axis = graph.GetXaxis()
        axis.SetNdivisions(len(x_mapping), False)
        for label, index in x_mapping.items():
            # Use regular expression to extract numeric part
            print(label) #name of the channel tree
            # Use regular expression to extract numeric part
            numeric_part = re.search(r'\d+', label).group()

            # Convert extracted numeric part to an integer
            numeric_value = str(numeric_part)
            axis.ChangeLabel(index + 1, -1, -1, -1, -1, -1, numeric_value)


        # Access the x-axis
        axis = graph.GetXaxis()

        # Adjust label offset and size for x-axis
        axis.SetLabelOffset(0.02)  # Adjust label offset if needed
        axis.SetLabelSize(0.04)    # Adjust label size if needed

        # Rotate labels vertically
        for label in axis.GetLabels():
            label.SetTextAngle(90)



        # Save the canvas as an image
        canvas.SaveAs(f"{filelocation}/board{fileName}_ENtries.png")


        #section for making the Tgraph for Cut1

        graph = ROOT.TGraph(len(x_indices), array('d', x_indices), array('d', NumPulse_Cut1_list))
        graph.SetTitle(f"board{fileName} Chan vs entries; channel num;Entries")
        canvas = ROOT.TCanvas("canvas", "Scatter Plot", 800, 600)
        graph.Draw("AB")


        # Customize x-axis labels to display original string values
        axis = graph.GetXaxis()
        axis.SetNdivisions(len(x_mapping), False)
        for label, index in x_mapping.items():
            # Use regular expression to extract numeric part
            print(label) #name of the channel tree
            # Use regular expression to extract numeric part
            numeric_part = re.search(r'\d+', label).group()

            # Convert extracted numeric part to an integer
            numeric_value = str(numeric_part)
            axis.ChangeLabel(index + 1, -1, -1, -1, -1, -1, numeric_value)


        # Access the x-axis
        axis = graph.GetXaxis()

        # Adjust label offset and size for x-axis
        axis.SetLabelOffset(0.02)  # Adjust label offset if needed
        axis.SetLabelSize(0.04)    # Adjust label size if needed

        # Rotate labels vertically
        for label in axis.GetLabels():
            label.SetTextAngle(90)



        # Save the canvas as an image
        canvas.SaveAs(f"{filelocation}/Cut1_board{fileName}_ENtries.png")


        
        # Close the file
        file.Close()


    



for fileNum in range(10):
    createTgraph(fileNum+1)



#createTgraph(4) #debugf
