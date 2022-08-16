rmdir build /s
rmdir cffirmware.egg-info /s
del cffirmware_wrap.c 
del cffirmware.py
del _cffirmware.cp38-win_amd64.pyd

set CSW_PYTHON=python
nmake Makefile_windows
%CSW_PYTHON% -m pip install -e .