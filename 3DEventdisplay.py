import ROOT as r
import os
import numpy as np
import array

def example_3D_plot_pyroot(eventNo,filelocation):
    file = r.TFile.Open(filelocation, "READ")
    tree = file.Get("tree")
    height = r.std.vector('double')()
    time = r.std.vector('double')()
    area = r.std.vector('double')()
    ix = r.std.vector('int')()
    iy = r.std.vector('int')()
    il = r.std.vector('int')()
    evt = array.array('I', [0])

    tree.SetBranchAddress("h", height)
    tree.SetBranchAddress("t", time)
    tree.SetBranchAddress("ix", ix)
    tree.SetBranchAddress("iy", iy)
    tree.SetBranchAddress("il", il)
    tree.SetBranchAddress("a", area)
    tree.SetBranchAddress("evt", evt)

    # Initialize a 3D histogram
    h3l1 = r.TH3D("h3l1", "Layer 1", 4915, -0.6, 4914.6, 10, -0.5, 9.5, 8, -0.5, 7.5);
    h3l2 = r.TH3D("h3l2", "Layer 2", 4915, -0.6, 4914.6, 10, -0.5, 9.5, 8, -0.5, 7.5);

    tree.GetEntry(eventNo)

    data = zip(time,height,ix,iy,il,area)
    for t,h,x,y,l,a in data:
        if l == 2: h3l2.Fill(t, x, y,a)
        elif l == 1: h3l1.Fill(t, x, y,a)
        

    # Create a canvas
    c1 = r.TCanvas("c1", "3D Histogram Example", 800, 600)
    c1.Divide(2, 1)
    
    # Draw the histogram with the BOX option
    c1.cd(1)     
    h3l2.Draw("BOX2")  # Options: "BOX2", "LEGO2", "SURF2"

    c1.cd(2)     
    # Draw the histogram with the BOX option
    h3l1.Draw("BOX2")  # Options: "BOX2", "LEGO2", "SURF2"

    c1.Update()

    # Keep the GUI window open
    #input("Press Enter to exit...")

    r.gApplication.Run()

    #c2 = r.TCanvas("c2", "3D Histogram Example", 800, 600)
    #h3l1.Draw("BOX2")



# Run the function
if __name__ == "__main__":
    fileDit = "/Users/haoliangzheng/subMETData/beamOff/KUmergefile/merged/r00020_event.root"
    eventNo = 5
    example_3D_plot_pyroot(eventNo,fileDit)
