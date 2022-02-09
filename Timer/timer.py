from datetime import datetime as now
from time import sleep
while True:
	hour=input('hour:        ')
	minute=input('minute:      ')
	second=input('second:      ')
	start=input(f'Set the timer for: hour:{hour}---minute:{minute}---second:{second} : (yes or enter / no)')
	if start=="yes" or start=="":
		timer=hour+minute+second
		condition=True
		while condition:
			now_tm_hour=now.today().strftime("%H")
			now_tm_min=now.today().strftime("%M")
			now_tm_sec=now.today().strftime("%S")
			TimeNowStr=f"{now_tm_hour}{now_tm_min}{now_tm_sec}"
			print(f'Now: {now_tm_hour}:{now_tm_min}:{now_tm_sec}',end='\r')
			if (timer==TimeNowStr):
				print("OK! TimeNow:")
				print(f"hour:{now_tm_hour}---minute:{now_tm_min}---second:{now_tm_sec}")
				condition=False
			sleep(0.01)
