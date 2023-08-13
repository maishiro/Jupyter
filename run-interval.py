
# %%
import time
import datetime
import threading


# %%
def worker():
    # print(time.time())
    print( datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') )
    time.sleep(8)

# %%
def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

# %%
def main():
    schedule(5, worker, False)

# %%
if __name__ == "__main__":
    main()
