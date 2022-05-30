# Shelf Enabled Global NEMO (SE-NEMO)

Thisse - the setup script has been tested and will checkout, compile and run the ORCA025 (NEMO 4.0.4) code on ARCHER, but namelists and forcing files are yet to be configured for the 'Shelf Enabled' part_**

Configuration files for SE-NEMO project


Base Configuration: GO8p6 at NEMO 4.0.4

## Quick Start:

```
git clone git@github.com:NOC-MSM/SE-NEMO.git
./SE-NEMO/scripts/setup/se-orca025_setup -w $PWD/test -x $PWD/test -s $PWD/SE-NEMO
cd test/nemo/cfgs/se-orca025/
cp -rP EXPREF EXP_MYRUN
cd EXP_MYRUN
ln -s ../EXP00/nemo nemo
ln -s 
```
Edit the project code and options in  `runscript.slurm` then:
```
sbatch runscript.slurm
```
This will produce a 5 day mean output from the beginning of 1976. The run should take 15 minutes to complete once in the machine.

### Forcing data:

[SE-ORCA025](http://gws-access.ceda.ac.uk/public/jmmp_collab/)

_this is automatically transferred when the setup script is executed_

### Outputs:

On JASMIN: /gws/nopw/j04/class_vol2/senemo

### Important:

The `MY_SRC_GO8_FROZEN` directory should only contain the re-ROSEd code from G08. If editing any of these routines, copy the file from `MY_SRC_GO8_FROZEN` to `MY_SRC` and edit it there. The build process will copy the contents of `MY_SRC_GO8_FROZEN` to `cfgs/se-nemo/MY_SRC` before copying `MY_SRC` to `cfgs/se-nemo/MY_SRC`. Any files with the same name will be overwritten.
