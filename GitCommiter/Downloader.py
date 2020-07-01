import requests

# 'https://www.kaggle.com/kernels/scriptcontent/14481387/download'

l = [16723308,16723379,16772145,16817530,17623070,17974938,17975477]

fileTitle='basic-feature-visualizations'

for i,k in zip(range(30), l):
    url = 'https://www.kaggle.com/kernels/scriptcontent/' + str(k) +'/download'
    r = requests.get(url, allow_redirects=True)
    filename = fileTitle + ' (' + str(i) + ').ipynb'
    print(url, filename)
    open(filename, 'wb').write(r.content)