import webbrowser
import time

n = 0
break_count = 3
print('the program start on' + time.ctime())
while(n<3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=lxcjV59jsoA")
    n=n+1
