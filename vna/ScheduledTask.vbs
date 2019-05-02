Dim app
Dim scpi

'Start time
'End Time
'Frequency

Dim delay

Dim startTime
Dim endTime
Dim time

Dim filePath
Dim fileName

startTime = 151140
endTime = 151240
delay = 1000 'millisecond

filePath = "D:\user_saved_states\Che\"
'Create / get the VNA application
' Set app = CreateObject ("AgilentPNA835x.Application")
' Set scpi = app.ScpiStringParser
' scpi.Execute ("SYST:F+PReset")
' scpi.Execute ("DISPlay:WINDow1:STATE ON")


' Wscript.Echo "hi"

time = Now()
hms = hmsTime(time)
' Wscript.Echo hms
' Only execute between 11:00AM and 11:30AM

While hms < startTime
    WScript.Sleep 2
    time = Now()
    hms = hmsTime(time)
    WScript.Echo hms
Wend
' Do your job here





While hmsTime(time) < endTime

    time = Now()
    ' fileName = "MMEM:STOR:DATA " & filePath & t &".csv" & ", 'CSV Formatted Data', 'Displayed', 'MA', -1"
    Wscript.Echo time
    ' scpi.Execute ("CALCulate:PARameter:DEFine:EXT '" & time &"', 's11'")

    ' scpi.Execute ("DISPlay:WINDow1:TRACe1:FEED '" & time &"'")
    ' scpi.Execute ("MMEM:STOR:DATA 'D:\user_saved_states\Che\" & time &".csv', 'CSV Formatted Data', 'Displayed', 'MA', -1")


   
    ' Wscript.Echo "Hello World!"
    Wscript.Sleep delay
    
Wend


Function hmsTime(t)
    hmsTime = Second(t) + Minute(t) * 100 + 10000 * Hour(t)
End Function
