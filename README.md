# Chalcogenide perovskites

This is a project website for my chalcogenide perovskite project, that I am carrying out during the first year of my PhD. 

This project is a collaborative experimental + computational project which aims to carry out vibrational spectraoscopy on materials that are part of the systhesis of the BaZrS<sub>3</sub> perovskite. 

Some background on this project are following:

Pb-based perovskites has performed well for photovoltaics applications. However, the Pb introduces questions about toxicity in the solar cells, and there is a search for new materials that could perform just as well but not be as toxic. MAPI and FAPI (some of the best performing perovskites in efficiencies) have also been shown instability due to environmental conditions. Chalogenide-based perovskites are making a new wave of non Pb-based perovkite studies for photovoltaic applications. One of the chalcogenide-based perovksite that has gained a lot of atthention is the BaZrS<sub>3</sub> material. It has been reported in the Pnma space group at room temperature in literature. For photovolatic applications, this material must be deposited to make the device. Zr has a high boiling point, which makes low temperature synthesis difficult. Giulia (our experimental collaborator) is carrying out two different techniques to perform this thin film synthesis at low temperature. One of them is the ball milling method and the other is the hot injection method. These are teachniques which will enable in depositing a BaZrS<sub>3</sub> aborber layer on the device. However, while carrying out both these techniques, it is difficult to "follow the reaction" and determine which phases have formed in it's course. 

Methods:

The idea of this project is to model competing ternary phases of the perovskite and binary phases of the BaS and ZrS<sub>2</sub> salts. The competing phases are determined through convex hulls/Gibbs' triangle available on online databases. The structures of these phases are then relaxed with FHI-aims and an electronic BS and phonon BS is done. With the harmonic phonon force constants, along with Born effective charges and dielectric constants, the peak positions of the IR/Raman spectra can be extracted. This is done via the Phonopy-Spectroscopy code, and writing the FHI-aims interface for it is part of this project. A further third-order phonon calculation has to be performed to extract the peak widths of the system. 

An electronic structure analysis is also done with bangaps from PBEsol and HSE06, with and without spin-orbit coupling to check for relativitic effects. The density of states are also plotted to comment on bonding of different phases. 

Expected outcomes:

The DFT predicted IR/Raman spectra of BaSrZ3 along with its competing binary and ternary phases will give an indication of changes during the reaction process which can then be matched with the experimental IR spectra. 


The website can be found here: https://prakayastha.github.io/chalcogenide_perovskite/

NOTE: This website is currently created to display the electronic and phonon band structures at the IOP Advances in Photovoltaics conference. As this project progresses, I will add more details like the IR/Raman spectra from DFT and experiment and our final results. 
