rmdir build /s
rmdir pycffirmware.egg-info /s
del pycffirmware_wrap.c 
del pycffirmware.py
del _pycffirmware.cp38-win_amd64.pyd

set CSW_PYTHON=python
nmake
%CSW_PYTHON% -m pip install -e .