config = {
"Luminosity": 1000,
"InputDirectory": "results",

"Histograms" : {
    "WtMass"          : {"rebin": 2},
    "invMass"         : {"rebin": 2},
    "lep_n"           : {},
    "lep_pt"          : {"rebin": 2},
    "lep_eta"         : {"rebin": 2},
    "lep_E"           : {"rebin": 2},
    "lep_phi"         : {"rebin": 2},
    "lep_charge"      : {"y_margin" : 0.5},
    "lep_type"        : {"rebin": 2},
    "lep_ptcone30"    : {"rebin": 2},
    "lep_etcone20"    : {"rebin": 2},
    "vxp_z"           : {"rebin": 2},
    "pvxp_n"          : {"rebin": 2},
},

"Paintables": {
    "Stack": {
        "Order": ["WZ", "Diboson", "DrellYan", "W", "stop", "ttbar"],
        "Processes" : {                
            "WZ" : {
                "Color"         : "#fa7921",
                "Contributions" : ["WZ"]},

            "Diboson" : {
                "Color"         : "#086788",
                "Contributions" : ["WW", "ZZ"]},
                                
            "DrellYan": {       
                "Color"         : "#5bc0eb",
                "Contributions" : ["DYeeM08to15", "DYeeM15to40", "DYmumuM08to15", "DYmumuM15to40", "DYtautauM08to15", "DYtautauM15to40", "Zee", "Zmumu", "Ztautau"]},
            
            "W": {              
                "Color"         : "#e55934",
                "Contributions" : ["WenuJetsBVeto", "WenuWithB", "WenuNoJetsBVeto", "WmunuJetsBVeto", "WmunuWithB", "WmunuNoJetsBVeto", "WtaunuJetsBVeto", "WtaunuWithB", "WtaunuNoJetsBVeto"]},
                  
            "stop": {
                "Color"         : "#fde74c",
                "Contributions" : ["stop_tchan_top", "stop_tchan_antitop", "stop_schan", "stop_wtchan"]},
            
            "ttbar": {
                "Color"         : "#9bc53d",
                "Contributions" : ["ttbar_lep", "ttbar_had"]}
        }
    },

    "data" : {
        "Contributions": ["data_Egamma", "data_Muons"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]
        },
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data"]
        },
    }
},
}