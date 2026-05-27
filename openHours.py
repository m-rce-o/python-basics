opens = 9
closes = 17

curr_time = int(input("Enter current hour (24h format): "))

if curr_time >= opens and curr_time <= closes:
    print("We're open!")
else:
    print("We're closed.")