@echo off
REM this is a cmd file to compile and link Survey.c to python on windows (as specified on the course pdf)
REM so far this has been useless as Survey.o isn't recognized

set PYTHON_DIR=%USERPROFILE%\AppData\Local\Programs\Python\Python37\include\
swig -python Survey.i
gcc -std=c99 -fPIC -c Survey_wrap.c -I %PYTHON_DIR%
ld -shared Survey.o Survey_wrap.o -L %PYTHON_DIR% -o _Survey.so
