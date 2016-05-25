config = {
"Luminosity": 1000,
"InputDirectory": "results",

"Histograms" : {
    "WtMass"          : {},
    "etmiss"          : {},
    "lep_pt"          : {},
    "lep_eta"         : {},
    "lep_E"           : {},
    "lep_phi"         : {},
    "lep_charge"      : {"y_margin" : 0.5},
    "lep_type"        : {},
    "lep_ptcone30"    : {},
    "lep_etcone20"    : {},
    "n_jets"          : {},
    "jet_pt"          : {},
    "jet_m"           : {},
    "jet_jvf"         : {},
    "jet_eta"         : {},
    "jet_MV1"         : {},
    "vxp_z"           : {},
    "pvxp_n"          : {},
},

"Paintables": {
    "Stack": {
        "Order": ["Diboson", "DrellYan", "W", "Z", "stop", "ttbar"],
        "Processes" : {                
            "Diboson" : {
                "Color"         : "#fa7921",
                "Contributions" : ["WW", "WZ", "ZZ"]},
                                
            "DrellYan": {       
                "Color"         : "#5bc0eb",
                "Contributions" : ["DYeeM08to15", "DYeeM15to40", "DYmumuM08to15", "DYmumuM15to40", "DYtautauM08to15", "DYtautauM15to40"]},
            
            "W": {              
                "Color"         : "#e55934",
                "Contributions" : ["WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]},
                                
            "Z": {              
                "Color"         : "#086788",
                "Contributions" : ["Zee", "Zmumu", "Ztautau"]},
                  
            "stop": {
                "Color"         : "#fde74c",
                "Contributions" : ["stop_tchan_top", "stop_tchan_antitop", "stop_schan", "stop_wtchan"]},
            
            "ttbar": {
                "Color"         : "#9bc53d",
                "Contributions" : ["ttbar_lep", "ttbar_had"]}
        }
    },

    'ZPrime1000': {
        'Color'        : '#0000ff', 
        'Scale'        : 10,
        'Contributions': ['ZPrime1000']},

    'ZPrime500': {
        'Color'        : '#0099cc', 
        'Scale'        : 10,
        'Contributions': ['ZPrime500']},

    "data" : {
        "Contributions": ["data_Egamma", "data_Muons"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC", "Z`Ratio"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]},
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data", 'ZPrime1000', 'ZPrime500']},

        'Z`Ratio': {
            'type'       : 'Ratio',
            'Paintables' : ['ZPrime1000', 'ZPrime500']},
    }
},
}