void convert_to_event_one(TString input = "board1.root", unsigned int Nevt = 1000000)
{ 
  //
  // Input
  //

  // File
  TFile* f_in = new TFile(input.Data());
  
  // Trees
  TTree* tree0 = new TTree;
  f_in->GetObject("ch0/pul_ch0", tree0);
  TTree* tree1 = new TTree;
  f_in->GetObject("ch1/pul_ch1", tree1);
  TTree* tree2 = new TTree;
  f_in->GetObject("ch2/pul_ch2", tree2);
  TTree* tree3 = new TTree;
  f_in->GetObject("ch3/pul_ch3", tree3);
  TTree* tree4 = new TTree;
  f_in->GetObject("ch4/pul_ch4", tree4);
  TTree* tree5 = new TTree;
  f_in->GetObject("ch5/pul_ch5", tree5);
  TTree* tree6 = new TTree;
  f_in->GetObject("ch6/pul_ch6", tree6);
  TTree* tree7 = new TTree;
  f_in->GetObject("ch7/pul_ch7", tree7);
  TTree* tree8 = new TTree;
  f_in->GetObject("ch8/pul_ch8", tree8);
  TTree* tree9 = new TTree;
  f_in->GetObject("ch9/pul_ch9", tree9);
  TTree* tree10 = new TTree;
  f_in->GetObject("ch10/pul_ch10", tree10);
  TTree* tree11 = new TTree;
  f_in->GetObject("ch11/pul_ch11", tree11);
  TTree* tree12 = new TTree;
  f_in->GetObject("ch12/pul_ch12", tree12);
  TTree* tree13 = new TTree;
  f_in->GetObject("ch13/pul_ch13", tree13);
  TTree* tree14 = new TTree;
  f_in->GetObject("ch14/pul_ch14", tree14);
  TTree* tree15 = new TTree;
  f_in->GetObject("ch15/pul_ch15", tree15);
 
  // branches
  double t0;
  double ht0;
  double a0;
  unsigned long int  evtn0;
  unsigned short int puln0;
  
  double t1;
  double ht1;
  double a1;
  unsigned long int  evtn1;
  unsigned short int puln1;
  
  double t2;
  double ht2;
  double a2;
  unsigned long int  evtn2;
  unsigned short int puln2;
  
  double t3;
  double ht3;
  double a3;
  unsigned long int  evtn3;
  unsigned short int puln3;
  
  double t4;
  double ht4;
  double a4;
  unsigned long int  evtn4;
  unsigned short int puln4;
  
  double t5;
  double ht5;
  double a5;
  unsigned long int  evtn5;
  unsigned short int puln5;
  
  double t6;
  double ht6;
  double a6;
  unsigned long int  evtn6;
  unsigned short int puln6;
  
  double t7;
  double ht7;
  double a7;
  unsigned long int  evtn7;
  unsigned short int puln7;
  
  double t8;
  double ht8;
  double a8;
  unsigned long int  evtn8;
  unsigned short int puln8;
  
  double t9;
  double ht9;
  double a9;
  unsigned long int  evtn9;
  unsigned short int puln9;
  
  double t10;
  double ht10;
  double a10;
  unsigned long int  evtn10;
  unsigned short int puln10;
  
  double t11;
  double ht11;
  double a11;
  unsigned long int  evtn11;
  unsigned short int puln11;
  
  double t12;
  double ht12;
  double a12;
  unsigned long int  evtn12;
  unsigned short int puln12;
  
  double t13;
  double ht13;
  double a13;
  unsigned long int  evtn13;
  unsigned short int puln13;
  
  double t14;
  double ht14;
  double a14;
  unsigned long int  evtn14;
  unsigned short int puln14;
  
  double t15;
  double ht15;
  double a15;
  unsigned long int  evtn15;
  unsigned short int puln15;
  
  tree0->SetBranchAddress("ZCtime1", &t0);
  tree0->SetBranchAddress("height", &ht0);
  tree0->SetBranchAddress("area",   &a0);
  tree0->SetBranchAddress("iEve",   &evtn0);
  tree0->SetBranchAddress("pulseN", &puln0);
  
  tree1->SetBranchAddress("ZCtime1", &t1);
  tree1->SetBranchAddress("height", &ht1);
  tree1->SetBranchAddress("area",   &a1);
  tree1->SetBranchAddress("iEve",   &evtn1);
  tree1->SetBranchAddress("pulseN", &puln1);
  
  tree2->SetBranchAddress("ZCtime1", &t2);
  tree2->SetBranchAddress("height", &ht2);
  tree2->SetBranchAddress("area",   &a2);
  tree2->SetBranchAddress("iEve",   &evtn2);
  tree2->SetBranchAddress("pulseN", &puln2);
  
  tree3->SetBranchAddress("ZCtime1", &t3);
  tree3->SetBranchAddress("height", &ht3);
  tree3->SetBranchAddress("area",   &a3);
  tree3->SetBranchAddress("iEve",   &evtn3);
  tree3->SetBranchAddress("pulseN", &puln3);
  
  tree4->SetBranchAddress("ZCtime1", &t4);
  tree4->SetBranchAddress("height", &ht4);
  tree4->SetBranchAddress("area",   &a4);
  tree4->SetBranchAddress("iEve",   &evtn4);
  tree4->SetBranchAddress("pulseN", &puln4);
  
  tree5->SetBranchAddress("ZCtime1", &t5);
  tree5->SetBranchAddress("height", &ht5);
  tree5->SetBranchAddress("area",   &a5);
  tree5->SetBranchAddress("iEve",   &evtn5);
  tree5->SetBranchAddress("pulseN", &puln5);
  
  tree6->SetBranchAddress("ZCtime1", &t6);
  tree6->SetBranchAddress("height", &ht6);
  tree6->SetBranchAddress("area",   &a6);
  tree6->SetBranchAddress("iEve",   &evtn6);
  tree6->SetBranchAddress("pulseN", &puln6);
  
  tree7->SetBranchAddress("ZCtime1", &t7);
  tree7->SetBranchAddress("height", &ht7);
  tree7->SetBranchAddress("area",   &a7);
  tree7->SetBranchAddress("iEve",   &evtn7);
  tree7->SetBranchAddress("pulseN", &puln7);
  
  tree8->SetBranchAddress("ZCtime1", &t8);
  tree8->SetBranchAddress("height", &ht8);
  tree8->SetBranchAddress("area",   &a8);
  tree8->SetBranchAddress("iEve",   &evtn8);
  tree8->SetBranchAddress("pulseN", &puln8);
  
  tree9->SetBranchAddress("ZCtime1", &t9);
  tree9->SetBranchAddress("height", &ht9);
  tree9->SetBranchAddress("area",   &a9);
  tree9->SetBranchAddress("iEve",   &evtn9);
  tree9->SetBranchAddress("pulseN", &puln9);
  
  tree10->SetBranchAddress("ZCtime1", &t10);
  tree10->SetBranchAddress("height", &ht10);
  tree10->SetBranchAddress("area",   &a10);
  tree10->SetBranchAddress("iEve",   &evtn10);
  tree10->SetBranchAddress("pulseN", &puln10);
  
  tree11->SetBranchAddress("ZCtime1", &t11);
  tree11->SetBranchAddress("height", &ht11);
  tree11->SetBranchAddress("area",   &a11);
  tree11->SetBranchAddress("iEve",   &evtn11);
  tree11->SetBranchAddress("pulseN", &puln11);
  
  tree12->SetBranchAddress("ZCtime1", &t12);
  tree12->SetBranchAddress("height", &ht12);
  tree12->SetBranchAddress("area",   &a12);
  tree12->SetBranchAddress("iEve",   &evtn12);
  tree12->SetBranchAddress("pulseN", &puln12);
  
  tree13->SetBranchAddress("ZCtime1", &t13);
  tree13->SetBranchAddress("height", &ht13);
  tree13->SetBranchAddress("area",   &a13);
  tree13->SetBranchAddress("iEve",   &evtn13);
  tree13->SetBranchAddress("pulseN", &puln13);
  
  tree14->SetBranchAddress("ZCtime1", &t14);
  tree14->SetBranchAddress("height", &ht14);
  tree14->SetBranchAddress("area",   &a14);
  tree14->SetBranchAddress("iEve",   &evtn14);
  tree14->SetBranchAddress("pulseN", &puln14);
  
  tree15->SetBranchAddress("ZCtime1", &t15);
  tree15->SetBranchAddress("height", &ht15);
  tree15->SetBranchAddress("area",   &a15);
  tree15->SetBranchAddress("iEve",   &evtn15);
  tree15->SetBranchAddress("pulseN", &puln15);
  
  //
  // Output
  //
  // File 
  TFile* f_out = new TFile(input.ReplaceAll(".root", "_event.root").Data(), "RECREATE");
	f_out->cd();
  TTree* tree = new TTree("tree", "tree");

  unsigned int evt_=0;
  TBranch *evt_b =  tree->Branch("evt", &evt_);
 
  // ch0 
  vector<double>   *timing0_ = 0;    TBranch *timing0_b =  tree->Branch("timing0", &timing0_);
  vector<double>   *height0_ = 0;    TBranch *height0_b =  tree->Branch("height0", &height0_);
  vector<double>   *area0_ = 0;      TBranch *area0_b =  tree->Branch("area0", &area0_);
  unsigned short int pulseN0_ = 0;   TBranch *pulseN0_b =  tree->Branch("pulseN0", &pulseN0_);
  
  // ch1 
  vector<double>   *timing1_ = 0;    TBranch *timing1_b =  tree->Branch("timing1", &timing1_);
  vector<double>   *height1_ = 0;    TBranch *height1_b =  tree->Branch("height1", &height1_);
  vector<double>   *area1_ = 0;      TBranch *area1_b =  tree->Branch("area1", &area1_);
  unsigned short int pulseN1_ = 0;   TBranch *pulseN1_b =  tree->Branch("pulseN1", &pulseN1_);
  
  // ch2 
  vector<double>   *timing2_ = 0;    TBranch *timing2_b =  tree->Branch("timing2", &timing2_);
  vector<double>   *height2_ = 0;    TBranch *height2_b =  tree->Branch("height2", &height2_);
  vector<double>   *area2_ = 0;      TBranch *area2_b =  tree->Branch("area2", &area2_);
  unsigned short int pulseN2_ = 0;   TBranch *pulseN2_b =  tree->Branch("pulseN2", &pulseN2_);
  
  // ch3 
  vector<double>   *timing3_ = 0;    TBranch *timing3_b =  tree->Branch("timing3", &timing3_);
  vector<double>   *height3_ = 0;    TBranch *height3_b =  tree->Branch("height3", &height3_);
  vector<double>   *area3_ = 0;      TBranch *area3_b =  tree->Branch("area3", &area3_);
  unsigned short int pulseN3_ = 0;   TBranch *pulseN3_b =  tree->Branch("pulseN3", &pulseN3_);
  
  // ch4 
  vector<double>   *timing4_ = 0;    TBranch *timing4_b =  tree->Branch("timing4", &timing4_);
  vector<double>   *height4_ = 0;    TBranch *height4_b =  tree->Branch("height4", &height4_);
  vector<double>   *area4_ = 0;      TBranch *area4_b =  tree->Branch("area4", &area4_);
  unsigned short int pulseN4_ = 0;   TBranch *pulseN4_b =  tree->Branch("pulseN4", &pulseN4_);
  
  // ch5 
  vector<double>   *timing5_ = 0;    TBranch *timing5_b =  tree->Branch("timing5", &timing5_);
  vector<double>   *height5_ = 0;    TBranch *height5_b =  tree->Branch("height5", &height5_);
  vector<double>   *area5_ = 0;      TBranch *area5_b =  tree->Branch("area5", &area5_);
  unsigned short int pulseN5_ = 0;   TBranch *pulseN5_b =  tree->Branch("pulseN5", &pulseN5_);
  
  // ch6 
  vector<double>   *timing6_ = 0;    TBranch *timing6_b =  tree->Branch("timing6", &timing6_);
  vector<double>   *height6_ = 0;    TBranch *height6_b =  tree->Branch("height6", &height6_);
  vector<double>   *area6_ = 0;      TBranch *area6_b =  tree->Branch("area6", &area6_);
  unsigned short int pulseN6_ = 0;   TBranch *pulseN6_b =  tree->Branch("pulseN6", &pulseN6_);
  
  // ch7 
  vector<double>   *timing7_ = 0;    TBranch *timing7_b =  tree->Branch("timing7", &timing7_);
  vector<double>   *height7_ = 0;    TBranch *height7_b =  tree->Branch("height7", &height7_);
  vector<double>   *area7_ = 0;      TBranch *area7_b =  tree->Branch("area7", &area7_);
  unsigned short int pulseN7_ = 0;   TBranch *pulseN7_b =  tree->Branch("pulseN7", &pulseN7_);
  
  // ch8 
  vector<double>   *timing8_ = 0;    TBranch *timing8_b =  tree->Branch("timing8", &timing8_);
  vector<double>   *height8_ = 0;    TBranch *height8_b =  tree->Branch("height8", &height8_);
  vector<double>   *area8_ = 0;      TBranch *area8_b =  tree->Branch("area8", &area8_);
  unsigned short int pulseN8_ = 0;   TBranch *pulseN8_b =  tree->Branch("pulseN8", &pulseN8_);
  
  // ch9 
  vector<double>   *timing9_ = 0;    TBranch *timing9_b =  tree->Branch("timing9", &timing9_);
  vector<double>   *height9_ = 0;    TBranch *height9_b =  tree->Branch("height9", &height9_);
  vector<double>   *area9_ = 0;      TBranch *area9_b =  tree->Branch("area9", &area9_);
  unsigned short int pulseN9_ = 0;   TBranch *pulseN9_b =  tree->Branch("pulseN9", &pulseN9_);
  
  // ch10 
  vector<double>   *timing10_ = 0;    TBranch *timing10_b =  tree->Branch("timing10", &timing10_);
  vector<double>   *height10_ = 0;    TBranch *height10_b =  tree->Branch("height10", &height10_);
  vector<double>   *area10_ = 0;      TBranch *area10_b =  tree->Branch("area10", &area10_);
  unsigned short int pulseN10_ = 0;   TBranch *pulseN10_b =  tree->Branch("pulseN10", &pulseN10_);
  
  // ch11 
  vector<double>   *timing11_ = 0;    TBranch *timing11_b =  tree->Branch("timing11", &timing11_);
  vector<double>   *height11_ = 0;    TBranch *height11_b =  tree->Branch("height11", &height11_);
  vector<double>   *area11_ = 0;      TBranch *area11_b =  tree->Branch("area11", &area11_);
  unsigned short int pulseN11_ = 0;   TBranch *pulseN11_b =  tree->Branch("pulseN11", &pulseN11_);
  
  // ch12 
  vector<double>   *timing12_ = 0;    TBranch *timing12_b =  tree->Branch("timing12", &timing12_);
  vector<double>   *height12_ = 0;    TBranch *height12_b =  tree->Branch("height12", &height12_);
  vector<double>   *area12_ = 0;      TBranch *area12_b =  tree->Branch("area12", &area12_);
  unsigned short int pulseN12_ = 0;   TBranch *pulseN12_b =  tree->Branch("pulseN12", &pulseN12_);
  
  // ch13 
  vector<double>   *timing13_ = 0;    TBranch *timing13_b =  tree->Branch("timing13", &timing13_);
  vector<double>   *height13_ = 0;    TBranch *height13_b =  tree->Branch("height13", &height13_);
  vector<double>   *area13_ = 0;      TBranch *area13_b =  tree->Branch("area13", &area13_);
  unsigned short int pulseN13_ = 0;   TBranch *pulseN13_b =  tree->Branch("pulseN13", &pulseN13_);
  
  // ch14 
  vector<double>   *timing14_ = 0;    TBranch *timing14_b =  tree->Branch("timing14", &timing14_);
  vector<double>   *height14_ = 0;    TBranch *height14_b =  tree->Branch("height14", &height14_);
  vector<double>   *area14_ = 0;      TBranch *area14_b =  tree->Branch("area14", &area14_);
  unsigned short int pulseN14_ = 0;   TBranch *pulseN14_b =  tree->Branch("pulseN14", &pulseN14_);
  
  // ch15 
  vector<double>   *timing15_ = 0;    TBranch *timing15_b =  tree->Branch("timing15", &timing15_);
  vector<double>   *height15_ = 0;    TBranch *height15_b =  tree->Branch("height15", &height15_);
  vector<double>   *area15_ = 0;      TBranch *area15_b =  tree->Branch("area15", &area15_);
  unsigned short int pulseN15_ = 0;   TBranch *pulseN15_b =  tree->Branch("pulseN15", &pulseN15_);
  
  //
  unsigned int i0_begin = 0; 
  unsigned int i1_begin = 0; 
  unsigned int i2_begin = 0; 
  unsigned int i3_begin = 0; 
  unsigned int i4_begin = 0; 
  unsigned int i5_begin = 0; 
  unsigned int i6_begin = 0; 
  unsigned int i7_begin = 0; 
  unsigned int i8_begin = 0; 
  unsigned int i9_begin = 0; 
  unsigned int i10_begin = 0; 
  unsigned int i11_begin = 0; 
  unsigned int i12_begin = 0; 
  unsigned int i13_begin = 0; 
  unsigned int i14_begin = 0; 
  unsigned int i15_begin = 0; 
  for(unsigned int i = 0; i<1000000; i++)  //here is i the event idex for the new tree
  {
    if(i%10000==0) cout << "adding event " << i << endl;
    
    // ch0
    for(unsigned int i0 = i0_begin; i0<tree0->GetEntries(); i0++) 
    { 
      tree0->GetEntry(i0);
      if(i!= evtn0) break;   //evtn0 is event from iEve from tree 0(board 0 data).

      unsigned long int evtn0_current = evtn0;
      height0_->push_back(ht0);
      area0_->push_back(a0);
      timing0_->push_back(t0);
      pulseN0_ = puln0;
      // 
      tree0->GetEntry(i0+1); 
      unsigned long int evtn0_next = evtn0; //what is this for? if it goes the another event then quit and set the new iteration iEve
      if(evtn0_current!=evtn0_next) 
      { 
        i0_begin = i0+1;
        break;
      }
    }
    
    // ch2
    for(unsigned int i1 = i1_begin; i1<tree1->GetEntries(); i1++) 
    { 
      tree1->GetEntry(i1);
      if(i!= evtn1) break; 

      unsigned long int evtn1_current = evtn1;
      height1_->push_back(ht1);
      area1_->push_back(a1);
      timing1_->push_back(t1);
      pulseN1_ = puln1;
      // 
      tree1->GetEntry(i1+1); 
      unsigned long int evtn1_next = evtn1;
      if(evtn1_current!=evtn1_next) 
      { 
        i1_begin = i1+1;
        break;
      }
    }
    
    // ch2
    for(unsigned int i2 = i2_begin; i2<tree2->GetEntries(); i2++) 
    { 
      tree2->GetEntry(i2);
      if(i!= evtn2) break; 

      unsigned long int evtn2_current = evtn2;
      height2_->push_back(ht2);
      area2_->push_back(a2);
      timing2_->push_back(t2);
      pulseN2_ = puln2;
      // 
      tree2->GetEntry(i2+1); 
      unsigned long int evtn2_next = evtn2;
      if(evtn2_current!=evtn2_next) 
      { 
        i2_begin = i2+1;
        break;
      }
    }
    
    // ch3
    for(unsigned int i3 = i3_begin; i3<tree3->GetEntries(); i3++) 
    { 
      tree3->GetEntry(i3);
      if(i!= evtn3) break; 

      unsigned long int evtn3_current = evtn3;
      height3_->push_back(ht3);
      area3_->push_back(a3);
      timing3_->push_back(t3);
      pulseN3_ = puln3;
      // 
      tree3->GetEntry(i3+1); 
      unsigned long int evtn3_next = evtn3;
      if(evtn3_current!=evtn3_next) 
      { 
        i3_begin = i3+1;
        break;
      }
    }
    
    // ch4
    for(unsigned int i4 = i4_begin; i4<tree4->GetEntries(); i4++) 
    { 
      tree4->GetEntry(i4);
      if(i!= evtn4) break; 

      unsigned long int evtn4_current = evtn4;
      height4_->push_back(ht4);
      area4_->push_back(a4);
      timing4_->push_back(t4);
      pulseN4_ = puln4;
      // 
      tree4->GetEntry(i4+1); 
      unsigned long int evtn4_next = evtn4;
      if(evtn4_current!=evtn4_next) 
      { 
        i4_begin = i4+1;
        break;
      }
    }
    
    // ch5
    for(unsigned int i5 = i5_begin; i5<tree5->GetEntries(); i5++) 
    { 
      tree5->GetEntry(i5);
      if(i!= evtn5) break; 

      unsigned long int evtn5_current = evtn5;
      height5_->push_back(ht5);
      area5_->push_back(a5);
      timing5_->push_back(t5);
      pulseN5_ = puln5;
      // 
      tree5->GetEntry(i5+1); 
      unsigned long int evtn5_next = evtn5;
      if(evtn5_current!=evtn5_next) 
      { 
        i5_begin = i5+1;
        break;
      }
    }
    
    // ch6
    for(unsigned int i6 = i6_begin; i6<tree6->GetEntries(); i6++) 
    { 
      tree6->GetEntry(i6);
      if(i!= evtn6) break; 

      unsigned long int evtn6_current = evtn6;
      height6_->push_back(ht6);
      area6_->push_back(a6);
      timing6_->push_back(t6);
      pulseN6_ = puln6;
      // 
      tree6->GetEntry(i6+1); 
      unsigned long int evtn6_next = evtn6;
      if(evtn6_current!=evtn6_next) 
      { 
        i6_begin = i6+1;
        break;
      }
    }
    
    // ch7
    for(unsigned int i7 = i7_begin; i7<tree7->GetEntries(); i7++) 
    { 
      tree7->GetEntry(i7);
      if(i!= evtn7) break; 

      unsigned long int evtn7_current = evtn7;
      height7_->push_back(ht7);
      area7_->push_back(a7);
      timing7_->push_back(t7);
      pulseN7_ = puln7;
      // 
      tree7->GetEntry(i7+1); 
      unsigned long int evtn7_next = evtn7;
      if(evtn7_current!=evtn7_next) 
      { 
        i7_begin = i7+1;
        break;
      }
    }
    
    // ch8
    for(unsigned int i8 = i8_begin; i8<tree8->GetEntries(); i8++) 
    { 
      tree8->GetEntry(i8);
      if(i!= evtn8) break; 

      unsigned long int evtn8_current = evtn8;
      height8_->push_back(ht8);
      area8_->push_back(a8);
      timing8_->push_back(t8);
      pulseN8_ = puln8;
      // 
      tree8->GetEntry(i8+1); 
      unsigned long int evtn8_next = evtn8;
      if(evtn8_current!=evtn8_next) 
      { 
        i8_begin = i8+1;
        break;
      }
    }
    
    // ch9
    for(unsigned int i9 = i9_begin; i9<tree9->GetEntries(); i9++) 
    { 
      tree9->GetEntry(i9);
      if(i!= evtn9) break; 

      unsigned long int evtn9_current = evtn9;
      height9_->push_back(ht9);
      area9_->push_back(a9);
      timing9_->push_back(t9);
      pulseN9_ = puln9;
      // 
      tree9->GetEntry(i9+1); 
      unsigned long int evtn9_next = evtn9;
      if(evtn9_current!=evtn9_next) 
      { 
        i9_begin = i9+1;
        break;
      }
    }
    
    // ch10
    for(unsigned int i10 = i10_begin; i10<tree10->GetEntries(); i10++) 
    { 
      tree10->GetEntry(i10);
      if(i!= evtn10) break; 

      unsigned long int evtn10_current = evtn10;
      height10_->push_back(ht10);
      area10_->push_back(a10);
      timing10_->push_back(t10);
      pulseN10_ = puln10;
      // 
      tree10->GetEntry(i10+1); 
      unsigned long int evtn10_next = evtn10;
      if(evtn10_current!=evtn10_next) 
      { 
        i10_begin = i10+1;
        break;
      }
    }
    
    // ch11
    for(unsigned int i11 = i11_begin; i11<tree11->GetEntries(); i11++) 
    { 
      tree11->GetEntry(i11);
      if(i!= evtn11) break; 

      unsigned long int evtn11_current = evtn11;
      height11_->push_back(ht11);
      area11_->push_back(a11);
      timing11_->push_back(t11);
      pulseN11_ = puln11;
      // 
      tree11->GetEntry(i11+1); 
      unsigned long int evtn11_next = evtn11;
      if(evtn11_current!=evtn11_next) 
      { 
        i11_begin = i11+1;
        break;
      }
    }
    
    // ch12
    for(unsigned int i12 = i12_begin; i12<tree12->GetEntries(); i12++) 
    { 
      tree12->GetEntry(i12);
      if(i!= evtn12) break; 

      unsigned long int evtn12_current = evtn12;
      height12_->push_back(ht12);
      area12_->push_back(a12);
      timing12_->push_back(t12);
      pulseN12_ = puln12;
      // 
      tree12->GetEntry(i12+1); 
      unsigned long int evtn12_next = evtn12;
      if(evtn12_current!=evtn12_next) 
      { 
        i12_begin = i12+1;
        break;
      }
    }
    
    // ch13
    for(unsigned int i13 = i13_begin; i13<tree13->GetEntries(); i13++) 
    { 
      tree13->GetEntry(i13);
      if(i!= evtn13) break; 

      unsigned long int evtn13_current = evtn13;
      height13_->push_back(ht13);
      area13_->push_back(a13);
      timing13_->push_back(t13);
      pulseN13_ = puln13;
      // 
      tree13->GetEntry(i13+1); 
      unsigned long int evtn13_next = evtn13;
      if(evtn13_current!=evtn13_next) 
      { 
        i13_begin = i13+1;
        break;
      }
    }
    
    // ch14
    for(unsigned int i14 = i14_begin; i14<tree14->GetEntries(); i14++) 
    { 
      tree14->GetEntry(i14);
      if(i!= evtn14) break; 

      unsigned long int evtn14_current = evtn14;
      height14_->push_back(ht14);
      area14_->push_back(a14);
      timing14_->push_back(t14);
      pulseN14_ = puln14;
      // 
      tree14->GetEntry(i14+1); 
      unsigned long int evtn14_next = evtn14;
      if(evtn14_current!=evtn14_next) 
      { 
        i14_begin = i14+1;
        break;
      }
    }
    
    // ch15
    for(unsigned int i15 = i15_begin; i15<tree15->GetEntries(); i15++) 
    { 
      tree15->GetEntry(i15);
      if(i!= evtn15) break; 

      unsigned long int evtn15_current = evtn15;
      height15_->push_back(ht15);
      area15_->push_back(a15);
      timing15_->push_back(t15);
      pulseN15_ = puln15;
      // 
      tree15->GetEntry(i15+1); 
      unsigned long int evtn15_next = evtn15;
      if(evtn15_current!=evtn15_next) 
      { 
        i15_begin = i15+1;
        break;
      }
    }

    evt_ = i+1;
      
    // fill tree
    tree->Fill(); 

    timing0_->clear();  height0_->clear();  area0_->clear();  pulseN0_ = 0;
    timing1_->clear();  height1_->clear();  area1_->clear();  pulseN1_ = 0;
    timing2_->clear();  height2_->clear();  area2_->clear();  pulseN2_ = 0;
    timing3_->clear();  height3_->clear();  area3_->clear();  pulseN3_ = 0;
    timing4_->clear();  height4_->clear();  area4_->clear();  pulseN4_ = 0;
    timing5_->clear();  height5_->clear();  area5_->clear();  pulseN5_ = 0;
    timing6_->clear();  height6_->clear();  area6_->clear();  pulseN6_ = 0;
    timing7_->clear();  height7_->clear();  area7_->clear();  pulseN7_ = 0;
    timing8_->clear();  height8_->clear();  area8_->clear();  pulseN8_ = 0;
    timing9_->clear();  height9_->clear();  area9_->clear();  pulseN9_ = 0;
    timing10_->clear();  height10_->clear();  area10_->clear();  pulseN10_ = 0;
    timing11_->clear();  height11_->clear();  area11_->clear();  pulseN11_ = 0;
    timing12_->clear();  height12_->clear();  area12_->clear();  pulseN12_ = 0;
    timing13_->clear();  height13_->clear();  area13_->clear();  pulseN13_ = 0;
    timing14_->clear();  height14_->clear();  area14_->clear();  pulseN14_ = 0;
    timing15_->clear();  height15_->clear();  area15_->clear();  pulseN15_ = 0;
  }
    
  f_in->Close();
  f_out->cd();
  tree->Write();
  f_out->Close();  

}

void convert_to_event()
{ 

  for(int i=1; i<11; i++)
  {
    if(i>1) continue;
    convert_to_event_one(Form("board%i.root", i));
  }
}
