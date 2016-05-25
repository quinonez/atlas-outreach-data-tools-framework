import argparse
import sys
import os
import glob
import ROOT
import importlib
import Analysis.Job as Job
import Analysis.Disclaimer as DC
from multiprocessing import Pool 


# configuration = None

def BuildJob(configuration, processName, fileLocation):
    configuration["Batch"] = True
    job = Job.Job(processName, configuration, fileLocation )
    return job


def SortJobsBySize(jobs):  
    def jobSize(job):
        return sum([os.lstat(f).st_size for f in job.InputFiles])
    return sorted(jobs, key=jobSize, reverse=True)

def RunJob(job):
    job.run()

 
#======================================================================
def main( argv ):
    """
    Main function to be executed when starting the code.
    """
    DC.printDisclaimer()
    
    # global configuration
    parser = argparse.ArgumentParser( description = 'Analysis Tool using XMLs' )
    parser.add_argument('-n', '--nWorkers',   default=4,                                 type=int,   help='number of workers' )  
    parser.add_argument('-p', '--parallel',   default=False,   action='store_const',     const=True, help='enables running in parallel')
    parser.add_argument('-c', '--configfile', default="Configurations/Configuration.py", type=str,   help='files to be analyzed')
    args = parser.parse_args()
    
    configModuleName = args.configfile.replace("/", ".").strip(".py")
    configuration = importlib.import_module(configModuleName)
  
    if not os.path.exists(configuration.Job["OutputDirectory"]):
        os.makedirs(configuration.Job["OutputDirectory"])

    if (args.parallel):
        jobs = [BuildJob(configuration.Job, processName, fileLocation) for processName, fileLocation in configuration.Processes.items()]
        jobs = SortJobsBySize(jobs)
        pool = Pool(processes=args.nWorkers)              # start with n worker processes
        pool.map(RunJob, jobs, chunksize=1)

    else:
        for processName, fileLocation in configuration.Processes.items():
            RunJob(BuildJob(configuration.Job, processName, fileLocation))      
  
#======================================================================   
if __name__ == "__main__":
    """
    Here the code should appear that is executed when running the plotter directly
    (and not import it in another python file via 'import Plotter')
    """
   
    main( sys.argv[1:] )

