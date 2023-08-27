python -m pytest -v -s -m sanity --html=./Reports/report3.html testCases/ --browser chrome

rem python -m pytest -v -s -m sanity --html=./Reports/report4.html testCases/ --browser firefox

rem python -m pytest -v -s -m "sanity and regression" --html=Reports\report1.html testCases/ --browser chrome
rem python -m pytest -v -s -m regression --html=Reports\report1.html testCases/ --browser chrome


