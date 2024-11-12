@echo off
rem Prüfen, ob Python installiert ist
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python ist nicht installiert oder nicht im PATH gefunden!
    pause
    exit /b
)

rem Prüfen, ob pytest installiert ist
pip show pytest >nul 2>nul
if %errorlevel% neq 0 (
    echo pytest ist nicht installiert. Installiere es mit "pip install pytest".
    pause
    exit /b
)

rem Testordner definieren
set TEST_DIR=LB1\tests

rem Überprüfen, ob der Testordner existiert
if not exist %TEST_DIR% (
    echo Der Testordner %TEST_DIR% existiert nicht!
    pause
    exit /b
)

rem Alle Tests im Ordner ausführen
echo Führe alle Tests im Ordner %TEST_DIR% aus...
python -m pytest %TEST_DIR% --maxfail=5 --disable-warnings --tb=short

rem Ergebnis anzeigen
if %errorlevel% equ 0 (
    echo Alle Tests wurden erfolgreich bestanden!
) else (
    echo Einige Tests sind fehlgeschlagen.
)

pause
