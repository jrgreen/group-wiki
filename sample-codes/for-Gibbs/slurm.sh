#!/bin/bash

# specify which shell to use.  Bash is recommended unless
# there is a compelling reason to use another.

# Sample slurm submission script for the Gibbs compute cluster
# Lines beginning with # are comments, and will be ignored by
# the interpreter.  Lines beginning with #SBATCH are directives
# to the scheduler.  These in turn can be commented out by
# adding a second # (e.g. ##SBATCH lines will not be processed
# by the scheduler).
#
#
# set name of job
#SBATCH --job-name=code
#

# set the number of nodes
#SBATCH -N8

# set the number of processes per node
#SBATCH -n 12 

#set an account to use
#if not used then default will be used
##SBATCH --account=scavenger

# set the number of GPU cards per node
# --gres=gpu[[:type]:count]
#SBATCH --gres=gpu:GTX980:2

#Or can use this
##SBATCH --gres=gpu:2


# set max wallclock time  DD-HH:MM:SS
#SBATCH --time=20-10:00:00


#To get error and output
#SBATCH --error=myRecord_error.err
#SBATCH --output=myRecord_output.out
#

#Optional
# set the partition where the job will run
##SBATCH --partition=GTX670

#Optional
# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=youremail@umb.edu


# Put your job commands here, including loading any needed
# modules.

module load python
python run-all-codes.py 
# module load <module_name>
# this job simply reports the hostname and sleeps for two minutes

#hostname
#sleep 120
