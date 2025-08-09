import time
print("welcome to the pomodoro timer")

min =int(input("Enter Time in minutes: "))

total_secs = min*60

while total_secs>0:
    min=total_secs//60

    sec=total_secs%60

    clock=f"{min:02d}:{sec:02d}"
    print(f"\rTime remaining:{clock}",end="")
    time.sleep(1)
    total_secs-=1

print("\nTime's up")
