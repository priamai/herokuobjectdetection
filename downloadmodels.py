import requests
import os
def DownloadFile(url,filename):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    return

print('Downloading frozen inference graph')
modelname='Faster-RCNN-ResNet-50'
pb_file = os.path.join('model',modelname+'.pb')

url = 'https://www.dropbox.com/s/yj4weum0yb65d7u/Faster-RCNN-ResNet-50.pb?dl=1'
DownloadFile(url, pb_file)

print('Downloaded frozen inference graph')