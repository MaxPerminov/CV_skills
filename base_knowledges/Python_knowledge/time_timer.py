import time

start = time.time()
time.sleep(3)
timer = time.time() - start
print(timer)


#########################################

# printing <1> during 2 seconds
time.sleep(1)
start = time.time()
while time.time() - start < 2:
    print(1)
