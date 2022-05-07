import time
box = 0
t0 = time.time()
for i in range(10000000):
    while box < 10000 :
        #print(box)
        box = box + 1
t = time.time()
print(t-t0) # ได้ 0.8062782287597656