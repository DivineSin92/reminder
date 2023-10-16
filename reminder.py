from time import sleep
import winsound

def reminder(time_s, message):
    times = 0
    print(chr(27) + "[2J")
    while times < time_s:
        sleep(1)
        times += 1

        time_left = time_s - times
        min_left = time_left // 60
        sec_left = time_left % 60

        print(f'{chr(27) + "[2J"} Time left: {min_left:02d}:{sec_left:02d}')
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    print(message)

time_m = int(input('Enter time in min: '))
message = input('Remind about?: ')
time_s = time_m * 60
reminder(time_s, message)
