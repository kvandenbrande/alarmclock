#!/bin/python
# -*- coding: utf-8 -*-
#__author__ = "Kevin Van den Brande"

from internet import is_connected
from push import pushnotify
import time
import ConfigParser
import socket
import os
import subprocess
import pywapi
import string
import random

NAME = "Kevin"

def alarm():
  if is_connected()==True:
    #print "we have internet connection"
    playlocal()
    time.sleep(2)
    greetings(0)#0 for internet
    weather()
    time.sleep(5)
    radio()
  else:
    #print "there's no internet connection"
    playlocal()
    time.sleep(2)
    greetings(1)#1 for no internet message

def playlocal():
  #output 1 to 6.mp3
  song = str(random.randint(1, 6)) + ".mp3"
  subprocess.Popen(['mpg123', '-q',song]).wait()


def greetings(status):
  #day_of_month=str(bsn.d2w(int(time.strftime("%d"))))

  now = time.strftime("%A %B %d") + ',' + time.strftime(" %I %M %p")

  if int(time.strftime("%H")) < 12:
    period = 'morning'
  if int(time.strftime("%H")) >= 12:
    period = 'afternoon'
  if int(time.strftime("%H")) >= 17:
    period = 'evening'

  #print time.strftime("%H")
  #print period

  # reads out good morning + my name
  gmt = 'Good ' + period + ', '

  # reads date and time 
  day = ' it\'s ' + now + '.  '

  # reads no internet
  internet = ' currently there is no active internet connection'

  if status ==0:
    greeting = gmt + NAME + day
  else:
    greeting = gmt + NAME + day + internet
  
  cmd_string = 'espeak -s110 -ven-f3 "{0}" >/dev/null'.format(greeting)
  #print cmd_string
  os.system(cmd_string)

def weather():
  weather_com_result = pywapi.get_weather_from_weather_com('BEXX0317')
  weather = "The weather today is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + " degrees celsius \n\n"

  cmd_string = 'espeak -s110 -ven-f3 "{0}" >/dev/null'.format(weather)
  print cmd_string
  os.system(cmd_string)
  pushnotify("Weather forecast", weather)

def radio():
  os.system('mpc play')

alarm()


