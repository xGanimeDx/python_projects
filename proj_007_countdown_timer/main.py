import time

def countdown(countdown_time_in_secs: int) -> None:
    while countdown_time_in_secs:
        mins, secs = divmod(countdown_time_in_secs, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        countdown_time_in_secs -= 1
    print("time's up")

usr_input_time = int(input("Enter time (in secs): "))
countdown(usr_input_time)
