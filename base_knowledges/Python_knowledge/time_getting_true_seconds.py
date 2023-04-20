# getting time true seconds

import time


while True:
    x = time.localtime()
    print(time.localtime().tm_sec)
    while True:
        time.sleep(0.001)
        if time.localtime().tm_sec != x.tm_sec:
            break
          