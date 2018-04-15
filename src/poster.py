import json
from StringIO import StringIO
import requests
import Image

para = {
  'userName': '武妝妝', 
  'userAvatar': 'http://static.dryeam.com/testIcon.jpg', 
  'qrImg': 'http://static.dryeam.com/qrimg.jpg', 
  'backGroundImg': 'http://static.dryeam.com/20170815112219.jpg', 
  'textColor': {'B': 45, 'R': 123, 'G': 9}
}

r = requests.post("http://openapi.nanchangmama.com/make_post/",data=json.dumps(para))

result = Image.open(StringIO(r.content))
result.show()
