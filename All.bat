@echo off

:: JudgeComp.exe
if exist ".\judge\Debug\JudgeComp.exe" (
    tasklist | find /i "JudgeComp.exe" >nul || (
        echo Starting JudgeComp.exe...
        start cmd /K "cd .\judge\Debug&&echo JudgeComp&&JudgeComp.exe"
    )
) else (
    echo JudgeComp.exe not found!
)

:: OperateTimeComp.exe
if exist ".\operatetime\Debug\OperateTimeComp.exe" (
    tasklist | find /i "OperateTimeComp.exe" >nul || (
        echo Starting OperateTimeComp.exe...
        start cmd /K "cd .\operatetime\Debug&&echo OperateTimeComp&&OperateTimeComp.exe"
    )
) else (
    echo OperateTimeComp.exe not found!
)

:: PlotComp.exe
if exist ".\plot\Debug\PlotComp.exe" (
    tasklist | find /i "PlotComp.exe" >nul || (
        echo Starting PlotComp.exe...
        start cmd /K "cd .\plot\Debug && echo PlotComp&& PlotComp.exe"
    )
) else (
    echo PlotComp.exe not found!
)

:: PlotTimeComp.exe
if exist ".\plottime\Debug\PlotTimeComp.exe" (
    tasklist | find /i "PlotTimeComp.exe" >nul || (
        echo Starting PlotTimeComp.exe...
        start cmd /K "cd .\plottime\Debug && echo PlotTimeComp&& PlotTimeComp.exe"
    )
) else (
    echo PlotTimeComp.exe not found!
)

:: QR_recognition.py
if exist ".\qr_recognition\QR_recognition\QR_recognition.py" (
    tasklist | find /i "python.exe" | find /i "QR_recognition.py" >nul || (
        echo Starting QR_recognition.py...
        start cmd /K "cd .\qr_recognition\QR_recognition && echo QR_recognition&& python QR_recognition.py" 


    )
) else (
    echo QR_recognition.py not found!
)

:: RepairManagement.py
if exist ".\repair_management\RepairManagement\RepairManagement.py" (
    tasklist | find /i "python.exe" | find /i "RepairManagement.py" >nul || (
        echo Starting RepairManagement.py...
       	start cmd /K "cd .\repair_management\RepairManagement && echo RepairManagement&&python RepairManagement.py"
    )
) else (
    echo RepairManagement.py not found!
)

:: Retention.py
if exist ".\retention\Retention\Retention.py" (
    tasklist | find /i "python.exe" | find /i "Retention.py" >nul || (
        echo Starting Retention.py...    	
	start cmd /K "cd .\retention\Retention && echo Retention&&python Retention.py"
    )
) else (
    echo Retention.py not found!
)

:: SignalManager.py
if exist ".\signalmanager\SignalManager\SignalManager.py" (
    tasklist | find /i "python.exe" | find /i "SignalManager.py" >nul || (
        echo Starting SignalManager.py...
	start cmd /K "cd .\signalmanager\SignalManager && echo SignalManager&&python SignalManager.py"
    )
) else (
    echo SignalManager.py not found!
)

:: Temporary_time.py
if exist ".\temporary_time\Temporary_time\Temporary_time.py" (
    tasklist | find /i "python.exe" | find /i "Temporary_time.py" >nul || (
        echo Starting Temporary_time.py...
        start cmd /K "cd .\temporary_time\Temporary_time && echo Temporary_time&&python Temporary_time.py"
    )
) else (
    echo Temporary_time.py not found!
)

:: Time_comparison.py
if exist ".\time_comparison\Time_comparison\Time_comparison.py" (
    tasklist | find /i "python.exe" | find /i "Time_comparison.py" >nul || (
        echo Starting Time_comparison.py...
	start cmd /K "cd .\time_comparison\Time_comparison && echo Time_comparison&&python Time_comparison.py"
    )
) else (
    echo Time_comparison.py not found!
)

echo All checks complete.
pause
