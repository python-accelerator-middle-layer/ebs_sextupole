from scipy.constants import speed_of_light
import ebs_sextupole_bind
from ebs_sextupole.sextu_model import SextuModel, ConfigModel as SextuConfigModel

brho = 6e9 / speed_of_light

fileDir = "MagnetModel/Parameters/"
S = ebs_sextupole_bind.mag_init(
    f"{fileDir}SD1_meas_strengths.csv", f"{fileDir}SD1_params.csv", "SD1-16196"
)
strs = ebs_sextupole_bind.compute_strengths(
    S,
    1.0 / brho,
    [5.24976230e01, 1.52758796e-02, 3.94936191e-02, 2.27161913e-02, -3.75450523e-02],
)
print(strs)
curs = ebs_sextupole_bind.compute_currents(S, brho, strs)
print(curs)


s = SextuModel(
    SextuConfigModel(
        strength_data=f"{fileDir}SD1_meas_strengths.csv",
        param_file=f"{fileDir}SD1_params.csv",
        serial_number="SD1-16196",
        powerconverters=[None,None,None,None,None],
    )
)
s.set_magnet_rigidity(brho)
strs = s.compute_strengths([5.24976230e01, 1.52758796e-02, 3.94936191e-02, 2.27161913e-02, -3.75450523e-02])
print(strs)
curs = s.compute_hardware_values(strs)
print(curs)
