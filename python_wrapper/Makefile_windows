firmdir = ../
modinc = $(firmdir)/src/modules/interface
modinc2 = $(firmdir)/src/hal/interface
modinc3 = $(firmdir)/src/utils/interface
modinc4 = $(firmdir)/vendor/CMSIS/CMSIS/Include
modsrc = $(firmdir)/src/modules/src

cffirmware_wrap.c: cffirmware.i $(modinc)/*.h $(modinc2)/*.h $(modinc3)/*.h $(modinc4)/*.h
	swig -python -I$(modinc) -I$(modinc2) -I$(modinc3) -I$(modinc4) cffirmware.i

clean:
	rm -f cffirmware.py _cffirmware.so *.pyc cffirmware_wrap.c
	rm -rf build
