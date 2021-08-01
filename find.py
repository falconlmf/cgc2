import os
import time
import cv2
import mss
import numpy as np

def monitor():
    while 1:
        bottomleft = find('ui_bar', 'status_off', corner='bottomleft')
        topright = find('ui_action', 'kick', corner='topright')
        if bottomleft and topright:
            break
        time.sleep(0.5)
    left = bottomleft[0][0]
    top = topright[0][1]
    width = topright[0][0]-bottomleft[0][0]
    height = bottomleft[0][1]-topright[0][1]
    # return left, top, width, height
    return {'top':top, 'left':left, 'width':width, 'height':height}

def find(cls, itm, corner='center', save=0, duration=0):
    time_end = 0
    findings = []
    if duration > 0:
        time_end = time.time() + duration
    if not (os.path.isfile(f'{cls}/{itm}.png') and os.path.isfile(f'{cls}/test.png')):
        print (f'[find] FILE ERROR: {cls}, {itm}')
        return
    while 1:
        template = cv2.imread(f'{cls}/{itm}.png',cv2.IMREAD_UNCHANGED)
        image = cv2.imread(f'{cls}/test.png',cv2.IMREAD_UNCHANGED)

        h, w = template.shape[:-1]
        method = cv2.TM_SQDIFF

        res = cv2.matchTemplate(image, template, method, None, mask=template)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # create threshold from min val, find where sqdiff is less than thresh
        min_thresh = (min_val + 1e-6) * 1.25
        match_locations = np.where(res<=min_thresh)

        # draw template match boxes, scan from top left
        for (x, y) in zip(match_locations[1], match_locations[0]):
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
            print (findings[-1])
            if save:
                cv2.rectangle(image, (x, y), (x+w, y+h), [0,0,255,255], 1)
                cv2.rectangle(image, findings[-1], findings[-1], [200,255,200,255], 2)
                cv2.imwrite(f'runtime/{save}.png', image)
                # cv2.imshow('', image)
        if time.time() > time_end:
            break
        if duration != -1 and not findings:
            break

    return findings



def demo():
    while 1:
        t = time.time()
        ret = find('test',save=1)
        print (ret, 1/(time.time()-t))