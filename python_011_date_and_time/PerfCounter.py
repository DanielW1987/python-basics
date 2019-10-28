import time

start_time = time.perf_counter()
time.sleep(3)
end_time = time.perf_counter()

print("Execution time is {}".format(end_time - start_time))
