# ebs-sextupole

EBS sextupole magnet model extetnsion for Python Accelerator Middle Layer.
This module binds C++ EBS Sextupole magnet model to pyAML `MagnetModel`.

Configuration exmaple:
```yaml
- type: pyaml.magnet.cfm_magnet
  name: SJ2A-C04
  mapping:
    - [B2, SJ2A-C04-S]
    - [B0, SJ2A-C04-H]
    - [A0, SJ2A-C04-V]
    - [A1, SJ2A-C04-SQ]
  model:
    type: ebs_sextupole.sextu_model
    strength_data: /operation/control/infra/equipment/magnets/MagnetModel/Parameters/SF2_meas_strengths.csv
    param_file: /operation/control/infra/equipment/magnets/MagnetModel/Parameters/SF2_params.csv
    serial_number: SF2-16246
    powerconverters:
      - type: tango.pyaml.attribute
        attribute: srmag/vps-sf2/c04-a/current
        unit: A
      - type: tango.pyaml.attribute
        attribute: srmag/ps-corr-sf2/c04-a-ch01/current
        unit: A
      - type: tango.pyaml.attribute
        attribute: srmag/ps-corr-sf2/c04-a-ch02/current
        unit: A
      - type: tango.pyaml.attribute
        attribute: srmag/ps-corr-sf2/c04-a-ch03/current
        unit: A
      - type: tango.pyaml.attribute
        attribute: srmag/ps-corr-sf2/c04-a-ch04/current
        unit: A
```
