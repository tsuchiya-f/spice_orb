import spiceypy as spice

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='/Users/Shared/spice/'):

    # load SPK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/SPK/
    spice.furnsh(source_dir + 'vex/kernels/spk/DE405.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/EARTHSTNS_FX_050714.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/EARTHSTNS_ITRF93_050714.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/ESTRACK_V03.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/ORVM_T19___________00001.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/OUTERPLANETS_V0003.BSP')
    spice.furnsh(source_dir + 'vex/kernels/spk/VEX_STRUCT_V01.BSP')

    # load FK
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vco-v-spice-6-v1.0/vcosp_1000/data/fk/
    spice.furnsh(source_dir + 'vex/kernels/fk/rssd0002.tf')
    spice.furnsh(source_dir + 'vex/kernels/fk/vco_spacecraft_v26.tf')

    # load LSK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/LSK/
    spice.furnsh(source_dir + 'vex/kernels/lsk/NAIF0011.TLS')

    # load PCK 
    # https://naif.jpl.nasa.gov/pub/naif/pds/data/vex-e_v-spice-6-v2.0/vexsp_2000/DATA/PCK/
    spice.furnsh(source_dir + 'vex/kernels/pck/PCK00010.TPC')

    return