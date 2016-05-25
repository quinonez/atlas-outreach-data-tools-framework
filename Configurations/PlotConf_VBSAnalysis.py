config = {
"Luminosity": 1000,
"InputDirectory": "results",

"Histograms" : {
    "JetInvMass"        : {},
    "etmiss"            : {},
    "vxp_z"             : {},
    "pvxp_n"            : {},
    "lep_n"             : {},
    "leadlep_pt"        : {},
    "leadlep_eta"       : {},
    "leadlep_E"         : {},
    "leadlep_phi"       : {},
    "leadlep_charge"    : {"y_margin" : 0.5},
    "leadlep_type"      : {},
    "leadlep_ptcone30"  : {},
    "leadlep_etcone20"  : {},
    "leadlep_z0"        : {},
    "leadlep_d0"        : {},
    "traillep_pt"       : {},
    "traillep_eta"      : {},
    "traillep_E"        : {},
    "traillep_phi"      : {},
    "traillep_charge"   : {"y_margin" : 0.5},
    "traillep_type"     : {},
    "traillep_ptcone30" : {},
    "traillep_etcone20" : {},
    "traillep_z0"       : {},
    "traillep_d0"       : {},
    "n_jets"            : {},
    "jet_pt"            : {},
    "jet_m"             : {},
    "jet_jvf"           : {},
    "jet_eta"           : {},
    "jet_MV1"           : {},
},

"Paintables": {
    "Stack": {
        "Order": ["WW", "Diboson", "DrellYan", "W", "stop", "ttbar"],
        "Processes" : {                
            "WW" : {
                "Color"         : "#fa7921",
                "Contributions" : ["WW"]},

            "Diboson" : {
                "Color"         : "#086788",
                "Contributions" : ["WW", "WZ", "ZZ"]},
                                
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