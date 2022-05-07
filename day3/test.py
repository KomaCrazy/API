import http.client
import time

def s1():
  time.sleep(0.1)

conn = http.client.HTTPSConnection("www.google.com")
payload = ''
headers = {
  'Cookie': '1P_JAR=2022-05-06-08; AEC=AakniGN2prwZv9aryI5KRouiw_O0ipSoEgWHfChHpiaO3XDWR4KqvQBjfHc; NID=511=A8nJweAjvt2i5rx1N3_NxOGcVxS9ufwf-hfTe26CbEDn0QSC1BoSZ38R6SDxDRz9c28XmBbjr5RFZOv3WrEAZTXIlPqzdF9SclnoKyT2VUxByj3zvLQhEaEGSG4pSYRrR-Kp_S1OJZb8M-gJHzGdmWM8nGMRGGk_FJTXUpYiUH8'
}
conn.request("GET", "/finance/?sa=X&ved=2ahUKEwjo3L_IvMr3AhWfzzgGHZ-AB2MQ6M8CegQIDhAG", payload, headers)
res = conn.getresponse()
data = res.read()
box = data.decode("utf-8")
box = box.split()
i = 17380
while i < len(box):
  s1()
  print(i,":",box[i])
  i = i + 1