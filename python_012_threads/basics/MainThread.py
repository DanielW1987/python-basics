import threading

print("Current thread that is running:", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Current thread is main thread")
else:
    print("Some other thread")

