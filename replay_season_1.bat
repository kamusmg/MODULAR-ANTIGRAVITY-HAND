@echo off
echo [NUCLEUS] Initing Replay: Season 1 (Levels 1-50)...
echo [DANGER] Ensure Art Studio V3 is OPEN before continuing.
pause
.\.venv\Scripts\python src/brain/recursive_artist.py 50
echo [NUCLEUS] Season 1 Replay Complete.
pause
