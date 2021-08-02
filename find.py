import os
import time
import cv2
import mss
import numpy as np

def monitor():
    bottomleft = find('ui_bar', 'status_off', corner='bottomleft',duration=-1)
    topright = find('ui_action', 'kick', corner='topright',duration=-1)
    left = bottomleft[0][0]
    top = topright[0][1]
    width = topright[0][0]-bottomleft[0][0]
    height = bottomleft[0][1]-topright[0][1]
    # return [left, top, width, height]
    return {'top':top, 'left':left, 'width':width, 'height':height}

def find(cls, itm, corner='center', monitor=None, save=0, duration=0, log=0):
    print (f'[find]: {cls}/{itm} at monitor({monitor})')
    time_end = 0
    findings = []
    if duration > 0:
        time_end = time.time() + duration
    if not os.path.isfile(f'{cls}/{itm}.png'):
        print (f'[find] FILE ERROR: {cls}, {itm}')
        return findings

    template = cv2.imread(f'{cls}/{itm}.png',cv2.IMREAD_UNCHANGED)
    h, w = template.shape[:-1]
    with mss.mss() as sct:
        if monitor:
            _x = monitor['left']
            _y = monitor['top']
            _monitor = monitor
        else:
            _x = 0
            _y = 0
            _monitor = sct.monitors[0]
        while 1:
            mask = template.copy()
            img = np.array(sct.grab(_monitor))
            res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED, None, mask=mask)
            match_locations = np.where(res>=0.99999)
            if log:
                print('match_locations: ', match_locations)
            # draw template match boxes, scan from top left
            for (x, y) in zip(match_locations[1], match_locations[0]):
                x += _x
                y += _y
                if corner == 'center':
                    findings.append([int(x+w/2),int(y+h/2)])
                elif corner == 'topleft':
                    findings.append([x,y])
                elif corner == 'topright':
                    findings.append([x+w,y])
                elif corner == 'bottomleft':
                    findings.append([x,y+h])
                elif corner == 'bottomright':
                    findings.append([x+w,y+h])
                if save:
                    cv2.rectangle(img, (x, y), (x+w, y+h), [0,0,255,255], 1)
                    cv2.rectangle(img, findings[-1], findings[-1], [200,255,200,255], 2)
                    cv2.imwrite(f'runtime/{save}.png', img)
                    # cv2.imshow('', img)
            if duration >= 0:
                if time.time() > time_end:
                    break
                if findings:
                    break
            elif findings:
                    break
    return findings



def demo():
    while 1:
        t = time.time()
        ret = find('test',save=1)
        print (ret, 1/(time.time()-t))