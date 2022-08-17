firmdir = ../
modinc = $(firmdir)/src/modules/interface
modinc2 = $(firmdir)/src/hal/interface
modinc3 = $(firmdir)/src/utils/interface
modinc4 = $(firmdir)/vendor/CMSIS/CMSIS/Include
modsrc = $(firmdir)/src/modules/src

swig: setup.py pycffirmware_wrap.c $(modsrc)/*.c
	$(CSW_PYTHON) setup.py build_ext --inplace

pycffirmware_wrap.c: pycffirmware.i $(modinc)/*.h $(modinc2)/*.h $(modinc3)/*.h $(modinc4)/*.h
	swig -python -I$(modinc) -I$(modinc2) -I$(modinc3) -I$(modinc4) pycffirmware.i

clean:
	rm -f pycffirmware.py _pycffirmware.so *.pyc pycffirmware_wrap.c
	rm -rf build
