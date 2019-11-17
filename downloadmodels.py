import urllib.request
print('Downloading frozen inference graph')
url = 'https://www.dropbox.com/s/yj4weum0yb65d7u/frozen_inference_graph.pb?dl=1'
urllib.request.urlretrieve(url, "./model/frozen_inference_graph.pb")

print('Downloaded frozen inference graph')