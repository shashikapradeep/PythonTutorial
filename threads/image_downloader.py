#url = 'https://picsum.photos/id/1/800/1200'
import requests;

def getImageUrls(count):
 if count < 1
   print('invalid count')
   return

 for i in range(0:count):
  url = f'https://picsum.photos/id/{i}/800/1200'
  yield url

urls = getImageUrls(100)
for url in urls:

