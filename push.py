#!/bin/python
# -*- coding: utf-8 -*-
#__author__ = "Kevin Van den Brande"

#pip install pushbullet.py

from pushbullet import PushBullet

def pushnotify(title, body):

    apiKey = "o.3lKNfLdeqfB0aBGR1FCfTlggRTleA1PO"
    p = PushBullet(apiKey)

    p.push_note(title,body)
