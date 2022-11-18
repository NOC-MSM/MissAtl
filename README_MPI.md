# Shelf Enabled Global NEMO (SE-NEMO): MPI variations

The setup script has been tested and will checkout, compile and run the ORCA025 (NEMO 4.0.4) code on ARCHER2 for three versions of MPI: Cray-MPICH, MPICH4 and openMPI.

## Quick Start:

```
git clone git@github.com:NOC-MSM/SE-NEMO.git

MPI_OPT='mpich4' # other options are mpich | ompi

./SE-NEMO/scripts/setup/se-eORCA025_setup -w $PWD/test_deploy_$MPI_OPT -x $PWD/test_deploy_$MPI_OPT -s $PWD/cfgs/SE-NEMO -m archer2 -a $MPI_OPT
cd test/nemo/cfgs/se-eORCA025/
cp -rP EXPREF EXP_MYRUN
cd EXP_MYRUN
ln -s INPUTS/domain_cfg_r018-010-010_glo-r018-010_ant_opt_v3_notaper.nc domain_cfg.nc # terrain following case (MES)
# alternativly use INPUTS/domcfg_eORCA025_v2.nc for the geopotential vertical coordinate (ZPS) case
```
Edit the project code and options in  `runscript.[slurm|mpirun]` then:
```
sbatch runscript.[slurm|mpirun] # at present openMPI uses the .mpirun script
```
This will produce a 5 day mean output from the beginning of 1976. The run should take 15 minutes to complete once in the machine.

### Forcing data:

[SE-ORCA025](http://gws-access.ceda.ac.uk/public/jmmp_collab/)

_this is automatically transferred when the setup script is executed_

For ARCHER2 users these data are held under `/work/n01/shared/senemo` and `/work/n01/shared/nemo/FORCING` and are linked during the setup.

### Current issue:

At higher core counts NEMO/XIOS are not running. The thought is that it may be linked to the Cray-MPICH installation, so other MPI setups are being explored. Below is a summary of current progress.

_core count vs MPI_

|  MES    | MPICH                      | MPICH4                           | OMPI|
| :----:  |  :----:                    |   :----:                         |:----:  |
| 1516    |  Runs                      | Hangs @ dia_ptr_init<sup>2</sup> ||
| 6376    |  Hangs in XIOS<sup>1</sup> | Hangs @ dia_ptr_init<sup>2</sup> ||
| 8448    |  Hangs in XIOS<sup>1</sup> | Hangs @ dia_ptr_init<sup>2</sup> ||

|  ZPS    | MPICH | MPICH4    | OMPI|
| :----:        |    :----:   |   :----:  |:----:  |
|1516     |       |    ||
| 6376   |        |      ||
| 8448   |         |      ||

Notes:

<sup>1</sup> If the number of outputs is reduced in the `file*.xml` files then the simulation runs. It is thought this is linked to a known bug in MPICH3 which Cray-MPICH is built on.

<sup>2</sup> At the moment it's unclear as to whether this is a NEMO issue or MPI issue.