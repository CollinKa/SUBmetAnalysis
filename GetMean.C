#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>


//TCanvas* c1 = new TCanvas("c1", "c1", 0, 400, 600, 300);


// Vector to store histogram pointers
//std::vector<TH1F*> B1CH1_histograms;
// Vector to store the points
std::vector<std::pair<double, double>> points;   // data from CH0
std::vector<std::pair<double, double>> Ch1Data; 


//deal with this later
/*
double GetMeanValue(TFile* f_in, TTree* tree , int ChanNum){
    f_in->GetObject(Form("ch%i/ped_ch%i",ChanNum,ChanNum), tree);
    TH1F* ch0_h = new TH1F(Form("ch%i_h", ChanNum), "ABEmean", 500, 0, 5000);
    tree->Draw("ABEmean>>Form("ch%i_h", ChanNum)"); // I doubt if this can work
}
*/



void GetMeanF(int runNum = 1){
    TFile* f_in;
    std::cout << Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum) << std::endl;
    if (runNum < 10) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum));}
    else if (runNum >= 13 ) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000%i/r000%i_board1.root", runNum,runNum));}    
    else {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000%i/board1.root", runNum));}
    //f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum));
    TTree* tree0 = new TTree;
    f_in->GetObject("ch0/ped_ch0", tree0);
    
    TH1F* ch0_h = new TH1F("ch0_h", "ABEmean", 500, 0, 5000);
    tree0->Draw("ABEmean>>ch0_h");
    float mean_value = ch0_h->GetMean();
    std::cout << mean_value << std::endl;

    //B1CH1_histograms.push_back(ch0_h);
    points.push_back(std::make_pair(runNum, mean_value));



    //loading the data from Ch1
    f_in->GetObject("ch1/ped_ch1", tree0);
    
    TH1F* ch1_h = new TH1F("ch1_h", "ABEmean", 500, 0, 5000);
    tree0->Draw("ABEmean>>ch1_h");
    float mean_value = ch0_h->GetMean();
    std::cout << mean_value << std::endl;

    //B1CH1_histograms.push_back(ch0_h);
    points.push_back(std::make_pair(runNum, mean_value));




    

}



//run 16 & 4 DNE
//for the run name run 13 - lastest run the file name follows the naming convention like _board6.root

void GetMean(){

    for (int runNum = 1; runNum < 32 ; runNum++)
    {
        if (runNum == 4 || runNum == 16 ) {continue;}

        GetMeanF(runNum);
    }

    const Int_t nPoints = points.size();
    // Arrays to store x and y coordinates
    Double_t x[nPoints];
    Double_t y[nPoints];

    // Fill arrays with data from the vector
    for (int i = 0; i < nPoints; ++i) {
        x[i] = points[i].first;
        y[i] = points[i].second;
    }
    // Create a TGraph with the data points
    TGraph *graph = new TGraph(nPoints, x, y);
    graph->SetMarkerStyle(20); // Set marker style if needed
    graph->Draw("AP");

}



