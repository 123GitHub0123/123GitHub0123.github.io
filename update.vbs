Option Explicit
Dim objShell
Set objShell = CreateObject("WScript.Shell")

objShell.Run "cmd /c python douban.py && git add * && git commit -m 'update' && git push", 0, True

Set objShell = Nothing
