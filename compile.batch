swig -python  Survey.i
gcc -std=c99 -fPIC -c Survey_wrap.c -I/usr/local/include/python3.6m
ld -shared Survey.o Survey_wrap.o -L/usr/local/include/python3.6m/ -o _Survey.so
