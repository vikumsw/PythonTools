import requests
import json
import matplotlib.pyplot as plt

x = requests.get('https://www.hpb.health.gov.lk/api/get-current-statistical')
y = json.loads(x.text)

finalUpdate = y['data']['update_date_time']

daily_pcr_testing_data = y['data']['daily_pcr_testing_data']
dataLength=len(daily_pcr_testing_data)

xticks = []
counts = []
for i in daily_pcr_testing_data:
    xticks.append(i['date'])
    counts.append(int(i['count']))

print(xticks)
print(counts)

plt.plot(counts,'ro')
plt.ylabel('Number of PCR Tests')
plt.xlabel('Date')
plt.title('Date vs. Number of PCR Tests ( Last Updated : {})'.format(finalUpdate))
plt.xticks([i for i in range(dataLength)],xticks,rotation=90)
plt.show()