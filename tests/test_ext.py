from scipy.constants import speed_of_light
import ebs_sextupole_bind

brho = 6e9 / speed_of_light

fileDir = "MagnetModel/Parameters/"
S = ebs_sextupole_bind.mag_init(f"{fileDir}SD1_meas_strengths.csv",f"{fileDir}SD1_params.csv","SD1-16196")
strs = ebs_sextupole_bind.compute_strengths(S,1./brho,[5.24976230e+01, 1.52758796e-02, 3.94936191e-02, 2.27161913e-02, -3.75450523e-02])
print(strs)
curs = ebs_sextupole_bind.compute_currents(S,brho,strs)
print(curs)