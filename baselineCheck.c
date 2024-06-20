#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>

void baselineCheckF(TString input = "/Users/haoliangzheng/subMETData/beamOn/Jun9/r00008/board1.root", int i = 1) 
{

    TFile* f_in = new TFile(input.Data());
    TFile outputFile(Form("baselineboard%i.root",i) , "RECREATE");

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
    TH1F* ch0_h = new TH1F("ch0_h", "ABEmean", 500, 0, 5000);
    TH1F* ch1_h = new TH1F("ch1_h", "ABEmean", 500, 0, 5000);
    TH1F* ch2_h = new TH1F("ch2_h", "ABEmean", 500, 0, 5000);
    TH1F* ch3_h = new TH1F("ch3_h", "ABEmean", 500, 0, 5000);
    TH1F* ch4_h = new TH1F("ch4_h", "ABEmean", 500, 0, 5000);
    TH1F* ch5_h = new TH1F("ch5_h", "ABEmean", 500, 0, 5000);
    TH1F* ch6_h = new TH1F("ch6_h", "ABEmean", 500, 0, 5000);
    TH1F* ch7_h = new TH1F("ch7_h", "ABEmean", 500, 0, 5000);
    TH1F* ch8_h = new TH1F("ch8_h", "ABEmean", 500, 0, 5000);
    TH1F* ch9_h = new TH1F("ch9_h", "ABEmean", 500, 0, 5000);
    TH1F* ch10_h = new TH1F("ch10_h", "ABEmean", 500, 0, 5000);



    TCanvas* c1 = new TCanvas("c1", "c1", 0, 400, 600, 300);
    c1->SetFillColor(0);

    ch0_h->SetLineColor(kBlack);
    ch1_h->SetLineColor(kGreen);

    //Draw command at here is used to save the AMEmean data to the histograms.
    tree0->Draw("ABEmean>>ch0_h");
    tree1->Draw("ABEmean>>ch1_h");
    tree2->Draw("ABEmean>>ch2_h");
    tree3->Draw("ABEmean>>ch3_h");
    tree4->Draw("ABEmean>>ch4_h");
    tree5->Draw("ABEmean>>ch5_h");
    tree6->Draw("ABEmean>>ch6_h");
    tree7->Draw("ABEmean>>ch7_h");
    tree8->Draw("ABEmean>>ch8_h");
    tree9->Draw("ABEmean>>ch9_h");
    tree10->Draw("ABEmean>>ch10_h");

    ch0_h->Draw();   
    ch1_h->Draw("same");   
    ch2_h->Draw("same"); 
    ch3_h->Draw("same");    
    ch4_h->Draw("same");  
    ch5_h->Draw("same");  
    ch6_h->Draw("same");
    ch7_h->Draw("same");    
    ch8_h->Draw("same");  
    ch9_h->Draw("same");  
    ch10_h->Draw("same");  

    

    //c1->cd();
    c1->Update();
    TLegend* legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    legend->AddEntry(ch0_h, "chan 0", "l");
    legend->AddEntry(ch1_h, "chan 1", "l");
    legend->AddEntry(ch2_h, "chan 2", "l");
    legend->AddEntry(ch3_h, "chan 3", "l");
    legend->AddEntry(ch4_h, "chan 4", "l");
    legend->AddEntry(ch5_h, "chan 5", "l");
    legend->AddEntry(ch6_h, "chan 6", "l");
    legend->AddEntry(ch7_h, "chan 7", "l");
    legend->AddEntry(ch8_h, "chan 8", "l");
    legend->AddEntry(ch9_h, "chan 9", "l");
    legend->AddEntry(ch10_h, "chan 10", "l");


    legend->Draw();

    c1->Write();
    outputFile.Close();


}


void baselineCheck()
{ 
    for(int i=1; i<11; i++)
    {
        baselineCheckF(Form("/Users/haoliangzheng/subMETData/beamOn/Jun9/r00008/board%i.root",i), i);
    }
}