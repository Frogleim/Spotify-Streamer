import time
starttime = time.time()
while True:
    print("tick")
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))