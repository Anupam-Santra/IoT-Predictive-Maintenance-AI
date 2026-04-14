@echo off
title AI Predictive Maintenance Hub
echo ========================================================
echo   Starting AI Predictive Maintenance Dashboard...
echo   Please wait a moment while the local server boots up.
echo ========================================================

:: Run the Streamlit app
streamlit run app.py

:: Pause keeps the window open if there's an error so you can read it
pause