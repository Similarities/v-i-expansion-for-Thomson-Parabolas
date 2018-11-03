# v(max)^i-expansion-for-fast ions (Thomson spectrometer)
Thomson Parabola maximum cutoff energy expansion for succesive charge states. 
_______________________________________________________________________________
# heavy ions 
# particle acceleration
# laser accelerated ions
# Thomson Spectrometer


Laser accelerated ions appear in successive charge states (usually positively charged). The acceleration mechanism highly depends on the ion's charge state (charge to mass number: Z/A). Hence, the maximum kinetic energy of ions with succesive charge states allows us to derive information about the underlying force, meaning the Ekin(max) to (Z/A)^i scaling factor. 
This question arises in the special case of symmetries in the maximum (minimum) kinetic energies of accelerated ions with same mass number at successive charge states. (https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.124801)

The fast ions travelled through a Thomson spectrometer (static E and B field) and are dispersed according to their velocity and Z/A.  The detector usually a Multi-channel-plate (MCP) is imaged with a camera from which the magnification factor is needed. 
 
'''''''''''''''''''''''''
This evaluation software displays an expansion of the velocity ( v(max)=Sum (k0 + k1*v*Z/A + k2*v0*(Z)^2/A + k3*v0*(Z)^3/A + k4*v0*(Z^4)/A, where v0 is 10^7 m/s and is treated in the following as a function of (Z^i/A).  Here, ki terms denote constants that have to be given in the input. k0 in particulare denotes a constant velocity that is independent of the Z/A scaling. Usual parameters that fit to example picture: 
K0: 0.1,
K1: 0,
K2: 0.16,
K3: 0,
K4: -0.000038.
-----------------------------------------------
In the code various constant for experimental parameter are given to determine the spectrometer function. So far, the code
is only in def not OOD. Since usual polynom fitting routines do only lead to an multi-power expansion without e.g. symmetry reasonings or other restrictions, this approach found a solution that delivers a high accuracy in the reproduction of the experimental results with a very low number of expansion power. This leads to a much better understanding of the analytical function for the data and revealed new physical content.
Details can be found in https://depositonce.tu-berlin.de/handle/11303/6149.




