#!/usr/bin/env python3
import alsaaudio, os
m = alsaaudio.Mixer()
vol = m.getvolume()[0]
meter = "[---------]"
spot = int(vol / 10)
meter = (meter[:spot]+"|"+meter[spot+1:])
if "BLOCK_BUTTON" in os.environ:
    if os.environ['BLOCK_BUTTON'] == '3':
        if m.getmute()[0] == 1:
            m.setmute(0)
        else:
            m.setmute(1)
    elif os.environ['BLOCK_BUTTON'] == '4':
        m.setvolume(vol+5)
    elif os.environ['BLOCK_BUTTON'] == '5':
        m.setvolume(vol-5)
    if m.getmute()[0] == 1:
        vol = 'MUTE'
    else:
        vol = str(vol)+"%"
    print(vol,meter)

else:
    print('no')
