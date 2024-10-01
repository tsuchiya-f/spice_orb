import spiceypy as spice

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='C:/share/Linux/doc/spice/'):

    # load spice kernel files
    spice.furnsh(source_dir + 'juno/juno_rec_orbit.bsp')
#    spice.furnsh(source_dir + 'juno/juno_pred_orbit.bsp')

    spice.furnsh(source_dir + 'juice/kernels/spk/jup365_19900101_20500101.bsp')
    spice.furnsh(source_dir + 'juice/kernels/spk/de432s.bsp')
    spice.furnsh(source_dir + 'juice/kernels/lsk/naif0012.tls')
    spice.furnsh(source_dir + 'juice/kernels/pck/pck00011.tpc')

    return