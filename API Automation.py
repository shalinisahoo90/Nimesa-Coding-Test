import urllib.request, json
from collections import defaultdict

url_link=u"""https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"""

data = urllib.request.urlopen(url_link).read()
output = json.loads(data)
weather_data = output['list']

tstamps = defaultdict(list)

for item in weather_data:
    dt,tm = item['dt_txt'].split()
    tstamps[int(''.join(dt.split('-')))].append(int(tm.split(':')[0]))
    
    if not (item['main']['temp'] <= item['main']["temp_max"] and item['main']['temp'] >= item['main']["temp_min"]):
        print("test 3 failed --> temp {0}  min_temp {1} max_temp {2}".format( item['main']['temp'], item['main']["temp_min"], item['main']["temp_max"]))
    
    if item["weather"][0]['id'] == 500 and not (item["weather"][0]['description'] == 'light rain') :
            print("test 4  failed  id {0}, description {1}".format(
                item["weather"][0]['id'], item["weather"][0]['description'] ))
    
    elif (item["weather"][0]['id'] == 800) and not (item["weather"][0]['description'] == 'clear sky') :
            print("test 5  failed  id {0}, description {1}".format(
                item["weather"][0]['id'], item["weather"][0]['description'] ))

sorted_key = sorted(tstamps)
strt_time = sorted(tstamps[sorted_key[0]])[0]
end_time = sorted(tstamps[sorted_key[-1]])[-1]

all_hours = []
total_hours = 0

for k in range(len(sorted_key)):
    sorted_hr = sorted(tstamps[sorted_key[k]])
    if k == 0:
        if not sorted_hr ==  list(range(strt_time,24)) :
            all_hours.append(False)
    elif k == len(sorted_key)-1:
        if not sorted_hr ==  list(range(0,end_time+1)):
            all_hours.append(False)
    else:
        if not sorted_hr == list(range(0,24)):
            all_hours.append(False)
    if all_hours:
        total_hours += len(sorted_hr)
    else:
        print("date for each hour for the date {0} is not present.".format(k))

if all_hours:
    print("Test Failed :- every hour data are not present")

if not total_hours >= 24*4 :
    print("Test Fail: Data for only {} hours are present".format(total_hours))
    
print("All Tests passed")
