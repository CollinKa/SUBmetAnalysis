from ROOT import TF1
import ROOT as r

output_file = r.TFile("pulseT4runRegionfit.root", "RECREATE")
graph = r.TGraphErrors()
graph.SetTitle("gauss means vs run;mean of G peak(is TDC);run number")
graph.SetMarkerStyle(20)  # Circle marker
graph.SetMarkerSize(0.5)
graph.SetMarkerColor(r.kRed)

#runNum = 53
for runNum in range(25,57):
    filelocation = f"/Users/haoliangzheng/subMETData/V3Data/SUBMET/2025MayVer/r000{runNum}_spill.root"
    print(f"processing run {filelocation}")
    lpulseT = r.TH1F("lpulseT{runNum}", "large pulse T Histogram;time;# of pulse", 4000, 0, 4000)

    file = r.TFile.Open(filelocation)
    if not file or file.IsZombie():
        print(f"Failed to open file: {filelocation}")
        continue
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
                #print(f"TDCtime {TDCtime}")

    lpulseT.Draw() #test
    # Define peak centers and fitting windows
    peak_means = [310, 738, 1215, 1745, 2215, 2689, 3171, 3648]  #the guess value of peaks that work for the majority of  cases.

    real_means = [310, 738, 1215, 1745, 2215, 2689, 3171, 3648] #guess values will be overwritten at below
    real_amps = [100]*8 #guess values will be overwritten at below
    #Find the real peak for each bunch

    for index,guessMean in enumerate(peak_means):
        LocalGaussAmp = 5
        for ibin in range(guessMean-200,guessMean+200):
            binVal= lpulseT.GetBinContent(ibin)
            #print(f"binVal {binVal} ")
            if binVal > LocalGaussAmp:
                LocalGaussAmp = binVal
                real_means[index] = ibin + 1
                real_amps[index] = LocalGaussAmp
    #print(f"current run {runNum}")
    #print(f"real_means {real_means}")
    #print(f"real_amps {real_amps}")

    fit_window_half_width = 200  # how wide your fit region is around each peak

    for i, mean in enumerate(peak_means):
        fit_min = mean - fit_window_half_width
        fit_max = mean + fit_window_half_width

        # Define a single Gaussian function for the local fit
        func = TF1(f"gauss_{i}", "[0]*TMath::Gaus(x, [1], [2])", fit_min, fit_max)
        #func.SetParameters(300, mean, 13)  # [amplitude, mean, sigma]
        func.SetParameters(real_amps[i], mean, 13)
        
        # Perform the fit
        lpulseT.Fit(func, "R")  # "R" tells ROOT to respect the function's range

        # Get parameters
        amp = func.GetParameter(0)
        mu = func.GetParameter(1)
        sigma = func.GetParameter(2)
        mu_err = func.GetParError(1)

        #print(f"Peak {i+1}: μ = {mu:.2f} ± {mu_err:.2f}, σ = {sigma:.2f}")
        if amp>0 and sigma > 0:
            graph.SetPoint(i + (runNum-25)*8, mu, runNum)
            graph.SetPointError(i + (runNum-25)*8, sigma, 0.0)
        else:
            print(f"warning run{runNum} the {i} th peak has wrong fitting")
    file.Close()
canvasS = r.TCanvas("c", "Canvas", 800, 600)
graph.Draw("AP")  # "A" for axis, "P" for points
canvasS.Update()
output_file.cd()
graph.Write()
canvasS.Write()
output_file.Close()
