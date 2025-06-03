import ROOT as r
from array import array  
import re
import numpy as np
from ROOT import TF1
import numpy as np



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




#filelocation = "/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/r00020_event.root"
#filelocation = "/Users/haoliangzheng/Desktop/SUBMET/analysisScript/SUBmetAnalysis/Merge4runs.root"
output_file = r.TFile("pulseT4runV2fit.root", "RECREATE")

# Create an empty TGraph
graph = r.TGraphErrors()

graph.SetTitle("gauss means vs run;mean of G peak(is TDC);run number")
graph.SetMarkerStyle(20)  # Circle marker
graph.SetMarkerSize(1.0)
graph.SetMarkerColor(r.kRed)


for runNum in range(25, 57):
    filelocation = f"/Users/haoliangzheng/subMETData/V3Data/SUBMET/2025MayVer/r000{runNum}_spill.root"
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

    for i in range(0, 24, 3):  # amplitude indices
        fit_func.SetParLimits(i, 0, 1e6)  # amplitude >= 0
    
    # Set parameter limits: constrain each Gaussian to stay near its initial guess
    means = [310, 738, 1215, 1745, 2215, 2689, 3171, 3648]
    sigmas = [13] * 8

    for i in range(8):
        amp_idx = i * 3      # Amplitude
        mean_idx = amp_idx + 1  # Mean
        sigma_idx = amp_idx + 2  # Sigma

        # Set amplitude >= 0
        fit_func.SetParLimits(amp_idx, 0, 1e6)

        # Mean must stay within ±25 of your guess
        fit_func.SetParLimits(mean_idx, means[i] - 25, means[i] + 25)

        # Sigma must stay within reasonable range
        fit_func.SetParLimits(sigma_idx, 5, 30)


    file.Close()
    lpulseT.Fit(fit_func)
    lpulseT.Draw("pe")

    canvas.Update()
    canvas.Draw()
    canvas.SaveAs("gaussfit4runs.png")



    lpulseT.Write()
    canvas.Write()


    # Loop over all parameters and print them
    point_index = 0  # Use separate index for graph points
    for i in range(fit_func.GetNpar()):
        Di = i // 3  # Index of the ith Gaussian
        a = i % 3     # 0: amplitude, 1: mean, 2: sigma

        if a == 2:
            print(f"distribution {Di} sigma: {fit_func.GetParameter(i)}")
            
        elif a == 1:
            mean_val = fit_func.GetParameter(i)
            print(f"distribution {Di} mean: {mean_val}")
            graph.SetPoint(point_index + (runNum-25)*8, mean_val, runNum)
            graph.SetPointError(point_index, fit_func.GetParError(i), 0.0)
            
            point_index += 1
        elif a == 0:
            print(f"distribution {Di} amplitude: {fit_func.GetParameter(i)}")


canvasS = r.TCanvas("c", "Canvas", 800, 600)
graph.Draw("AP")  # "A" for axis, "P" for points
canvasS.Update()
output_file.cd()
graph.Write()
canvasS.Write()
output_file.Close()