
import urllib.request, json

url_link = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
data = urllib.request.urlopen(url_link).read()
output = json.loads(data)
#print (output)
weather_data = output['list']
cnt = 0
#print(weather_data)

from collections import defaultdict

tstamps = defaultdict(list)

for item in weather_data:
    # print('\n\n', item)
    cnt += 1
    dt, tm = item['dt_txt'].split()
    tstamps[int(''.join(dt.split('-')))].append(int(tm.split(':')[0]))

    if not (item['main']['temp'] <= item['main']["temp_max"] and item['main']['temp'] >= item['main']["temp_min"]):
        print("test 3 failed --> temp {0}  min_temp {1} max_temp {2}".format(item['main']['temp'],
                                                                             item['main']["temp_min"],
                                                                             item['main']["temp_max"]))

    if item["weather"][0]['id'] == 500:
        if not (item["weather"][0]['description'] == 'light rain'):
            print("test 4  failed  id {0}, description {1}".format(
                item["weather"][0]['id'], item["weather"][0]['description']))

    if (item["weather"][0]['id'] == 800):
        if not (item["weather"][0]['description'] == 'clear sky'):
            print("test 5  failed  id {0}, description {1}".format(
                item["weather"][0]['id'], item["weather"][0]['description']))

    '''if cnt == 5:
        break
    '''
# print(tstamps)


sorted_key = sorted(tstamps)

strt_time = sorted(tstamps[sorted_key[0]])[0]
end_time = sorted(tstamps[sorted_key[-1]])[-1]

all_hours = True
total_hours = 0

for k in range(len(sorted_key)):

    sorted_hr = sorted(tstamps[sorted_key[k]])
    if k == 0:
        if not sorted_hr == list(range(strt_time, 24)):
            all_hours = False
    elif k == len(sorted_key) - 1:
        if not sorted_hr == list(range(0, end_time + 1)):
            all_hours = False
    else:
        if not sorted_hr == list(range(0, 24)):
            all_hours = False
    if all_hours:
        total_hours += len(sorted_hr)
    else:
        print("date for each hour for the date {0} is not present.".format(k))

if not all_hours:
    print("Test Failed :- every hour data are present")
if not total_hours >= 24 * 4:
    print("Test Fail: Data for only {} hours are present".format(total_hours))

print("All Tests passed")

