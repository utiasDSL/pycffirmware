# Crazyflie Firmware

This project contains a python wrapper for the source code for the firmware used in the Crazyflie range of platforms, including
the Crazyflie 2.X and the Roadrunner. This project is meant for simulation of on board controller response to sending commands from a ground station. 

## Installation
Clone this repo 

```
git clone https://github.com/spencerteetaert/crazyflie-firmware.git --single-branch --branch=python_wrapper
cd crazyflie-firmware/
```

Initialize sub repositories 

```
git submodule update --init --recursive
```

Install swig for your machine. Installation instructions can be found [here](https://www.swig.org/download.html). Ensure that the install location is added to your path variable. 

Install Numpy 

```
pip install numpy
```


### **For Linux**

Install the gcc compiler and make command. 
```
sudo apt update
sudo apt install build-essential
```

Navigate to and run the build script. 

```
cd python_wrapper
chmod +x build_linux.sh
./build_linux.sh
```


### **For MacOS**

Install the gcc compiler and make command.
```
brew install gcc make
```

Navigate to and run the build script. 

```
cd python_wrapper
chmod +x build_osx.sh
./build_osx.sh
```

### **For Windows** 

Install [Visual Studios](https://visualstudio.microsoft.com/downloads/). Make sure to include C++ and MSVC build tools. 

Navigate to and run the windows build script. 

```
cd python_wrapper
build_windows.bat
```

## Usage 
This module wraps parts of the firmware that are considered "value changing" when it comes to commands. These are the modules of the firmware that could change the intended values for a positional command to fit with Crazyflie constraints. These include: 
- Controller (only PID controller supported)
- High level commander and planner 
- State estimator (coming soon, only Kalman supported)

An example of how one might use this package can be found in a controller implementation from [safe-control-gym](https://github.com/utiasDSL/safe-control-gym/blob/alpha-iros-competition/safe_control_gym/controllers/firmware/firmware_wrapper.py). 
