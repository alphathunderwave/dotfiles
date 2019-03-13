#!/usr/bin/env python3
import math
power_now = open("/sys/class/power_supply/BAT1/energy_now", "r").readline()
power_full = open("/sys/class/power_supply/BAT1/energy_full", "r").readline()
status = open("/sys/class/power_supply/BAT1/status", "r").readline()
pwr = int(math.ceil(float(power_now)/float(power_full) * 100))
meter = "[----------]"
spot = int(pwr / 10)
meter = (meter[:spot]+"|"+meter[spot+1:])
# print (meter + ' ' + str(pwr) + "%" + status)
print (str(pwr) + "% " + status)
