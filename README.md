# pycffirmware

This project contains a python wrapper for the source code for the firmware used in the Crazyflie range of platforms, including
the Crazyflie 2.X and the Roadrunner. This project is meant for simulation of on board controller response to sending commands from a ground station. 

## Installation

Clone this repo.
```bash
git clone https://github.com/utiasDSL/pycffirmware.git
cd pycffirmware/
```

Initialize submodules.
```bash
git submodule update --init --recursive
```

### Ubuntu

Install SWIG for your machine. Ensure that the install location is added to your path variable. 
```
sudo apt update
sudo apt -y install swig
```

Install NumPy, `gcc`, and `make`. 
```bash
pip install numpy
sudo apt install build-essential
```

Navigate to and run the build script. 
```bash
cd wrapper
chmod +x build_linux.sh
./build_linux.sh
```

### macOS

Install [`brew`](https://brew.sh).
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install NumPy, SWIG, the `gcc` compiler and `make` command. 
```bash
pip install numpy
brew install swig
brew install gcc 
brew install make
```
Also run `xcode-select --install` if prompted. 

If gcc is installed in a different location than `/usr/local/bin/gcc-12` you will need to edit [`build_osx.sh`](https://github.com/utiasDSL/pycffirmware/blob/main/pycffirmware/build_osx.sh) to reflect this.
You can find the install location using
```bash
locate */bin/gcc-*
```

Navigate to and run the build script. 
```bash
cd wrapper
chmod +x build_osx.sh
./build_osx.sh
```

### Windows

Install SWIG for your machine. Installation instructions can be found [here](https://www.swig.org/download.html). Ensure that the install location is added to your path variable. 

Install NumPy.
```bash
python -m pip install numpy
```

Install [Visual Studio](https://visualstudio.microsoft.com/downloads/). Make sure to include C++ and MSVC build tools. 

Navigate to and run the windows build script. 
```bash
cd wrapper
build_windows.bat
```

## Use 
This module wraps parts of the firmware that are considered "value changing" when it comes to commands. These are the modules of the firmware that could change the intended values for a positional command to fit with Crazyflie constraints. These include: 
- Controller (only PID controller supported)
- High level commander and planner 
- State estimator (coming soon, only Kalman supported)

An example of how one might use this package can be found in [`safe-control-gym`](https://github.com/utiasDSL/safe-control-gym/blob/alpha-iros-competition/safe_control_gym/controllers/firmware/firmware_wrapper.py). 

-----
> University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL)
