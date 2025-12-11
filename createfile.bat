@echo off

set count=%1

for /l %%i in (1,1,%count%) do (
    echo # version%%i > version%%i.py
)

echo Created %count% files!
