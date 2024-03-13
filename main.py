import WIFI_CONFIG
from network_manager import NetworkManager
import time
import uasyncio
import ujson
import urllib
#from urllib import urequest
#from urllib2 import urequest
#import base64
import urequests
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni import Button
import gc


"""
Lets get Some Train Data from the RealTimeTrains API
"""

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

graphics = PicoGraphics(DISPLAY_INKY_PACK)
graphics.set_font("bitmap8")

WIDTH, HEIGHT = graphics.get_bounds()
ENDPOINT = "http://api.rtt.io/api/v1/json/search/PRE"


def status_handler(mode, status, ip):
    graphics.set_update_speed(2)
    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)
    graphics.text("Network: {}".format(WIFI_CONFIG.SSID), 10, 10, scale=2)
    status_text = "Connecting..."
    if status is not None:
        if status:
            status_text = "Connection successful!"
        else:
            status_text = "Connection failed!"

    graphics.text(status_text, 10, 30, scale=2)
    graphics.text("IP: {}".format(ip), 10, 60, scale=2)
    graphics.update()


network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=status_handler)


def update():
    uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))

    url = ENDPOINT
    print("Requesting URL: {}".format(url))

    payload = {}
    headers = {
      'Authorization': 'Basic YOUR_REALTIME_TRAIN_API_USERNAME:PASSWORD_BASE64_ENCODED'
        }

    print(gc.mem_free())
    #response = urequests.request("GET", url, headers=headers, data=payload)
    j = ujson.loads(urequests.request("GET", url, headers=headers, data=payload).text)
    #print(response.text)
    print(gc.mem_free())

    #j = ujson.loads(response.text)

    print(j)

    graphics.set_update_speed(1)
    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)
    graphics.text("Time Destination      Plat", 0, 1, wordwrap=WIDTH, scale=2)
    graphics.text("Expt", 245, 1, wordwrap=WIDTH, scale=2)
    graphics.line(0, 21, WIDTH, 20, 2)
    
    ypos=23;
    
    stopcount = 1
    
    for service in j['services']:
        graphics.text(service['locationDetail']['gbttBookedDeparture'], 0, ypos, wordwrap=WIDTH - 10, scale=2)
        graphics.text(service['locationDetail']['destination'][0]['description'][:15], 50, ypos, wordwrap=WIDTH - 10, scale=2)
        graphics.text("{:>4}".format(service['locationDetail']['platform']), 205, ypos, wordwrap=WIDTH - 10, scale=2)
        
        expected = int(service['locationDetail']['realtimeDeparture'])
        scheduled = int(service['locationDetail']['gbttBookedDeparture'])
        
        #print(expected)
        #print(scheduled)
        
        if expected > scheduled:
            graphics.text(service['locationDetail']['realtimeDeparture'], 245, ypos, wordwrap=WIDTH - 10, scale=2)
        else:
            graphics.text("OnTime", 245, ypos, wordwrap=WIDTH - 10, scale=2)
        
        #graphics.text(service['locationDetail']['realtimeDeparture'], 350, ypos, wordwrap=WIDTH - 10, scale=2)
        #print(service['locationDetail'])
        #print("-----------------")
        ypos=ypos+18
        stopcount = stopcount+1
        if stopcount > 6:
            break
        
import WIFI_CONFIG
from network_manager import NetworkManager
import time
import uasyncio
import ujson
import urllib
#from urllib import urequest
#from urllib2 import urequest
#import base64
import urequests
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni import Button
import gc


"""
Lets get Some Train Data from the RealTimeTrains API
"""

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

graphics = PicoGraphics(DISPLAY_INKY_PACK)
graphics.set_font("bitmap8")

WIDTH, HEIGHT = graphics.get_bounds()
ENDPOINT = "http://api.rtt.io/api/v1/json/search/PRE"


def status_handler(mode, status, ip):
    graphics.set_update_speed(2)
    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)
    graphics.text("Network: {}".format(WIFI_CONFIG.SSID), 10, 10, scale=2)
    status_text = "Connecting..."
    if status is not None:
        if status:
            status_text = "Connection successful!"
        else:
            status_text = "Connection failed!"

    graphics.text(status_text, 10, 30, scale=2)
    graphics.text("IP: {}".format(ip), 10, 60, scale=2)
    graphics.update()


network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=status_handler)


def update():
    uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))

    url = ENDPOINT
    print("Requesting URL: {}".format(url))

    payload = {}
    headers = {
      'Authorization': 'Basic YOUR_REALTIME_TRAIN_API_USERNAME:PASSWORD_BASE64_ENCODED'
        }

    print(gc.mem_free())
    #response = urequests.request("GET", url, headers=headers, data=payload)
    j = ujson.loads(urequests.request("GET", url, headers=headers, data=payload).text)
    #print(response.text)
    print(gc.mem_free())

    #j = ujson.loads(response.text)

    # print(j)

    graphics.set_update_speed(1)
    graphics.set_pen(15)
    graphics.clear()
    graphics.set_pen(0)
    graphics.text("Time Destination      Plat", 0, 1, wordwrap=WIDTH, scale=2)
    graphics.text("Expt", 245, 1, wordwrap=WIDTH, scale=2)
    graphics.line(0, 21, WIDTH, 20, 2)
    
    ypos=23;
    
    for service in j['services']:
        graphics.text(service['locationDetail']['gbttBookedDeparture'], 0, ypos, wordwrap=WIDTH - 10, scale=2)
        graphics.text(service['locationDetail']['destination'][0]['description'][:15], 50, ypos, wordwrap=WIDTH - 10, scale=2)
        
        if 'platform' in service['locationDetail']:
            graphics.text("{:>4}".format(service['locationDetail']['platform']), 205, ypos, wordwrap=WIDTH - 10, scale=2)
        
        if 'realtimeDeparture' in service['locationDetail']:
            expected = int(service['locationDetail']['realtimeDeparture'])
            scheduled = int(service['locationDetail']['gbttBookedDeparture'])
            
            #print(expected)
            #print(scheduled)
            
            if expected > scheduled:
                graphics.text(service['locationDetail']['realtimeDeparture'], 245, ypos, wordwrap=WIDTH - 10, scale=2)
            else:
                graphics.text("OnTime", 245, ypos, wordwrap=WIDTH - 10, scale=2)
        
        else:
            graphics.text("Cance", 245, ypos, wordwrap=WIDTH - 10, scale=2)
        #graphics.text(service['locationDetail']['realtimeDeparture'], 350, ypos, wordwrap=WIDTH - 10, scale=2)
        # print(service['locationDetail'])
        #print("-----------------")
        ypos=ypos+18

    graphics.update()


# Run continuously.
# Be friendly to the API you're using!
while True:
    update()

    while not button_a.is_pressed:
        time.sleep(0.1)

    graphics.update()


# Run continuously.
# Be friendly to the API you're using!
while True:
    update()

    while not button_a.is_pressed:
        time.sleep(0.1)





