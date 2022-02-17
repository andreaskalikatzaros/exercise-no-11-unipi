import math
import numpy as np
from urllib import request
from urllib.request import Request, urlopen
import json
d=[]
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data=data.decode()
res = json.loads(data)
v=(res['round'])
print(v)
for i in range (v-20,v):
  
  g=str(i)
  req = Request("https://drand.cloudflare.com/public/"+g, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
  data = urlopen(req).read()
  data=data.decode()
  res = json.loads(data)
  y=len(res['randomness'])
  for i in range (0,len(res['randomness'])):
     d.append(res['randomness'][i])
     
     
  
  k ="".join(d)
  
  k = int(k, 16)
  n=16
  p=k/n
  s=-sum([p*math.log2(p) for _ in range(n)])
  print('entropy: %.3f ' % s)
  d=[]
