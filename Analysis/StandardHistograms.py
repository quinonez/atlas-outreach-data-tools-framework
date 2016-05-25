"""This file defines standard histograms which can be reused in various analyses.
The ranges of these histograms should accomodate most analyses.
"""

import ROOT

def getStandardHistogram(name):
    if (name == "vxp_z"):        return ROOT.TH1D("vxp_z",                 "Primary Vertex Position; z_{Vertex}; Events", 40, -200,200)
    if (name == "pvxp_n"):       return ROOT.TH1D("pvxp_n",                "Number of Vertices; N_{vertex}; Events", 30, -0.5,29.5)
    if (name == "etmiss"):       return ROOT.TH1D("etmiss",                "Missing Transverse Momentum;MET;Events", 20, 0,200)
                                                                           
    if (name == "n_jets"):       return ROOT.TH1D("n_jets",                "Number of Jets;N_{jets};Events", 10, -0.5, 9.5)
    if (name == "jet_pt"):       return ROOT.TH1D("jet_pt",                "Jet Transverse Momentum;p_{T}^{jet};Jets", 20, 0, 200)
    if (name == "jet_m"):        return ROOT.TH1D("jet_m",                 "Jet Mass; m^{jet} [MeV]; Jets", 20, 0, 20000)
    if (name == "jet_jvf"):      return ROOT.TH1D("jet_jvf",               "Jet Vertex Fraction; JVF ; Jets", 20, 0, 1)
    if (name == "jet_eta"):      return ROOT.TH1D("jet_eta",               "Jet Pseudorapidity; #eta^{jet}; Jets", 30, -3, 3)
    if (name == "jet_MV1"):      return ROOT.TH1D("jet_MV1",               "Jet MV1; MV1 weight ; Jets", 20, 0, 1)
    if (name == "lep_n"):        return ROOT.TH1D("lep_n",                 "Number of Leptons; N_{lep} ;Events", 10, -0.5, 9.5)
                                                                           
    if (name == "lep_pt"):       return ROOT.TH1D("lep_pt",                "Lepton Transverse Momentum;p_{T}^{lep};Leptons", 20, 0, 200)
    if (name == "lep_eta"):      return ROOT.TH1D("lep_eta",               "Lepton Pseudorapidity; #eta^{lep}; Leptons", 30, -3, 3)
    if (name == "lep_E"):        return ROOT.TH1D("lep_E",                 "Lepton Energy; E^{lep} [GeV]; Leptons", 30, 0, 300)
    if (name == "lep_phi"):      return ROOT.TH1D("lep_phi",               "Lepton Azimuthal Angle ; #phi^{lep}; Leptons", 32, -3.2, 3.2)
    if (name == "lep_charge"):   return ROOT.TH1D("lep_charge",            "Lepton Charge; Q^{lep}; Leptons", 7, -1.75, 1.75)
    if (name == "lep_type"):     return ROOT.TH1D("lep_type",              "Lepton PDG ID; PDGID^{lep}; Leptons", 61, -30.5, 30.5)
    if (name == "lep_ptcone30"): return ROOT.TH1D("lep_ptcone30",          "Lepton Transverse Momentum Isolation; ptcone30^{lep}; Leptons", 30, -4.5, 10.5)
    if (name == "lep_etcone20"): return ROOT.TH1D("lep_etcone20",          "Lepton Transverse Energy Isolation; etcone20^{lep}; Leptons", 30, -4.5, 10.5)
    if (name == "lep_z0"):       return ROOT.TH1D("lep_z0",                "Lepton z0 impact parameter; z_{0}^{lep}; Leptons", 20, -1, 1)
    if (name == "lep_d0"):       return ROOT.TH1D("lep_d0",                "Lepton d0 impact parameter; d_{0}^{lep}; Leptons", 20, -1, 1)

    if (name == "leadlep_pt"):        return ROOT.TH1D("leadlep_pt",       "Leading Lepton Transverse Momentum;p_{T}^{leadlep};Leptons", 20, 0, 200)
    if (name == "leadlep_eta"):       return ROOT.TH1D("leadlep_eta",      "Leading Lepton Pseudorapidity; #eta^{leadlep}; Leptons", 30, -3, 3)
    if (name == "leadlep_E"):         return ROOT.TH1D("leadlep_E",        "Leading Lepton Energy; E^{leadlep} [GeV]; Leptons", 30, 0, 300)
    if (name == "leadlep_phi"):       return ROOT.TH1D("leadlep_phi",      "Leading Lepton Azimuthal Angle ; #phi^{leadlep}; Leptons", 32, -3.2, 3.2)
    if (name == "leadlep_charge"):    return ROOT.TH1D("leadlep_charge",   "Leading Lepton Charge; Q^{leadlep}; Leptons", 7, -1.75, 1.75)
    if (name == "leadlep_type"):      return ROOT.TH1D("leadlep_type",     "Leading Lepton PDG ID; PDGID^{leadlep}; Leptons", 61, -30.5, 30.5)
    if (name == "leadlep_ptcone30"):  return ROOT.TH1D("leadlep_ptcone30", "Leading Lepton Transverse Momentum Isolation; ptcone30^{leadlep}; Leptons", 30, -4.5, 10.5)
    if (name == "leadlep_etcone20"):  return ROOT.TH1D("leadlep_etcone20", "Leading Lepton Transverse Energy Isolation; etcone20^{leadlep}; Leptons", 30, -4.5, 10.5)
    if (name == "leadlep_z0"):        return ROOT.TH1D("leadlep_z0",       "Leading Lepton z0 impact parameter; z_{0}^{leadlep}; Leptons", 20, -1, 1)
    if (name == "leadlep_d0"):        return ROOT.TH1D("leadlep_d0",       "Leading Lepton d0 impact parameter; d_{0}^{leadlep}; Leptons", 20, -1, 1)

    if (name == "traillep_pt"):       return ROOT.TH1D("traillep_pt",       "Trailing Lepton Transverse Momentum;p_{T}^{traillep};Leptons", 20, 0, 200)
    if (name == "traillep_eta"):      return ROOT.TH1D("traillep_eta",      "Trailing Lepton Pseudorapidity; #eta^{traillep}; Leptons", 30, -3, 3)
    if (name == "traillep_E"):        return ROOT.TH1D("traillep_E",        "Trailing Lepton Energy; E^{traillep} [GeV]; Leptons", 30, 0, 300)
    if (name == "traillep_phi"):      return ROOT.TH1D("traillep_phi",      "Trailing Lepton Azimuthal Angle ; #phi^{traillep}; Leptons", 32, -3.2, 3.2)
    if (name == "traillep_charge"):   return ROOT.TH1D("traillep_charge",   "Trailing Lepton Charge; Q^{traillep}; Leptons", 7, -1.75, 1.75)
    if (name == "traillep_type"):     return ROOT.TH1D("traillep_type",     "Trailing Lepton PDG ID; PDGID^{traillep}; Leptons", 61, -30.5, 30.5)
    if (name == "traillep_ptcone30"): return ROOT.TH1D("traillep_ptcone30", "Trailing Lepton Transverse Momentum Isolation; ptcone30^{traillep}; Leptons", 30, -4.5, 10.5)
    if (name == "traillep_etcone20"): return ROOT.TH1D("traillep_etcone20", "Trailing Lepton Transverse Energy Isolation; etcone20^{traillep}; Leptons",   30, -4.5, 10.5)
    if (name == "traillep_z0"):       return ROOT.TH1D("traillep_z0",       "Trailing Lepton z0 impact parameter; z_{0}^{traillep}; Leptons", 20, -1, 1)
    if (name == "traillep_d0"):       return ROOT.TH1D("traillep_d0",       "Trailing Lepton d0 impact parameter; d_{0}^{traillep}; Leptons", 20, -1, 1)
    return None