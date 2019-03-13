#!/usr/bin/env python3
import os
from subprocess import call

if "BLOCK_BUTTON" in os.environ:
    if os.environ['BLOCK_BUTTON'] == '1':
        call(['nm-connection-editor'])
    call(['iwgetid','-r'])
else:
    print('no')
