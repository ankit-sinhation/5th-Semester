#!/usr/bin/python2

from urllib2 import Request, urlopen

values = """
  {
    "image": "http://52.66.165.140/image/ankit/ankit_recog1.jpg",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'dbdef037',
  'app_key': '0f060e240e9b9c1a0953e585004a125b'
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
#print  response_body
b=()
b=response_body.split(":")
c=b[3]
d=c.split(",")
a="Ankit_Sinha"
b="Anurag_Kumar"
if a in response_body :
    print "Attendance Updated."
    print "Ankit Sinha Found."
    print "Confidence: "+d[0]
elif b in response_body :
    print "Attendance Updated."
    print "Anurag Kumar Found."
    print "Confidence: "+d[0]
else :
    print "Not Found."
    print "Authentication Failure."
