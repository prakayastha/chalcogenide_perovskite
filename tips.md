This is a file I am creating to keep a note of all the things I have learnt through the course of this project. As a tips and tricks. 

# I love symmetry hence I love symmetry constrained relaxation!
- The symmetry constrained relaxation feature in FHI-aims is a feature I have been loving so much. Not only does it ensure the symmetry of your crystal remain pefect throughout the calculation, it also makes sure that space group symmetries are accounted for when you do finite displacement calculations on your system. 
- The band structures, both electronic and phonon, loose symmetry due to small numerical noise when you fully relax. The band structures look very neat when you contrain the calculation. 
- If you fully relax, the symmetry is lowered and if you plot the bandstructure on the original symmetry path, you might see kinks or "funny" looking dispersion. The reason is inaccurate symmetry
- When you fully relax your system, even with tight settings some noise seeps in the lattice coordinates and breaks the symmetry of the system. This can alter the electronic as well as phonon bandstructure of the system. 
- Unless required by a problem specifically, I don't see myself using a full relax feature at all. 
# Check your AFLOW generated FHI-aims input file!
- While the AFLOW toolkit for making geometry files with parametric constraints is extremely useful, it is not a click and go. There is no free lunch. The parameters given from the aflow output make sense formally, but do not take into account the periodicity of the atoms in the unit cell. One needs to map the parameters of the atoms back into the unit cell. Many thanks to Tom Purcell on the FHI-aims slack channel for helping me figure this out. I was stuck on this problem for weeks.  
# IR/Raman spectra
- One quick shortcut to generating Born effective charge tensor is to try Mulliken/Badar charges. These are scalar so the tensor then becomes diagonal with all same elements. Its quick and provides a rough estimates for dry runs. 
