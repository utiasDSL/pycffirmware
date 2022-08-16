"""Compiles the cffirmware C extension."""

from distutils.core import setup, Extension
import os, sys
import glob

import numpy as np


fw_dir = "../"
include = [
    os.path.join(fw_dir, "src/modules/interface"),
    os.path.join(fw_dir, "src/hal/interface"),
    os.path.join(fw_dir, "src/utils/interface"),
    os.path.join(fw_dir, "src/config"),
    os.path.join(fw_dir, "src/drivers/interface"),
    # os.path.join(fw_dir, "vendor/CMSIS/CMSIS/Include"),
    np.get_include(),
]

modules = [
    "collision_avoidance.c",
    "planner.c",
    "pptraj.c",
    "pptraj_compressed.c",
    "controller_pid.c",
    "position_controller_pid.c",
    "attitude_pid_controller.c",
    "pid.c",
    "sensfusion6.c",
    "crtp_commander_high_level.c",
    # "estimator_kalman.c",
    # "kalman_core.c",
    # "outlierFilter.c"
]
utils = [
    "filter.c",
    "num.c",
]
drivers = [
    # "motors.c"
]
math_packages = [] #glob.glob(os.path.join(fw_dir, "vendor/CMSIS/CMSIS/DSP_Lib/Source/*/*.c"))

fw_sources = [os.path.join(fw_dir, "src/modules/src", mod) for mod in modules] \
    + [os.path.join(fw_dir, "src/utils/src", mod) for mod in utils] \
    + [os.path.join(fw_dir, "src/drivers/src", mod) for mod in drivers] + math_packages

if sys.platform == 'win32':
    compile_args=[
        "-Ox",
        "-D__fp16=uint16_t",
        "/std:c++17"
    ]
else:
    compile_args=[
        "-O3",
        "-D__fp16=uint16_t",
        "-std=gnu11"
    ]

cffirmware = Extension(
    "_cffirmware",
    include_dirs=include,
    sources=fw_sources + ["cffirmware_wrap.c"],
    extra_compile_args=compile_args,
)

setup(name="cffirmware", version="1.0", ext_modules=[cffirmware])
