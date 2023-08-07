#!/bin/bash
#SBATCH --job-name=SE-ZIP
#SBATCH --time=24:00:00
#SBATCH --account=n01-CLASS
#SBATCH --partition=serial
#SBATCH --qos=serial

. XXX_ENV_XXX/gnu-mpich
export LD_LIBRARY_PATH=${CRAY_LD_LIBRARY_PATH}:${LD_LIBRARY_PATH}
export OMP_NUM_THREADS=1

if [ -z OUTPUTS_ZIP ]
then
	mkdir OUTPUTS_ZIP
fi

cd OUTPUTS

for i in *
do
	nccopy -4 -d 1 -c x/64,y/64 $i ../OUTPUTS_ZIP/$i
done

