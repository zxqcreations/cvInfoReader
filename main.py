import cv2, time

cap = cv2.VideoCapture(cv2.CAP_DSHOW+0)

old_width=0
old_height=0

wids = [3840, 1920, 1600, 1280, 800, 640, 640, 352, 320, 176, 160]
heis = [2160, 1080, 1200, 720,  600, 480, 360, 288, 240, 144, 120]
resi = 0
print('\n--------------------[INFO]--------------------\n')
while True:
    
    ret, img = cap.read();
    #print(img)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cv2.putText(img,str(width)+' '+str(height), (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255))
    cv2.imshow('cv', img)
    k = cv2.waitKey(10)
    if k==32:
        break
    if k==115:
        
        print('[INFO] Setting Resolution to' + str((wids[resi],heis[resi])))
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, wids[resi])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, heis[resi])
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('[INFO] resolution was set to' + str((width, height)))
        
        if width == wids[resi] and height == heis[resi]:
            print('[INFO] ' + str((wids[resi],heis[resi])) + ' is OK! index=' + str(resi))
        resi=resi+1 if resi<len(wids)-1 else 0

        print('----------------------------------------------')

cap.release()
cv2.destroyAllWindows()
