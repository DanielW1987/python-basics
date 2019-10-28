import time

# seconds since epoch (01.01.1970)
epoch_seconds: float = time.time()

print(epoch_seconds)

# convert epoch seconds to a date
date = time.ctime(epoch_seconds)
print(date)
