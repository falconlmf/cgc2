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
    monitor = regDict.get('canvas','monitor')
    pt = fd.find(*keys, monitor=monitor)
    if pt:
        return pt[0]
    return None

def findAll(*keys):
    monitor = regDict.get('canvas','monitor')
    return fd.find(keys, monitor=monitor)

def findMonitor():
    return fd.monitor()

def init():
    print ('[init] start')
    monitor = findMonitor()
    regDict.set(monitor, 'canvas', 'monitor')
    regDict.set([monitor['left']+monitor['width']/2, monitor['top']+monitor['height']/2], 'canvas', 'center')
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