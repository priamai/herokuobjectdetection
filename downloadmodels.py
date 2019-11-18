import urllib.request
print('Downloading frozen inference graph')
url = 'https://www.dropbox.com/s/yj4weum0yb65d7u/Faster-RCNN-ResNet-50.pb?dl=1'
urllib.request.urlretrieve(url, "./model/Faster-RCNN-ResNet-50.pb")

print('Downloaded frozen inference graph')