import winsound
import math
for i in range(10):
    winsound.Beep(int(600 * math.sin(i / 6.28) + 700), 100)
print("\a")