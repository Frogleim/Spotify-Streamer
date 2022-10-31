import time

start_time = time.time()

while True:
    time.sleep(3)
    print('Hello')
    if time.time() - start_time >= 3:
        time.sleep(5)
        print('Sleeping...')
