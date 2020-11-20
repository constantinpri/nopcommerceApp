pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ 
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ 
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ 
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ 
pause
