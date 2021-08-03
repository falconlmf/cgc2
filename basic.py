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
    pt = findAll(*keys, **kwargs)
    posDict.set(pt, *keys)
    print(posDict.print())
    for pt in posDict.get(*keys):
        pag.click(pt)
        # pag.moveTo(pt)
        # print (pt)

def click(*keys, **kwargs):
    print ('[click]', *keys, '**', kwargs)
    if not posDict.get(*keys):
        posDict.set(find(*keys,  **kwargs), *keys)
    pt = posDict.get(*keys)[0]
    if pt:
        pag.click(pt)

def eliminate(input):
    if len(input) == 0:
        return input
    ret = [input[0]]
    for pt in input:
        print (ret[-1], 'vs', pt, 'abs[0]', abs(pt[0]-ret[-1][0]), 'abs[1]', abs(pt[1]-ret[-1][1]))
        if abs(pt[0]-ret[-1][0]) > 10 and abs(pt[1]-ret[-1][1]) > 10:
            ret.append(pt)
    return ret

def find(*keys, **kwargs):
    pt = fd.find(*keys, monitor=getMonitor(), **kwargs)
    if pt:
        if kwargs.get('offset'):
            return (pt[0][0]+kwargs.get('offset')[0], pt[0][1]+kwargs.get('offset')[1])
        else:
            return pt[0]
    return None

def findAll(*keys, **kwargs):
    pt = fd.find(*keys, monitor=getMonitor(), **kwargs)
    if pt:
        ptelim = eliminate(pt)
        print (f'[findAll] \r\npt({len(pt)}: {pt}\r\nptelim({len(ptelim)}: {ptelim}')
        return ptelim
    return pt

def getMonitor():
    monitor = regDict.get('canvas','monitor')
    if monitor:
        return monitor
    monitor = fd.monitor()
    regDict.set(monitor, 'canvas', 'monitor')
    return monitor

def init():
    print ('[init] start')
    cg = getMonitor()
    print (f'[init] ({len(cg)}) {cg}')
    print ('[init] done')

def main():
    print ('[start]')
    init()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print (f'bye')
        sys.exit()