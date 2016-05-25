import ROOT

import Analysis
import AnalysisHelpers as AH

#======================================================================
 
class VBSAnalysis(Analysis.Analysis):
  """Vector Boson Analysis searching for events with a WW pair decaying to two leptons of same charge and two
  high energetic jets.
  """
  def __init__(self, store):
    super(VBSAnalysis, self).__init__(store)
    
  def initialize(self):
      self.hist_invMass         = self.addHistogram("JetInvMass", ROOT.TH1D("JetInvMass", "dijet invariant mass;M_{jj} [GeV]; Events", 10, 0,1000))

      self.hist_leptn           =  self.addStandardHistogram("lep_n")

      self.hist_leadleptpt      =  self.addStandardHistogram("leadlep_pt")
      self.hist_leadlepteta     =  self.addStandardHistogram("leadlep_eta")
      self.hist_leadleptE       =  self.addStandardHistogram("leadlep_E")
      self.hist_leadleptphi     =  self.addStandardHistogram("leadlep_phi")
      self.hist_leadleptch      =  self.addStandardHistogram("leadlep_charge")
      self.hist_leadleptID      =  self.addStandardHistogram("leadlep_type")
      self.hist_leadleptptc     =  self.addStandardHistogram("leadlep_ptcone30")
      self.hist_leadleptetc     =  self.addStandardHistogram("leadlep_etcone20")
      self.hist_leadlepz0       =  self.addStandardHistogram("leadlep_z0")
      self.hist_leadlepd0       =  self.addStandardHistogram("leadlep_d0")

      self.hist_trailleptpt     =  self.addStandardHistogram("traillep_pt")
      self.hist_traillepteta    =  self.addStandardHistogram("traillep_eta")
      self.hist_trailleptE      =  self.addStandardHistogram("traillep_E")
      self.hist_trailleptphi    =  self.addStandardHistogram("traillep_phi")
      self.hist_trailleptch     =  self.addStandardHistogram("traillep_charge")
      self.hist_trailleptID     =  self.addStandardHistogram("traillep_type")
      self.hist_trailleptptc    =  self.addStandardHistogram("traillep_ptcone30")
      self.hist_trailleptetc    =  self.addStandardHistogram("traillep_etcone20")
      self.hist_traillepz0      =  self.addStandardHistogram("traillep_z0")
      self.hist_traillepd0      =  self.addStandardHistogram("traillep_d0")
 
      self.hist_njets           =  self.addStandardHistogram("n_jets")       
      self.hist_jetspt          =  self.addStandardHistogram("jet_pt")       
      self.hist_jetm            =  self.addStandardHistogram("jet_m")        
      self.hist_jetJVF          =  self.addStandardHistogram("jet_jvf")      
      self.hist_jeteta          =  self.addStandardHistogram("jet_eta")      
      self.hist_jetmv1          =  self.addStandardHistogram("jet_MV1")      

      self.hist_etmiss          = self.addStandardHistogram("etmiss")
      self.hist_vxp_z           = self.addStandardHistogram("vxp_z")
      self.hist_pvxp_n          = self.addStandardHistogram("pvxp_n")

  def analyze(self):
      # retrieving objects
      eventinfo = self.Store.getEventInfo()
      weight = eventinfo.scalefactor()*eventinfo.eventWeight() if not self.getIsData() else 1
      self.countEvent("no cut", weight)
      
      # apply standard event based selection
      if not AH.StandardEventCuts(eventinfo): return False
      self.countEvent("EventCuts", weight)

      # Lepton Requirements
      goodLeptons = AH.selectAndSortContainer(self.Store.getLeptons(), AH.isGoodLepton, lambda p: p.pt())
      if not (len(goodLeptons) == 2): return False
      self.countEvent("2 high pt Leptons", weight)

      leadLepton =  goodLeptons[0]
      trailLepton = goodLeptons[1]

      if not (leadLepton.charge() * trailLepton.charge() > 0): return False
      if not (abs(leadLepton.pdgId()) != abs(trailLepton.pdgId())): return False

 
      goodJets = AH.selectAndSortContainer(self.Store.getJets(), AH.isGoodJet, lambda p: p.pt())
      if not len(goodJets) >= 2: return False
      self.countEvent("Jets", weight)
           
      
      # Vertex Histograms
      self.hist_vxp_z.Fill(eventinfo.primaryVertexPosition(), weight)
      self.hist_pvxp_n.Fill(eventinfo.numberOfVertices(), weight)
      
      # Missing Et Histograms
      etmiss    = self.Store.getEtMiss()
      self.hist_etmiss.Fill(etmiss.et(),weight)
      
      #Lepton Histograms
      self.hist_leptn.Fill(len(goodLeptons), weight)
      
      # Leading Lepton Histograms
      self.hist_leadleptpt.Fill(leadLepton.pt(), weight)
      self.hist_leadlepteta.Fill(leadLepton.eta(), weight)
      self.hist_leadleptE.Fill(leadLepton.e(), weight)
      self.hist_leadleptphi.Fill(leadLepton.phi(), weight)
      self.hist_leadleptch.Fill(leadLepton.charge(), weight)
      self.hist_leadleptID.Fill(leadLepton.pdgId(), weight)
      self.hist_leadleptptc.Fill(leadLepton.isoptcone30(), weight)
      self.hist_leadleptetc.Fill(leadLepton.isoetcone20(), weight)
      self.hist_leadlepz0.Fill(leadLepton.z0(), weight)
      self.hist_leadlepd0.Fill(leadLepton.d0(), weight)
      
      # Trailing Lepton Histograms
      self.hist_trailleptpt.Fill(trailLepton.pt(), weight)
      self.hist_traillepteta.Fill(trailLepton.eta(), weight)
      self.hist_trailleptE.Fill(trailLepton.e(), weight)
      self.hist_trailleptphi.Fill(trailLepton.phi(), weight)
      self.hist_trailleptch.Fill(trailLepton.charge(), weight)
      self.hist_trailleptID.Fill(trailLepton.pdgId(), weight)
      self.hist_trailleptptc.Fill(trailLepton.isoptcone30(), weight)
      self.hist_trailleptetc.Fill(trailLepton.isoetcone20(), weight)
      self.hist_traillepz0.Fill(trailLepton.z0(), weight)
      self.hist_traillepd0.Fill(trailLepton.d0(), weight)
      
      # Jet Histograms
      leadJet =  goodJets[0]
      trailJet = goodJets[1]
      self.hist_njets.Fill(len(goodJets), weight)
      [self.hist_jetm.Fill(jet.m(), weight) for jet in goodJets]
      [self.hist_jetspt.Fill(jet.pt(), weight) for jet in goodJets]
      [self.hist_jetJVF.Fill(jet.jvf(), weight) for jet in goodJets]
      [self.hist_jeteta.Fill(jet.eta(), weight) for jet in goodJets]
      [self.hist_jetmv1.Fill(jet.mv1(), weight) for jet in goodJets]
      
      # dijet histograms
      self.hist_invMass.Fill((leadJet.tlv() + trailJet.tlv()).M(), weight)      
      return True
      
  def finalize(self):
      pass