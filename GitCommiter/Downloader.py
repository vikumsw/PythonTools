import requests

# 'https://www.kaggle.com/kernels/scriptcontent/14481387/download'

l = [14481387,14506258,14762559,14772014,14772114,14825582,14832157,14832262,14833831,16425441,16439428,16440380,16477362,16494447,16510937,16512453,16512641,17277979,17610093,17923289,19077281]

for i,k in zip(range(30), l):
    url = 'https://www.kaggle.com/kernels/scriptcontent/' + str(k) +'/download'
    r = requests.get(url, allow_redirects=True)
    filename = 'beginners-basic-workflow-introduction (' + str(i) + ').ipynb'
    print(url, filename)
    open(filename, 'wb').write(r.content)