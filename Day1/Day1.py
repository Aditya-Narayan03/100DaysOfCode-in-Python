import time


timestamp = time.strftime('%H:%M:%S')
print("The Current Time is - " + timestamp)

hour = time.strftime('%H')
print("\nThis is the hour right now " + hour)

if int(hour) > 0 and int(hour) < 12:
	print('Good Morning Sir!!!')

elif int(hour) > 12 and int(hour) < 17:
	print('Good Afternoon Sir!!!')

elif int(hour) > 17 and int(hour) < 20:
	print('Good Evening Sir!!!')

elif int(hour) > 20 and int(hour) < 24:
	print('Good Night Sir!!!')
	
