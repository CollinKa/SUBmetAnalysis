#include "TCanvas.h"
#include "TTree.h"
#include "TFile.h"

#include <iostream>
#include <filesystem>

double GetMeanValue(int boardNum,int runNum , int ChanNum){
    TFile* f_in;
    std::cout << Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board%i.root", runNum,boardNum) << std::endl;
    if (runNum < 10) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r0000%i/board%i.root", runNum,boardNum));}
    else if (runNum >= 13 ) {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000%i/r000%i_board%i.root", runNum,runNum,boardNum));}    
    else {f_in = new TFile(Form("/Users/haoliangzheng/subMETData/beamOn/runs/Exp00/r000%i/board%i.root", runNum,boardNum));}
    
    //check if the file exist
    if (!f_in || f_in->IsZombie()) {
        
        
        // Clean up the file object if it was created but is in a bad state
        if (f_in) delete f_in;

        
        return -1;  //return the mean value as -1, so it can't be seen on the canvas
    }
    
    
    TTree* tree0 = new TTree;
    f_in->GetObject(Form("ch%i/ped_ch%i",ChanNum,ChanNum), tree0);
    TH1F* ch0_h = new TH1F("ch0_h", "ABEmean", 500, 0, 5000);
    tree0->Draw("ABEmean>>ch0_h"); // I doubt if this can work

    //close the file and delete the tree
    float mean_value = ch0_h->GetMean();




    //To do : delete the tree and histogram after iteration to save memory

    f_in->Close();
    /*
    delete f_in;
    delete ch0_h;
    delete tree0;
    */
    


    
    return mean_value;

}


void MakePlot(TGraph& graph,const std::vector<std::pair<double, double>>& datapair, int markerStyle=2){
    const Int_t nPointsCH1 = datapair.size();
    Double_t RunN[nPointsCH1];//this might need to be removed
    Double_t Mean[nPointsCH1];

    // separate the data pair
    for (int i = 0; i < nPointsCH1; ++i) {
        RunN[i] = datapair[i].first;
        Mean[i] = datapair[i].second;
        graph.SetPoint(i,datapair[i].first,datapair[i].second);
        
    }
    graph.SetMarkerStyle(markerStyle);
    

    
    //TGraph *graph = new TGraph(nPointsCH1, RunN, Mean);  //this might need to be removed
}



//main function
void tryTree(){

    int runNum;
    int boardNum;
    int chanNum;



    std::vector<std::pair<double, double>> CH0Data;
    std::vector<std::pair<double, double>> CH1Data;
    std::vector<std::pair<double, double>> CH2Data;
    std::vector<std::pair<double, double>> CH3Data;
    std::vector<std::pair<double, double>> CH4Data; 
    std::vector<std::pair<double, double>> CH5Data;
    std::vector<std::pair<double, double>> CH6Data;
    std::vector<std::pair<double, double>> CH7Data;
    std::vector<std::pair<double, double>> CH8Data;
    std::vector<std::pair<double, double>> CH9Data;
    std::vector<std::pair<double, double>> CH10Data;
    std::vector<std::pair<double, double>> CH11Data;
    std::vector<std::pair<double, double>> CH12Data;  
    std::vector<std::pair<double, double>> CH13Data;
    std::vector<std::pair<double, double>> CH14Data;
    std::vector<std::pair<double, double>> CH15Data;

    


    


    for (boardNum = 1; boardNum < 11; ++boardNum )
    {

        //create the canvas for each board
        
        


        for (runNum = 1; runNum < 32; ++runNum ) 
        {

            if (runNum == 4 || runNum == 16 ) {continue;} //The files for these two run are missing

            for (chanNum = 0; chanNum<16; ++chanNum)
            {
                double mean_value = GetMeanValue(boardNum,runNum,chanNum);
                if (chanNum == 0) {
                    CH0Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 1) {
                    CH1Data.push_back(std::make_pair(runNum, mean_value));
                    
                }
                else if (chanNum == 2)  {
                    CH2Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 3)  {
                    CH3Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 4)  {
                    CH4Data.push_back(std::make_pair(runNum, mean_value));
                    
                }
                else if (chanNum == 5)  {
                    CH5Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 6)  {
                    CH6Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 7)  {
                    CH7Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 8)  {
                    CH8Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 9) {
                    CH9Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 10) {
                    CH10Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 11) {
                    CH11Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 12)  {
                    CH12Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 13) {
                    CH13Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 14)  {
                    CH14Data.push_back(std::make_pair(runNum, mean_value));
                }
                else if (chanNum == 15)  {
                    CH15Data.push_back(std::make_pair(runNum, mean_value));
                }

                std::cout << chanNum << std::endl;
                std::cout << mean_value << std::endl;
            }//end of channel loop

        }//end of run number loop

        TCanvas *canvas = new TCanvas("canvas", "Overlayed Scatter Plots", 800, 600);
        gPad->DrawFrame(0, 3500, 40, 3760,"Overlayed Scatter Plots;X-axis;Y-axis");

        TGraph CH_0G;
        TGraph CH_1G;
        TGraph CH_2G;
        TGraph CH_3G;
        TGraph CH_4G;
        TGraph CH_5G;
        TGraph CH_6G;
        TGraph CH_7G;
        TGraph CH_8G;
        TGraph CH_9G;
        TGraph CH_10G;
        TGraph CH_11G;
        TGraph CH_12G;
        TGraph CH_13G;
        TGraph CH_14G;
        TGraph CH_15G;

        MakePlot(CH_0G,CH0Data,0);
        MakePlot(CH_1G,CH1Data,1);
        MakePlot(CH_2G,CH2Data,2);
        MakePlot(CH_3G,CH3Data,3);
        MakePlot(CH_4G,CH4Data,4);
        MakePlot(CH_5G,CH5Data,5);
        MakePlot(CH_6G,CH6Data,6);
        MakePlot(CH_7G,CH7Data,7);
        MakePlot(CH_8G,CH8Data,8);
        MakePlot(CH_9G,CH9Data,9);
        MakePlot(CH_10G,CH10Data,10);
        MakePlot(CH_11G,CH11Data,11);
        MakePlot(CH_12G,CH12Data,12);
        MakePlot(CH_13G,CH13Data,13);
        MakePlot(CH_14G,CH14Data,14);
        MakePlot(CH_15G,CH15Data,15);

        CH_0G.Draw("PL");
        CH_1G.Draw("PLsame");
        CH_2G.Draw("PLsame");
        CH_3G.Draw("PLsame");
        CH_4G.Draw("PLsame");
        CH_4G.Draw("PLsame");
        CH_5G.Draw("PLsame");
        CH_6G.Draw("PLsame");
        CH_7G.Draw("PLsame");
        CH_8G.Draw("PLsame");
        CH_9G.Draw("PLsame");
        CH_10G.Draw("PLsame");
        CH_11G.Draw("PLsame");
        CH_12G.Draw("PLsame");
        CH_13G.Draw("PLsame");
        CH_14G.Draw("PLsame");
        CH_15G.Draw("PLsame");

        TLegend *legend = new TLegend(0.7, 0.7, 0.9, 0.9); 
        legend->SetHeader("Legend", "C");
        legend->AddEntry(&CH_0G, "CH0", "p");
        legend->AddEntry(&CH_1G, "CH1", "p");
        legend->AddEntry(&CH_2G, "CH2", "p");
        legend->AddEntry(&CH_3G, "CH3", "p");
        legend->AddEntry(&CH_4G, "CH4", "p");
        legend->AddEntry(&CH_5G, "CH5", "p");
        legend->AddEntry(&CH_6G, "CH6", "p");
        legend->AddEntry(&CH_7G, "CH7", "p");
        legend->AddEntry(&CH_8G, "CH8", "p");
        legend->AddEntry(&CH_9G, "CH9", "p");
        legend->AddEntry(&CH_10G, "CH10", "p");
        legend->AddEntry(&CH_11G, "CH11", "p");
        legend->AddEntry(&CH_12G, "CH12", "p");
        legend->AddEntry(&CH_13G, "CH13", "p");
        legend->AddEntry(&CH_14G, "CH14", "p");
        legend->AddEntry(&CH_15G, "CH15", "p");

        // Draw the legend
        legend->Draw();
        canvas->Update();

        
        //MakePlot(TGraph& graph,const std::vector<std::pair<double, double>>& datapair)
        TFile* rootFile = new TFile(Form("baseLineABSMean_board%i.root",boardNum), "RECREATE");
        
        canvas->Write();



        CH0Data.clear();
        CH1Data.clear();
        CH2Data.clear();
        CH3Data.clear();
        CH4Data.clear();
        CH5Data.clear();
        CH6Data.clear();
        CH7Data.clear();
        CH8Data.clear();
        CH9Data.clear();
        CH10Data.clear();
        CH11Data.clear();
        CH12Data.clear();
        CH13Data.clear();
        CH14Data.clear();
        CH15Data.clear();
        rootFile->Close();
        
    
    } //end of the board loop
    
    
    
}