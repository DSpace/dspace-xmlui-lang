#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
for file in os.listdir("."):
    if file.endswith(".xml"):
        if file is not "messages.xml":
            print(file)
            os.system('python3 lang-util.py migrate -f ' + file)
            os.system('rm ' + file)
            os.system('cp output.xml ' + file)