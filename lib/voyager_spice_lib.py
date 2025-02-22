import spiceypy as spice

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='/Users/Shared/spice/'):

    # load SPK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/
    spice.furnsh(source_dir + 'generic_kernels//spk/planets/de442s.bsp')

    # https://naif.jpl.nasa.gov/pub/naif/VOYAGER/kernels/spk/
    spice.furnsh(source_dir + 'voyagers/kernels/spk/Voyager_1.a54206u_V0.2_merged.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/Voyager_2.m05016u.merged.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/sat337.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr1_jup230.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr1_sat337.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr1.x2100.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr2_jup230.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr2_nep097.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr2_sat337.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr2.ura182.bsp')
    spice.furnsh(source_dir + 'voyagers/kernels/spk/vgr2.x2100.bsp')

    # load FK
    # https://naif.jpl.nasa.gov/pub/naif/VOYAGER/kernels/fk/
    spice.furnsh(source_dir + 'voyagers/kernels/fk/vg1_v02.tf')
    spice.furnsh(source_dir + 'voyagers/kernels/fk/vg2_v02.tf')

    # load LSK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/
    spice.furnsh(source_dir + 'generic_kernels/lsk/naif0012.tls')

    # load PCK 
    # https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/
    spice.furnsh(source_dir + 'generic_kernels/pck/pck00011.tpc')

    return