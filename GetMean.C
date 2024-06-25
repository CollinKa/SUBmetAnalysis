#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>


TCanvas* c1 = new TCanvas("c1", "c1", 0, 400, 600, 300);


// Vector to store histogram pointers
std::vector<TH1F*> B1CH1_histograms;



void GetMeanF(int runNum = 1){
    TFile* f_in;
    std::cout << Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum) << std::endl;
    if (runNum < 10) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum));}
    else if (runNum >= 13 ) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/r000%i_board1.root", runNum,runNum));}    
    else {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000%i/board1.root", runNum));}
    //f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board1.root", runNum));
    TTree* tree0 = new TTree;
    f_in->GetObject("ch0/ped_ch0", tree0);
    
    TH1F* ch0_h = new TH1F(Form("B0ch0_Run%i",runNum), "ABEmean", 500, 0, 5000);
    tree0->Draw("ABEmean>>ch0_h");
    float mean_value = ch0_h->GetMean();
    std::cout << mean_value << std::endl;

    B1CH1_histograms.push_back(ch0_h);

}



//run 16 & 4 DNE
//for the run name run 13 - lastest run the file name follows the naming convention like _board6.root

void GetMean(){

    for (int runNum = 1; runNum < 7 ; runNum++)
    {
        if (runNum == 4 || runNum == 16 ) {continue;}

        GetMeanF(runNum);
    }

}
