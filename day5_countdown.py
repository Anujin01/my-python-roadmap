import time
my_time = 0

my_time = int(input("Enter coundownn number: "))

while my_time <= 0:
    my_time = int(input("Enter coundownn number: "))

for x in range(my_time, -1, -1):
    seconds = int(x % 60)
    minutes = int((x/60) % 60)
    if minutes == 10:
        continue #skips when it is minute 10
    hours = int((x/3600) % 60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("end")
