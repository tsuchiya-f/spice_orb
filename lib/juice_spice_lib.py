import numpy as np
import math
import spiceypy as spice
import datetime
#from planetary_coverage import MetaKernel

# ---------------------------------------------------------
# Load NAIF SPICE kernels for S/C
# ---------------------------------------------------------
def spice_ini(source_dir='C:/share/Linux/doc/spice/juice/kernels/'):

    # load spice kernel files
#    spice.furnsh(MetaKernel(source_dir + "mk/juice_plan.tm", kernels=source_dir))
    spice.furnsh(source_dir + "ck/juice_sc_crema_5_1_150lb_23_1_baseline_v03.bc")
#    spice.furnsh(source_dir + "ck/juice_sc_crema_5_1_150lb_default_v01.bc")
    spice.furnsh(source_dir + 'spk/juice_crema_5_1_150lb_23_1_v01.bsp')
    spice.furnsh(source_dir + 'spk/juice_orbm_000059_240817_240827_v01.bsp')
    spice.furnsh(source_dir + "spk/jup365_19900101_20500101.bsp")
    spice.furnsh(source_dir + 'spk/de432s.bsp')
    spice.furnsh(source_dir + 'lsk/naif0012.tls')
    spice.furnsh(source_dir + 'pck/pck00011.tpc')

    return

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   refernce target on the x-axis: x_ref
#   reference frame: ref
#   target: tar
#   origin: org
#   light time correction: corr
# ---------------------------------------------------------
def get_pos_xref(et, ref='IAU_SUN', tar='JUICE', org='SUN', x_ref='JUPITER', corr='LT+S'):

    # number of data
    nd = len(et)

    # get S/C orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    # spice temporal variable
    vec_z = [0.0, 0.0, 1.0]
    vec_org = [0.0, 0.0, 0.0]

    for i in range(0, nd):

        #Get state vector of S/C
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x_s = state[0]
        y_s = state[1]
        z_s = state[2]

        #Get state vector of reference target
        [state, lttime] = spice.spkezr(x_ref, et[i], ref, corr, org)
        x_r = state[0]
        y_r = state[1]
        z_r = state[2]

#        vec_x = [x_r, y_r, 0.0]
#        mout = spice.twovec(vec_x, 1, vec_z, 3)
#        vec_in = [x_s, y_s, z_s]
#        vec_out = spice.mxv(mout, vec_in)
        vec_x = [x_r, y_r, z_r]
        plane = spice.nvp2pl(vec_x, vec_org)
        vec_prj = spice.vprjp(vec_z, plane)

#        mout = spice.twovec(vec_x, 1, vec_z, 3)
        mout = spice.twovec(vec_x, 1, vec_prj, 3)
        vec_in = [x_s, y_s, z_s]
        vec_out = spice.mxv(mout, vec_in)

        x[i] = vec_out[0]
        y[i] = vec_out[1]
        z[i] = vec_out[2]
        r[i] = math.sqrt(x[i]**2+y[i]**2+z[i]**2)
        lat[i] = math.asin(z[i]/r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_SUN
#   target: JUICE
#   origin: SUN
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_sun(et, x_ref='JUPITER'):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref='IAU_SUN', tar='JUICE', org='SUN', x_ref=x_ref, corr='LT+S')

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_JUPITER
#   target: JUICE
#   origin: JUPITER
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_jup(et, x_ref='GANYMEDE'):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref='IAU_JUPITER', tar='JUICE', org='JUPITER', x_ref=x_ref, corr='LT+S')

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: IAU_EARTH
#   target: JUICE
#   origin: EARTH
#   refernce target on the x-axis: x_ref
# ---------------------------------------------------------
def get_juice_pos_earth(et, x_ref='SUN'):

    x, y, z, r, lat, lon = get_pos_xref(
        et, ref='IAU_EARTH', tar='JUICE', org='EARTH', x_ref=x_ref, corr='LT+S')

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate orbit
#   reference frame: ref
#   origin: org
#   target: tar
# ---------------------------------------------------------
def get_pos(et, ref='IAU_SUN', tar='JUICE', org='SUN'):

    # light time correction
    corr = 'LT+S'

    # number of data
    nd = len(et)

    # get S/C orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    for i in range(0, nd):

        # Get state vector of target
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x[i] = state[0]
        y[i] = state[1]
        z[i] = state[2]
        r[i] = math.sqrt(x[i]**2+y[i]**2+z[i]**2)
        lat[i] = math.asin(z[i]/r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]

# ---------------------------------------------------------
#   Calculate JUICE orbit
#   reference frame: ref
#   target: tar
#   origin: org
#   refernce target on the x-axis: x_ref
#   light time correction: corr
#
#   new reference frame for output position of this function
#   x : vector from the origin to the reference target
#   y : vector of the orbital direction of the reference target
# ---------------------------------------------------------
def get_pos_ref(et, ref='IAU_JUPITER', tar='JUICE', org='JUPITER', tar_ref='GANYMEDE', corr='LT+S'):

    # number of data
    nd = len(et)

    # get target orbit
    x = np.zeros(nd)
    y = np.zeros(nd)
    z = np.zeros(nd)
    r = np.zeros(nd)
    lat = np.zeros(nd)
    lon = np.zeros(nd)

    for i in range(0, nd):

        #Get state vector of target
        [state, lttime] = spice.spkezr(tar, et[i], ref, corr, org)
        x_t = [state[0], state[1], state[2]]

        #Get state vector of reference target
        [state, lttime] = spice.spkezr(tar_ref, et[i], ref, corr, org)
        x_r = [state[0], state[1], state[2]]
        v_r = [state[3], state[4], state[5]]
        r_r = math.sqrt(x_r[0]**2+x_r[1]**2+x_r[2]**2)

        # create a plane whose normal vector is parallel to org-ref_target and at position of ref_target
        plane = spice.nvc2pl(x_r, r_r)
        # project v_r onto the plane
        vec_y = spice.vprjp(v_r, plane)

        mout = spice.twovec(x_r, 1, vec_y, 2)
        vec_out = spice.mxv(mout, x_t)

        x[i] = vec_out[0]
        y[i] = vec_out[1]
        z[i] = vec_out[2]
        r[i] = math.sqrt(x[i]**2+y[i]**2+z[i]**2)
        lat[i] = math.asin(z[i]/r[i])
        lon[i] = math.atan2(y[i], x[i])

    return [x, y, z, r, lat, lon]
