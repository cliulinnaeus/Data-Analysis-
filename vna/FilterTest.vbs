Dim app
Dim scpi

'Start time
'End Time
'Frequency
Dim duration
Dim rate
Dim currTime
Dim filePath
Dim fileName

duration = 10000
rate = 2000
currTime = 0
filePath = "D:\user_saved_states\Che\"


'Create / get the VNA application
Set app = CreateObject ("AgilentPNA835x.Application")
Set scpi = app.ScpiStringParser
scpi.Execute ("SYST:F+PReset")
scpi.Execute ("DISPlay:WINDow1:STATE ON")
Dim z
z = 0
' fileName = filePath
Dim t

Do While currTime < duration

    t = Time()
    fileName = "MMEM:STOR:DATA " & filePath & t &".csv" & ", 'CSV Formatted Data', 'Displayed', 'MA', -1"
    ' Wscript.Echo t
    scpi.Execute ("CALCulate:PARameter:DEFine:EXT '" & t &"', 's11'")

    scpi.Execute ("DISPlay:WINDow1:TRACe1:FEED '" &t&"'")
    scpi.Execute ("MMEM:STOR:DATA 'D:\user_saved_states\Che\" & t &".csv', 'CSV Formatted Data', 'Displayed', 'MA', -1")


   
    ' Wscript.Echo "Hello World!"
    Wscript.Sleep rate
    currTime = currTime + rate
    z = z + 1
Loop
