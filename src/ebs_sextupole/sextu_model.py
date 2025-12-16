import numpy as np
import numpy as np
from pydantic import BaseModel, ConfigDict

from pyaml.common.element import __pyaml_repr__
from pyaml.common.exception import PyAMLException
from pyaml.control.deviceaccess import DeviceAccess
from pyaml.magnet.model import MagnetModel

import ebs_sextupole_bind

# Define the main class name for this module
PYAMLCLASS = "SextuModel"


class ConfigModel(BaseModel):
    """
    EBS sextupole model configuration

    Parameters
    ----------
    strength_data: str
        Calibration data
    param_file: str
        Parameter file name
    serial_number: str
        Seriai number
    powerconverters: list[DeviceAccess | None]
        Power converters
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    strength_data: str
    param_file: str
    serial_number: str
    powerconverters: list[DeviceAccess | None]
    multipoles : list[str] = ["B2","B0","A0","A1"]


class SextuModel(MagnetModel):

    def __init__(self, cfg: ConfigModel):
        self._cfg = cfg
        self.__nbPS: int = len(cfg.powerconverters)
        if( self.__nbPS != 5 ):
            raise PyAMLException(f"SextuModel {self._cfg.serial_number}: 5 power converters expected")
        self.S = ebs_sextupole_bind.mag_init(self._cfg.strength_data,self._cfg.param_file,self._cfg.serial_number)
        self.brho = np.nan

    def compute_hardware_values(self, strengths: np.array) -> np.array:
        curs = ebs_sextupole_bind.compute_currents(self.S,self._brho,strengths)
        return np.array(curs)

    def compute_strengths(self, currents: np.array) -> np.array:
        strs = ebs_sextupole_bind.compute_strengths(self.S,1./self._brho,currents)
        return np.array(strs)

    def get_strength_units(self) -> list[str]:
        return ["m-2","rad","rad","m-1"]

    def get_hardware_units(self) -> list[str]:
        return ["A","A","A","A","A"]

    def get_devices(self) -> list[DeviceAccess]:
        return self._cfg.powerconverters

    def set_magnet_rigidity(self, brho: np.double):
        self._brho = brho

    def has_hardware(self) -> bool:
        return False

    def __repr__(self):
        return __pyaml_repr__(self)