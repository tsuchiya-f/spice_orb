import spiceypy as spice

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='/Users/Shared/spice/'):

    # load SPK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/SPK/
    spice.furnsh(source_dir + 'vex/kernel/spk/DE405.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/EARTHSTNS_FX_050714.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/EARTHSTNS_ITRF93_050714.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/ESTRACK_V03.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/ORVM_T19___________00001.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/OUTERPLANETS_V0003.BSP')
    spice.furnsh(source_dir + 'vex/kernel/spk/VEX_STRUCT_V01.BSP')

    # load LSK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/LSK/
    spice.furnsh(source_dir + 'vex/kernel/lsk/NAIF0011.TLS')

    # load PCK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/PCK/
    spice.furnsh(source_dir + 'vex/kernel/pck/PCK00010.TPC')

    return