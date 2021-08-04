from collections import deque


costo = deque(maxlen=3)

costo.append(1)

costo.append(2)

costo.append(3)

print(costo)
costo.popleft()
print(costo)