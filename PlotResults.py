import argparse
import sys
import os
import glob
import ROOT
import Plotting.PlotStyle as PS
import Plotting.Paintable as Paintable
import Plotting.Depiction as Depiction
import Plotting.Database  as Database
import importlib
from collections import OrderedDict
 
def collectPaintables(definition):
    paintables = {}
    for key, item in definition.items():
        if   "Stack" in key: paintables["Stack"] = Paintable.StackPaintable("stack", definition["Stack"])
        elif "data"  in key: paintables["data"]  = Paintable.DataPaintable("data", definition["data"]) 
        else:                paintables[key]     = Paintable.OverlayPaintable(key, definition[key])
    return paintables

def collectDepictions(configuration):
    depictions = []
    definitions = configuration["Definitions"]
    for depiction in configuration["Order"]:
        if definitions[depiction]["type"] == "Main"     : depictions.append(Depiction.MainDepiction(      definitions[depiction], depiction))
        if definitions[depiction]["type"] == "Ratio"    : depictions.append(Depiction.RatioDepiction(     definitions[depiction], depiction))
        if definitions[depiction]["type"] == "Agreement": depictions.append(Depiction.AgreementDepiction( definitions[depiction], depiction))
    return depictions

def initializeDepictions(Depictions):
    n = len(Depictions)
    
    if n == 1:
        Depictions[0].initializeDepiction( 0.0, 0.0, 1.0, 1.0, 0.1, 0.1)        
    elif n == 2:
        Depictions[0].initializeDepiction( 0.0, 0.3, 1.0, 1.0, 0.1, 0.005)
        Depictions[1].initializeDepiction( 0.0, 0.0, 1.0, 0.3, 0.005, 0.1)

    elif n == 3:
        Depictions[0].initializeDepiction( 0.0,  0.4, 1.0,  1.0, 0.1, 0.005)
        Depictions[1].initializeDepiction( 0.0, 0.25, 1.0,  0.4, 0.01, 0.01)
        Depictions[2].initializeDepiction( 0.0,  0.0, 1.0, 0.25, 0.01, 0.1)

    else:
        print "Not Supported Yet"
        sys.exit()
    updateStyle(Depictions)

def updateStyle(Depictions):
    # last depiction determins the size for the x label
    bottomPad = Depictions[-1].pad
    bottomPad.SetBottomMargin(0.1/bottomPad.GetAbsHNDC())
    ROOT.gStyle.SetTitleXOffset(1.5/bottomPad.GetAbsHNDC())

def DrawPlot(configuration, histlocation):
    canvas = ROOT.TCanvas( histlocation, "title", 900, 900 )
    
    Paintables = collectPaintables(configuration["Paintables"])
    Depictions = collectDepictions(configuration["Depictions"])
    initializeDepictions(Depictions)

    Depictions[0].drawDepiction(Paintables)    
    for i in range(1, len(Depictions)):
        Depictions[i].drawDepiction(Paintables)
    canvas.SaveAs("Output/" + histlocation+ ".pdf")  
 
#======================================================================
def main( argv ):
  """
  Main function to be executed when starting the code.
  """
  ROOT.gROOT.SetBatch()
  ROOT.TH1.AddDirectory(False)
  PS.setStyle();

  parser = argparse.ArgumentParser( description = 'Plotting Tool using YAML files for configuration' )
  parser.add_argument('configfile', type=str, help='configuration file to be used')
  args = parser.parse_args()

  configModuleName = args.configfile.replace("/", ".").strip(".py")
  configuration = importlib.import_module(configModuleName).config

  for histogram in configuration["Histograms"]:
    Database.UpdateDataBase(configuration, histogram)
    DrawPlot(configuration, histogram)
    
#======================================================================   
if __name__ == "__main__":
  """
  Here the code should appear that is executed when running the plotter directly
  (and not import it in another python file via 'import Plotter')
  """

  # start main program    
  main( sys.argv[1:] )

  
#======================================================================   
