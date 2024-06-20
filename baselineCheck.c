#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>

void baselineCheck(TString input = "/Users/haoliangzheng/subMETData/beamOn/Jun9/r00008/board1.root") {

    TFile* f_in = new TFile(input.Data());
    TFile outputFile("baselineboard1.root", "RECREATE");

    // Trees
    TTree* tree0 = new TTree;
    f_in->GetObject("ch0/ped_ch0", tree0);
    TTree* tree1 = new TTree;
    f_in->GetObject("ch1/ped_ch1", tree1);
    TTree* tree2 = new TTree;
    f_in->GetObject("ch2/ped_ch2", tree2);
    TTree* tree3 = new TTree;
    f_in->GetObject("ch3/ped_ch3", tree3);
    TTree* tree4 = new TTree;
    f_in->GetObject("ch4/ped_ch4", tree4);
    TTree* tree5 = new TTree;
    f_in->GetObject("ch5/ped_ch5", tree5);
    TTree* tree6 = new TTree;
    f_in->GetObject("ch6/ped_ch6", tree6);
    TTree* tree7 = new TTree;
    f_in->GetObject("ch7/ped_ch7", tree7);
    TTree* tree8 = new TTree;
    f_in->GetObject("ch8/ped_ch8", tree8);
    TTree* tree9 = new TTree;
    f_in->GetObject("ch9/ped_ch9", tree9);
    TTree* tree10 = new TTree;
    f_in->GetObject("ch10/ped_ch10", tree10);
    TTree* tree11 = new TTree;
    f_in->GetObject("ch11/ped_ch11", tree11);
    TTree* tree12 = new TTree;
    f_in->GetObject("ch12/ped_ch12", tree12);
    TTree* tree13 = new TTree;
    f_in->GetObject("ch13/ped_ch13", tree13);
    TTree* tree14 = new TTree;
    f_in->GetObject("ch14/ped_ch14", tree14);
    TTree* tree15 = new TTree;
    f_in->GetObject("ch15/ped_ch15", tree15);


    //create histograms for different channels
    TH1F* ch0_h = new TH1F("ch0_h", "ABEmean", 100, 0, 5000);
    TH1F* ch1_h = new TH1F("ch1_h", "ABEmean", 100, 0, 5000);
    TH1F* ch2_h = new TH1F("ch2_h", "ABEmean", 100, 0, 5000);

    TH1F* merged = new TH1F("merged", "ABEmean merged", 100, 0, 5000);

    TCanvas* c1 = new TCanvas("c1", "c1", 0, 400, 600, 300);
    c1->SetFillColor(0);

    ch0_h->SetLineColor(kBlack);
    ch1_h->SetLineColor(kGreen);

    //Draw command here is used to save the AMEmean data to the histogram
    tree0->Draw("ABEmean>>ch0_h");
    tree1->Draw("ABEmean>>ch1_h");

    ch0_h->Draw();   
    ch1_h->Draw("same");   
    
    //merged->Add(ch0_h);
    //merged->Add(ch1_h);
    //merged->Add(ch2_h);

    //c1->cd();
    c1->Update();
    TLegend* legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    legend->AddEntry(ch0_h, "chan 0", "l");
    legend->AddEntry(ch1_h, "chan 1", "l");
    legend->Draw();

    merged->Write();
    c1->Write();
    outputFile.Close();


}