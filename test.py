import json
import urllib.request
import dateutil  
from dateutil import parser

print()

# 4106 Tupsula -> Hervanta
# 4097 Tupsula -> Keskusta
stopIDList = [4097, 4106]

for stopID in stopIDList:
    
    # Fetch data about stopping busses
    with urllib.request.urlopen("https://data.itsfactory.fi/journeys/api/1/stop-monitoring?stops=" + str(stopID)) as url:
        data = json.load(url)
        # print(data)

    # Fetch data about single stop for a name
    with urllib.request.urlopen("http://data.itsfactory.fi/journeys/api/1/stop-points/" + str(stopID)) as url:
        stopData = json.load(url)

    print("Stop: " + str(stopID) + " - " + str(stopData['body'][0]['name']))

    for stop in data['body'][str(stopID)]:

        # Sometimes there is no aimedArrivalTime key
        if 'expectedDepartureTime' in stop['call']:
            aimedArrivalTime = parser.parse(stop['call']['expectedDepartureTime'])
        else:
            aimedArrivalTime = parser.parse(stop['call']['aimedArrivalTime'])

        print("Bus: " + stop['lineRef']+ ", Time Arrival: " + aimedArrivalTime.strftime("%H:%M") + " (tracked)")
    
    print()
