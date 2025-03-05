import spiceypy as spice
import os

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='/Users/Shared/spice/'):

    # load SPK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/
    spice.furnsh(source_dir + 'generic_kernels/spk/planets/de442s.bsp')

    # https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/
    spice.furnsh(source_dir + 'cassini/kernels/spk/171215R_SCPSEops_97288_17258.bsp')
    #spice.furnsh(source_dir + 'cassini/kernels/spk/180628RU_SCPSE_04183_17258.bsp')

    # load FK

    # load LSK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/
    spice.furnsh(source_dir + 'generic_kernels/lsk/naif0012.tls')

    # load PCK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/
    spice.furnsh(source_dir + 'generic_kernels/pck/pck00011.tpc')

    return