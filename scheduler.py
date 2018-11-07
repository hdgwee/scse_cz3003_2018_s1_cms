import sched, time
import urllib.request
import json


s = sched.scheduler(time.time, time.sleep)
sendPSIAlert = False
def send_email(a='default'):
  #contents = urllib.request.urlopen("http://localhost:8000/reports/send_email").read()
  #print(contents)
  print("Boo")
  s.enter(10, 1, send_email)


def checkPSI():
    contents = urllib.request.urlopen("http://localhost:8000/get_psi?psi_type=psi_twenty_four_hourly").read()
    data = json.loads(contents)
    northAlert = 0
    southAlert = 0
    eastAlert = 0
    westAlert = 0
    north = float(data['north'])
    south = float(data['south'])
    west = float(data['west'])
    east = float(data['east'])
    if north > 50:
        sendPSIAlert = True
        northAlert = 1
        print("North PSI too high")
    if south > 50:
        sendPSIAlert = True
        southAlert = 1
        print("South PSI too high")
    if east > 50:
        sendPSIAlert = True
        eastAlert = 1
        print("East PSI too high")
    if west > 50:
        sendPSIAlert = True
        westAlert = 1
        print("West PSI too high")
    if sendPSIAlert:
        data = {'north': northAlert , 'south':southAlert , 'east':eastAlert, 'west':westAlert }
        data_json = json.dumps(data)
        print(data_json)
        #requests.post("http://127.0.0.1:5000/api/v1.0/projects", json=data_json)
    s.enter(2, 1, checkPSI)

def print_some_times():
  print(time.time())
  s.enter(10, 1, send_email)
  s.enter(5, 1, checkPSI)
  s.run()
  print(time.time())

print_some_times()
