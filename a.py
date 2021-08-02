import sys
import os
import time
import find as fd
import dictionary
import pyautogui as pag



posDict = dictionary.position()
regDict = dictionary.region()



def clickAll(*keys, **kwargs):
    print ('[click]', *keys, '**', kwargs)
    if not posDict.get(*keys):
        posDict.set(fd.find(*keys), *keys)
    for pt in posDict.get(*keys):
        pag.moveTo(pt)
        print (pt)

def click(*keys, **kwargs):
    print ('[click]', *keys, '**', kwargs)
    if not posDict.get(*keys):
        posDict.set(fd.find(*keys), *keys)
    pt = posDict.get(*keys)[0]
    if pt:
        pag.click(pt)

def find(*keys):
    pt = fd.find(*keys, monitor=getMonitor())
    return pt or None

def findAll(*keys):
    return fd.find(keys, monitor=getMonitor())

def getMonitor():
    monitor = regDict.get('canvas','monitor')
    if monitor:
        return monitor
    monitor = fd.monitor()
    regDict.set(monitor, 'canvas', 'monitor')
    regDict.set([monitor['left']+monitor['width']/2, monitor['top']+monitor['height']/2], 'canvas', 'center')
    return monitor

def init():
    print ('[init] start')
    pag.click(find('ui_bar', 'status_off'))
    while 1:
        print(find('ui_bar', 'status_off'))
    print ('[init] done')

def main():
    print ('[start]')
    init()
    # clickAll('monster', '花妖')
    # posDict.print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print (f'bye')
        sys.exit()