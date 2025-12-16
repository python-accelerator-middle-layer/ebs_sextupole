from pyaml.accelerator import Accelerator

sr = Accelerator.load("EBSOrbit.yaml")
sr.live.orbit.correct()