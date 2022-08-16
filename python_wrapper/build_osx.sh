SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTPATH
rm -rf build cffirmware.egg-info
rm _cffirmware.cpython-39-x86_64-linux-gnu.so cffirmware_wrap.c cffirmware.py
export CSW_PYTHON=python3
make CC=/usr/local/bin/gcc-12
python3 -m pip install -e .