Read the preamble of the slurm file carefully.

You may want to change the following in the slurm file:

##############################################################################
# set name of job
#SBATCH --job-name=code  <-- give a name of your code. It's an identifier of the code you plan to run using this slurm file.
##############################################################################

Set the name of your output file (not the date file your code will save) and the error file
#To get error and output
#SBATCH --error=myRecord_error.err
#SBATCH --output=myRecord_output.out
##############################################################################
Set your email
# send mail to this address
#SBATCH --mail-user=youremail@umb.edu  <---- your email address goes here. 
##############################################################################

Load your modules and run the code

# Put your job commands here, including loading any needed
# modules.

module load python
python run-all-codes.py <--- the name the python code you want to run
##############################################################################

Play with the following to find the optimum combination

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
##############################################################################
