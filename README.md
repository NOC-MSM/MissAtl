# Shelf Enabled Global NEMO (SE-NEMO)

The setup script has been tested and will checkout, compile and run the ORCA025 (NEMO 4.0.4) code on ARCHER2 for three versions of MPI: Cray-MPICH, MPICH4 and openMPI. This branch is under development and will provide an option to compile the newer NEMO 4.2 code base.

Configuration files for SE-NEMO project

Base Configuration: GO8p6 at NEMO 4.0.4

## Quick Start for Mission Atlantic:

```
git clone git@github.com:NOC-MSM/SE-NEMO.git
./SE-NEMO/scripts/setup/se-eORCA025_setup -w $PWD/test -x $PWD/test -s $PWD/SE-NEMO -m archer2 -a mpich -c gnu
cd test/nemo/cfgs/se-eORCA025/
cp -rP EXPREF EXP_CNRM
cd EXP_CNRM
ln -s ../INPUTS/domcfg_eORCA025_v2.nc domain_cfg.nc # or whatever domain_cfg you are using
```
The scripts for running the different climate projection experiments are
CNRM-CM6-1HR historical period:
```
sbatch runscript_GS1p0_CNRM_hist.slurm
```

### Forcing data:

For ARCHER2 users these data are held under `/work/n01/shared/annkat` and are linked during the setup

