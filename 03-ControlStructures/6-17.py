time = str(input("Enter time (24-hour format): "))
hour = int(time[0:2])
minute = time[3:5]
fixed_hour = hour - 12
if fixed_hour > 0:
    print(f"Time in 12-hour format: {fixed_hour}:{minute} PM")
else:
    print(f"Time in 12-hour format: {time} AM")