#!/usr/bin/env python

""" Fetch the list of recent stations from tuneinradio plugin """
""" and start playing the first one """

import subprocess
import time
from kodipydent import Kodi

## Turn on the TV via CEC over HDMI 
subprocess.call('/usr/bin/kodi-send --action="XBMC.CECActivateSource"', shell=True)

my_kodi = Kodi('localhost', 80)
stations = my_kodi.Files.GetDirectory('plugin://plugin.audio.tuneinradio/?path=recents')
station = stations['result']['files'][0]
my_kodi.Player.Open.im_self.timeout = 120
my_kodi.Player.Open(0, item={u'file': station['file']})
