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
        
    # Set a common color range
    min_val = min(h3l1.GetMinimum(), h3l2.GetMinimum())
    max_val = max(h3l1.GetMaximum(), h3l2.GetMaximum())
    h3l1.SetMinimum(min_val)
    h3l1.SetMaximum(max_val)
    h3l2.SetMinimum(min_val)
    h3l2.SetMaximum(max_val)

    # Create a canvas and divide it into two pads
    c1 = r.TCanvas("c1", "Two 3D Histograms with Color Bar", 800, 600)
    c1.Divide(2, 1)
    palette = r.TPaletteAxis(0.92, 0.1, 0.96, 0.9, h3l2)  # Position the color bar
    # Draw the first histogram in pad 1
    c1.cd(1)
    h3l1.Draw("LEGO2Z")  # Use LEGO2 to enable color mapping with color bar

    # Draw the second histogram in pad 2
    c1.cd(2)
    h3l2.Draw("LEGO2Z")  # Use LEGO2 to enable color mapping with color bar

    # Back to the main canvas to draw a global color bar
    c1.cd()
    r.gPad.Update()

    # Add a TPaletteAxis for the second histogram to act as a shared color bar
    
    palette.SetLabelSize(0.02)
    palette.Draw()

    # Update the canvas
    c1.Modified()
    c1.Update()
    output_file = r.TFile("output_canvas.root", "RECREATE")
    c1.Write()
    output_file.Close()



    #r.gApplication.Run()




# Run the function
if __name__ == "__main__":
    fileDit = "/Users/haoliangzheng/subMETData/beamOff/KUmergefile/merged/r00047_event.root"
    eventNo = 5
    example_3D_plot_pyroot(eventNo,fileDit)