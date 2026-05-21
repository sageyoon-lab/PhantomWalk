# PhantomWalk
Polymer system initialization workflow that utilizes a random walk and dissipative particle dynamics as a soft push potential.

## Environment

Build a software environment using the `environment.yml` file and the command ```conda env create -f environment.yml```

## Examples
1 - Run a dpd simulation and check the bond lengths and inter-particle distances.
2 - Run a dpd simulation with an energy stabilization cutoff. Write out simulation to trajectory file.
3 - Run a dpd simulation with option for angles and dihedrals. Write out to trajectory file. Start a Lennard-Jones WCA simulation with optional angles and dihedrals.
4 - Replace the random walk in the DPD workflow with mbuild self-avoiding random walk.
5 - Run DPD on a rigid body model used for anisotropic coarse-graining. Based on flowerMD classes.

## signac
These files are meant to be utilized on supercomputers to run parallel simulations of this workflow. 

