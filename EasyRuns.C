#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>


void EasyRuns() {


TCanvas* c1 = new TCanvas("c1", "c1", 0, 400, 600, 300);
c1->SetFillColor(0);

TFile* f_in0 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00000/board1.root","READ");
TFile* f_in1 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00001/board1.root","READ");
TFile* f_in2 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00002/board1.root","READ");
TFile* f_in3 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00003/board1.root","READ");
//run 4 is extremly short only
TFile* f_in5 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00005/board1.root","READ"); 
TFile* f_in6 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00006/board1.root","READ");
TFile* f_in7 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00007/board1.root","READ");
TFile* f_in8 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00008/board1.root","READ");
TFile* f_in9 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00009/board1.root","READ");
TFile* f_in10 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00010/board1.root","READ");
TFile* f_in11 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00011/board1.root","READ");
TFile* f_in12 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00012/board1.root","READ");
TFile* f_in13 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00013/r00013_board1.root","READ");
TFile* f_in14 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00014/r00014_board1.root","READ");
TFile* f_in15 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00015/r00015_board1.root","READ");
//there is no run 16
TFile* f_in17 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00017/r00017_board1.root","READ");
TFile* f_in18 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00018/r00018_board1.root","READ");
TFile* f_in19 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00019/r00019_board1.root","READ");
TFile* f_in20 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00020/r00020_board1.root","READ");
TFile* f_in21 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00021/r00021_board1.root","READ");
TFile* f_in22 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00022/r00022_board1.root","READ");
TFile* f_in23 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00023/r00023_board1.root","READ");
TFile* f_in24 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00024/r00024_board1.root","READ");
TFile* f_in25 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00025/r00025_board1.root","READ");
TFile* f_in26 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00026/r00026_board1.root","READ");
TFile* f_in27 = new TFile("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r00027/r00027_board1.root","READ");


TTree* tree0 = new TTree;
TTree* tree1 = new TTree;
TTree* tree2 = new TTree;
TTree* tree3 = new TTree;
TTree* tree5 = new TTree;
TTree* tree6 = new TTree;
TTree* tree7 = new TTree;
TTree* tree8 = new TTree;
TTree* tree9 = new TTree;
TTree* tree10 = new TTree;
TTree* tree11 = new TTree;
TTree* tree12 = new TTree;
TTree* tree13 = new TTree;
TTree* tree14 = new TTree;
TTree* tree15 = new TTree;
TTree* tree17 = new TTree;
TTree* tree18 = new TTree;
TTree* tree19 = new TTree;
TTree* tree20 = new TTree;
TTree* tree21 = new TTree;
TTree* tree22 = new TTree;
TTree* tree23 = new TTree;
TTree* tree24 = new TTree;
TTree* tree25 = new TTree;
TTree* tree26 = new TTree;
TTree* tree27 = new TTree;





f_in0->GetObject("ch1/ped_ch1", tree0);
f_in1->GetObject("ch1/ped_ch1", tree1);
f_in2->GetObject("ch1/ped_ch1", tree2);
f_in3->GetObject("ch1/ped_ch1", tree3);
f_in5->GetObject("ch1/ped_ch1", tree5);
f_in6->GetObject("ch1/ped_ch1", tree6);
f_in7->GetObject("ch1/ped_ch1", tree7);
f_in8->GetObject("ch1/ped_ch1", tree8);
f_in9->GetObject("ch1/ped_ch1", tree9);
f_in10->GetObject("ch1/ped_ch1", tree10);
f_in11->GetObject("ch1/ped_ch1", tree11);
f_in12->GetObject("ch1/ped_ch1", tree12);
f_in13->GetObject("ch1/ped_ch1", tree13);
f_in14->GetObject("ch1/ped_ch1", tree14);
f_in15->GetObject("ch1/ped_ch1", tree15);
f_in17->GetObject("ch1/ped_ch1", tree17);
f_in18->GetObject("ch1/ped_ch1", tree18);
f_in19->GetObject("ch1/ped_ch1", tree19);
f_in20->GetObject("ch1/ped_ch1", tree20);
f_in21->GetObject("ch1/ped_ch1", tree21);
f_in22->GetObject("ch1/ped_ch1", tree22);
f_in23->GetObject("ch1/ped_ch1", tree23);
f_in24->GetObject("ch1/ped_ch1", tree24);
f_in25->GetObject("ch1/ped_ch1", tree25);
f_in26->GetObject("ch1/ped_ch1", tree26);
f_in27->GetObject("ch1/ped_ch1", tree27);


TH1F* ch1_R0 = new TH1F("ch1_R0", "ABEmean", 500, 0, 5000);
TH1F* ch1_R1 = new TH1F("ch1_R1", "ABEmean", 500, 0, 5000);
TH1F* ch1_R2 = new TH1F("ch1_R2", "ABEmean", 500, 0, 5000);
TH1F* ch1_R3 = new TH1F("ch1_R3", "ABEmean", 500, 0, 5000);
TH1F* ch1_R5 = new TH1F("ch1_R5", "ABEmean", 500, 0, 5000);
TH1F* ch1_R6 = new TH1F("ch1_R6", "ABEmean", 500, 0, 5000);
TH1F* ch1_R7 = new TH1F("ch1_R7", "ABEmean", 500, 0, 5000);
TH1F* ch1_R8 = new TH1F("ch1_R8", "ABEmean", 500, 0, 5000);
TH1F* ch1_R9 = new TH1F("ch1_R9", "ABEmean", 500, 0, 5000);
TH1F* ch1_R10 = new TH1F("ch1_R10", "ABEmean", 500, 0, 5000);
TH1F* ch1_R11 = new TH1F("ch1_R11", "ABEmean", 500, 0, 5000);
TH1F* ch1_R12 = new TH1F("ch1_R12", "ABEmean", 500, 0, 5000);
TH1F* ch1_R13 = new TH1F("ch1_R13", "ABEmean", 500, 0, 5000);
TH1F* ch1_R14 = new TH1F("ch1_R14", "ABEmean", 500, 0, 5000);
TH1F* ch1_R15 = new TH1F("ch1_R15", "ABEmean", 500, 0, 5000);
TH1F* ch1_R17 = new TH1F("ch1_R17", "ABEmean", 500, 0, 5000);
TH1F* ch1_R18 = new TH1F("ch1_R18", "ABEmean", 500, 0, 5000);
TH1F* ch1_R19 = new TH1F("ch1_R19", "ABEmean", 500, 0, 5000);
TH1F* ch1_R20 = new TH1F("ch1_R20", "ABEmean", 500, 0, 5000);
TH1F* ch1_R21 = new TH1F("ch1_R21", "ABEmean", 500, 0, 5000);
TH1F* ch1_R22 = new TH1F("ch1_R22", "ABEmean", 500, 0, 5000);
TH1F* ch1_R23 = new TH1F("ch1_R23", "ABEmean", 500, 0, 5000);
TH1F* ch1_R24 = new TH1F("ch1_R24", "ABEmean", 500, 0, 5000);
TH1F* ch1_R25 = new TH1F("ch1_R25", "ABEmean", 500, 0, 5000);
TH1F* ch1_R26 = new TH1F("ch1_R26", "ABEmean", 500, 0, 5000);
TH1F* ch1_R27 = new TH1F("ch1_R27", "ABEmean", 500, 0, 5000);

tree0->Draw("ABEmean>>ch1_R0");
tree1->Draw("ABEmean>>ch1_R1");
tree2->Draw("ABEmean>>ch1_R2");
tree3->Draw("ABEmean>>ch1_R3");
tree5->Draw("ABEmean>>ch1_R5");
tree6->Draw("ABEmean>>ch1_R6");
tree7->Draw("ABEmean>>ch1_R7");
tree8->Draw("ABEmean>>ch1_R8");
tree9->Draw("ABEmean>>ch1_R9");
tree10->Draw("ABEmean>>ch1_R10");
tree11->Draw("ABEmean>>ch1_R11");
tree12->Draw("ABEmean>>ch1_R12");
tree13->Draw("ABEmean>>ch1_R13");
tree14->Draw("ABEmean>>ch1_R14");
tree15->Draw("ABEmean>>ch1_R15");
tree17->Draw("ABEmean>>ch1_R17");
tree18->Draw("ABEmean>>ch1_R18");
tree19->Draw("ABEmean>>ch1_R19");
tree20->Draw("ABEmean>>ch1_R20");
tree21->Draw("ABEmean>>ch1_R21");
tree22->Draw("ABEmean>>ch1_R22");
tree23->Draw("ABEmean>>ch1_R23");
tree24->Draw("ABEmean>>ch1_R24");
tree25->Draw("ABEmean>>ch1_R25");
tree26->Draw("ABEmean>>ch1_R26");
tree27->Draw("ABEmean>>ch1_R27");


//f_in27->Close();
TFile outputFile("board1Ch1Runs.root" , "RECREATE");

ch1_R0->Draw();   
ch1_R1->Draw("same");  
ch1_R2->Draw("same");  
ch1_R3->Draw("same");  
ch1_R5->Draw("same");  
ch1_R6->Draw("same");  
ch1_R7->Draw("same");  
ch1_R8->Draw("same");  
ch1_R9->Draw("same");  
ch1_R10->Draw("same");  
ch1_R11->Draw("same");  
ch1_R12->Draw("same");  
ch1_R13->Draw("same");  
ch1_R14->Draw("same");  
ch1_R15->Draw("same");  
ch1_R17->Draw("same");  
ch1_R18->Draw("same");  
ch1_R19->Draw("same");  
ch1_R20->Draw("same");  
ch1_R21->Draw("same");  
ch1_R22->Draw("same");  
ch1_R23->Draw("same");  
ch1_R24->Draw("same");  
ch1_R25->Draw("same");  
ch1_R26->Draw("same");  
ch1_R27->Draw("same");  


//c1->Update();
c1->cd();
c1->Write();
outputFile.Close();

}



