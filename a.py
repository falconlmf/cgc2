import sys
import os
import time
import find
import dictionary
import pyautogui as pag



posDict = dictionary.position()
regDict = dictionary.region()



def clickAll(cls, itm, **kwargs):
    print ('[click]', cls, itm, '**', kwargs)
    if not posDict.get(cls, itm):
        print ('[click] new key')
        posDict.set(cls, itm, find.find(cls, itm))
    for pt in posDict.get(cls, itm):
        pag.moveTo(pt)
        print (pt)

def click(cls, itm, **kwargs):
    print ('[click]', cls, itm, '**', kwargs)
    if not posDict.get(cls, itm):
        print ('[click] new key')
        posDict.set(cls, itm, find.find(cls, itm))
    pt = posDict.get(cls, itm)[0]
    if pt:
        pag.click(pt)


def init():
    print ('[init] start')
    monitor = find.monitor()
    regDict.set(monitor, 'canvas', 'monitor')
    regDict.set([monitor['left']+monitor['width']/2, monitor['top']+monitor['height']/2], 'canvas', 'center')
    regDict.print()
    print ('[init] done')


def main():
    print ('[start]')
    init()
    # clickAll('monster', '花妖')
    # posDict.print('monster')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print (f'bye')
        sys.exit()