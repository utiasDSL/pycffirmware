SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH
rm -rf build pycffirmware.egg-info
rm _pycffirmware.cpython-39-x86_64-linux-gnu.so pycffirmware_wrap.c pycffirmware.py
export CSW_PYTHON=python3
make CC=/usr/local/bin/gcc-12
python3 -m pip install -e .