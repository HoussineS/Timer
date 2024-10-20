import time
h = int(input("put hours (you can skip put 0)"))
m = int(input("put minutes (you can skip put 0)"))
s = int(input("put seconds (you can skip put 0)"))
while(h==0 and m == 0 and s == 0):
    print("you didn't put any think")
    h = int(input("put hours (you can skip put 0)"))
    m = int(input("put minutes (you can skip put 0)"))
    s = int(input("put seconds (you can skip put 0)"))
your_time = h * 3600 + m * 60 + s

for i in range(your_time,0,-1):
    seconds = i % 60
    minutes = int (i / 60 ) % 60
    hours =int( i / 3600 )
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time is up")