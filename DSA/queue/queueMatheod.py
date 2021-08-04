import queue as q
cus  = q.Queue(maxsize = 3)
cus.put(1)
cus.put(2)
cus.put(3)
print(cus.qsize())
cus.get()
print(cus.qsize())