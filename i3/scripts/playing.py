#!/usr/bin/python
import json
from os.path import expanduser
import sys
import argparse

home = expanduser("~")
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="Parses and print Google Play Music Desktop Player song info")

def parseJson():
    try:
        with open(home + '/.config/Google Play Music Desktop Player/json_store/playback.json') as f:
            data = f.read()
    except:
        with open(home + '/GPMDP_STORE/playback.json') as f:
            data = f.read()
    return json.loads(data)

def getSong(data):
    return data['song']['title']

def getAlbum(data):
    return data['song']['album']

def getArtist(data):
    return data['song']['artist']

def convert_time(ms):
    x = ms / 1000
    x % 60
    m, s = divmod(x, 60)
    return "%d:%02d" % (m, s)
def getProgress(data):
    cur = data['time']['current']
    total = data['time']['total']
    return convert_time(cur) + "/" + convert_time(total)

def parseLayout(layout):
    displaystr = ""
    for i in layout:
        if i == 't':
            displaystr += getSong(data)
        elif i == 'a':
            displaystr += getAlbum(data)
        elif i == 'A':
            displaystr += getArtist(data)
        elif i == 'p':
            displaystr += getProgress(data)
        elif i == '-':
            displaystr += " - "
    return displaystr

def run(data, layout, notplaying):
    displaystr = ""
    if data['playing']:
        displaystr = parseLayout(layout)
    else:
        sys.stdout.write("   ")
    if sys.version[0] == '2':
        displaystr = displaystr.encode('utf-8')

    if not displaystr and notplaying:
        print("Not Playing")
    else:
        print(displaystr)
import os
from os import environ
if "BLOCK_BUTTON" in os.environ:

    if os.environ['BLOCK_BUTTON'] == '8': #back
        os.system('playerctl previous')

    elif os.environ['BLOCK_BUTTON'] == '9': #next
        os.system('playerctl next')


else:
    print('no')

parser.add_argument("--layout",
        action="store",
        dest="layout",
        help="t = Song Title\na = Song Album\nA = Artist Name\np = Track time progess\n- = Spacer\nExample: t-a-A-p",
    )
parser.add_argument("--not-playing",
        action="store_true",
        dest="notplaying",
        help="Display the text 'Not Playing' when no music is playing",
    )
args = parser.parse_args()
data = parseJson()
try:
    run(data, args.layout, args.notplaying)
except:
    run(data, "t-a-A-p", False)
