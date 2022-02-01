@echo off
color cf
echo ############################################
echo #	       Utility set-ups Modules     #
echo ############################################
pause
py -m pip install haversine
py -m pip install Pillow
color 0f
start py main.py