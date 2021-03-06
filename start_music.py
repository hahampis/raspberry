#!/usr/bin/env python

""" Fetch the list of recent stations from tuneinradio plugin """
""" and play one at random """

import subprocess
import time
from kodipydent import Kodi
from random import choice


def kodi_is_playing():
    if my_kodi.Player.GetActivePlayers()['result'] == []:
        return False
    else:
        return True


if __name__ == '__main__':
    my_kodi = Kodi('localhost', 80)
    ## Turn on the TV via CEC over HDMI 
    subprocess.call('/usr/bin/kodi-send --action="XBMC.CECActivateSource"', shell=True)
    if not kodi_is_playing():
        stations = my_kodi.Files.GetDirectory('plugin://plugin.audio.tuneinradio/?path=recents')
        station = choice(stations['result']['files'])
        my_kodi.Player.Open.im_self.timeout = 120
        my_kodi.Player.Open(0, item={u'file': station['file']})
    else:
        print "Kodi is already playing"
