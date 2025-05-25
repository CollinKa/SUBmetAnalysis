import ROOT as r
from array import array  
import re
import numpy as np
from ROOT import TF1
import numpy as np


#filelocation = "/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root"
#filelocation = "/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/Merge4runs.root"
filelocation = "/Users/haoliangzheng/subMETData/V3Data/SUBMET/2025MayVer/r00025_spill.root"
lpulseT = r.TH1F("lpulseT", "large pulse T Histogram;time;# of pulse", 4000, 0, 4000)

file = r.TFile.Open(filelocation)
tree = file.Get("tree")
h = r.std.vector('Double_t')() #height
t = r.std.vector('Double_t')()
width = r.std.vector('Double_t')()

RMSv = r.std.vector('Double_t')()
tree.SetBranchAddress("pulse_volt_height", h)
tree.SetBranchAddress("pulse_time_is", t)
tree.SetBranchAddress("event_volt_rms_abe", RMSv)
tree.SetBranchAddress("pulse_time_fwhm", width)

TotalEntries=tree.GetEntries()

for index in range(TotalEntries):
    tree.GetEntry(index)

    for TDCtime,TDCheihgt,TDCrmsabeV,TDCwidth in zip(t,h,RMSv,width):
        if TDCheihgt>3000 and TDCwidth< 100 and TDCrmsabeV < 2:
            lpulseT.Fill(TDCtime)

def sum_of_two_gaussians(x, params):
    gauss1 = params[0] * r.TMath.Gaus(x[0], params[1], params[2]) # params[0]: Amplitude (normalization) for the first Gaussian.   params[1]: Mean of the first Gaussian.    params[2]: Sigma (standard deviation) of the first Gaussian
    gauss2 = params[3] * r.TMath.Gaus(x[0], params[4], params[5])
    gauss3 = params[6] * r.TMath.Gaus(x[0], params[7], params[8])
    gauss4 = params[9] * r.TMath.Gaus(x[0], params[10], params[11])
    gauss5 = params[12] * r.TMath.Gaus(x[0], params[13], params[14])
    gauss6 = params[15] * r.TMath.Gaus(x[0], params[16], params[17])
    gauss7 = params[18] * r.TMath.Gaus(x[0], params[19], params[20])
    gauss8 = params[21] * r.TMath.Gaus(x[0], params[22], params[23])
    return gauss1 + gauss2 + gauss3 + gauss4 + gauss5 + gauss6 + gauss7 + gauss8

    #2nd fitting function(yeild the same result like above)
    #gauss = params[0] * r.TMath.Gaus(x[0], params[1], params[2]) + params[3] * r.TMath.Gaus(x[0], params[4], params[5]) + params[6] * r.TMath.Gaus(x[0], params[7], params[8]) + params[9] * r.TMath.Gaus(x[0], params[10], params[11]) + params[12] * r.TMath.Gaus(x[0], params[13], params[14]) + params[15] * r.TMath.Gaus(x[0], params[16], params[17]) + params[18] * r.TMath.Gaus(x[0], params[19], params[20]) + params[21] * r.TMath.Gaus(x[0], params[22], params[23])
    #return gauss


fit_func = TF1("fit_func", sum_of_two_gaussians, 100, 4000, 24) #fitting range, number fitting parameters



#guess the mean and sigma for gaussian distribution
sigma =13
mean1 = 310
sigma1 = sigma
mean2 = 738
sigma2 = sigma
mean3 = 1215
sigma3 = sigma
mean4 = 1745
sigma4 = sigma
mean5 = 2215
sigma5 = sigma
mean6 = 2689
sigma6 = sigma
mean7 = 3171
sigma7 = sigma
mean8 = 3648
sigma8 = sigma


#fit_func.SetParameters([100, mean1, sigma1, 100, mean2, sigma2,100,mean3, sigma3,100,mean4, sigma4,100,mean5, sigma5,100,mean6, sigma6,100,mean7, sigma7,100,mean8, sigma8])
amplitude = 350
params = [amplitude, mean1, sigma1, amplitude, mean2, sigma2, amplitude, mean3, sigma3, 
          amplitude, mean4, sigma4, amplitude, mean5, sigma5, amplitude, mean6, sigma6, 
          amplitude, mean7, sigma7, amplitude, mean8, sigma8]


# Convert the list to a numpy array of type double
params_array = np.array(params, dtype='double')

# Set the parameters using the numpy array
fit_func.SetParameters(params_array)


r.gROOT.SetBatch(False)  # This ensures that ROOT is in interactive mode
canvas = r.TCanvas("canvas", "Canvas", 800, 600)




file.Close()
lpulseT.Fit(fit_func)
lpulseT.Draw("pe")

canvas.Update()
canvas.Draw()
canvas.SaveAs("gaussfit4runs.png")


output_file = r.TFile("pulseT4runs.root", "RECREATE")
lpulseT.Write()
canvas.Write()
output_file.Close()

# Loop over all parameters and print them
for i in range(fit_func.GetNpar()):
    Di = i // 3 #index of the i th gaussion distribution
    a = i - Di*3 #used to determine if number is associate with amplitude or sigma or mean.

    if a == 2: print(f"distribution {Di} sigma: {fit_func.GetParameter(i)}")
    elif a == 1: print(f"distribution {Di} mean: {fit_func.GetParameter(i)}")
    elif a == 0: print(f"distribution {Di} amplitude: {fit_func.GetParameter(i)}")   
    