#!/usr/bin/python2

from urllib2 import Request, urlopen

values = """
  {
    "image": "http://52.66.165.140/image/ankit/IMG_9348.jpg", 
    "subject_id": "Ankit_Sinha",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'dbdef037',
  'app_key': '0f060e240e9b9c1a0953e585004a125b'
}
request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
