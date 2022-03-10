#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os import environ
if "BLOCK_BUTTON" in os.environ:
    if os.environ['BLOCK_BUTTON'] == '4':
        os.system('light -A 10')

    elif os.environ['BLOCK_BUTTON'] == '5':
        os.system('light -U 10')

    print("☀")

else:
    print('no')
