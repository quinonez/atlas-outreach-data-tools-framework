config = {
'InputDirectory': 'results',
'Luminosity': 1000,

'Histograms': {
    'deltaphill'         : {},
    'etmiss'             : {},
    'leadlep_E'          : {},
    'leadlep_charge'     : {"y_margin" : 0.5},
    'leadlep_d0'         : {},
    'leadlep_eta'        : {},
    'leadlep_etcone20'   : {},
    'leadlep_phi'        : {},
    'leadlep_pt'         : {},
    'leadlep_ptcone30'   : {},
    'leadlep_type'       : {},
    'leadlep_z0'         : {},
    'ptll'               : {},
    'pvxp_n'             : {},
    'traillep_E'         : {},
    'traillep_charge'    : {"y_margin" : 0.5},
    'traillep_d0'        : {},
    'traillep_eta'       : {},
    'traillep_etcone20'  : {},
    'traillep_phi'       : {},
    'traillep_pt'        : {},
    'traillep_ptcone30'  : {},
    'traillep_type'      : {},
    'traillep_z0'        : {},
    'vismass'            : {},
    'vxp_z'              : {},
},

'Paintables': {
    'Stack': {
        "Order"     : ["Diboson", "DrellYan", "W", "Z", "stop", "ttbar"],
        "Processes" : {
            'Diboson': {
                'Color'         : '#fa7921',
                'Contributions' : ['WW', 'WZ', 'ZZ']},
                                
            'DrellYan': {       
                'Color'         : '#5bc0eb',
                'Contributions' : ['DYeeM08to15', 'DYeeM15to40', 'DYmumuM08to15', 'DYmumuM15to40', 'DYtautauM08to15', 'DYtautauM15to40']},
            
            'W': {              
                'Color'         : '#e55934',
                'Contributions' : ['WenuJetsBVeto', 'WenuWithB', 'WenuNoJetsBVeto', 'WmunuJetsBVeto', 'WmunuWithB', 'WmunuNoJetsBVeto', 'WtaunuJetsBVeto', 'WtaunuWithB', 'WtaunuNoJetsBVeto']},
                                
            'Z': {              
                'Color'         : '#086788',
                'Contributions' : ['Zee', 'Zmumu', 'Ztautau']},
                  
            'stop': {
                'Color'         : '#fde74c',
                'Contributions' : ['stop_tchan_top', 'stop_tchan_antitop', 'stop_schan', 'stop_wtchan']},
            
            'ttbar': {
                'Color'         : '#9bc53d',
                'Contributions' : ['ttbar_lep', 'ttbar_had']}
            }
    },
                    
    'Higgs': {
        'Color': '#0000ff', 
        'Contributions': ['ggH125_WW2lep']},
                    
    'data' : {
        'Contributions': ['data_Egamma', 'data_Muons']}
},

'Depictions': {
    "Order"       : ["Main", "Data/MC", "S/B"],
    "Definitions" : {
      'Data/MC': {
          'type'       : 'Agreement',
          'Paintables' : ['data', 'Stack']},
      
      'Main': {
          'type'      : 'Main',
          'Paintables': ['Stack', 'data', 'Higgs']},
      
      'S/B': {
          'type'       : 'Ratio',
          'Paintables' : ['Higgs', 'Stack']},
      }
}
}