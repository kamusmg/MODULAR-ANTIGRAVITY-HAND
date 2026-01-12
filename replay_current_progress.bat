@echo off
echo [NUCLEUS] Initing Full Replay: Level 1 to 53...
echo [DANGER] Ensure Art Studio V3 is OPEN before continuing.
pause
.\.venv\Scripts\python src/brain/recursive_artist.py 53
echo [NUCLEUS] Full Replay Complete.
pause
