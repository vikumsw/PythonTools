import requests

# 'https://www.kaggle.com/kernels/scriptcontent/14481387/download'


def download(file_title, l):
    for i, k in zip(range(30), l):
        url = 'https://www.kaggle.com/kernels/scriptcontent/' + str(k) + '/download'
        r = requests.get(url, allow_redirects=True)
        filename = 'res/' + file_title + '(' + str(i) + ').ipynb'
        print(url, filename)
        open(filename, 'wb').write(r.content)