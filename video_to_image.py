import cv2
import csv
import os
import glob
import threading


def video_to_frame(start,end):
    rootPath = 'dataset/qia2020-3/test3/*.mp4'
    file_path = sorted(glob.glob(rootPath))
    for i in range(start, end):
        print(i)
        name = file_path[i][-11:-6]
        print(name)
        save_folder_path = "dataset/qia2020-3/image_frame_test3/" + str(name).zfill(5)

        video_file_path = (file_path[i])
        print(video_file_path)
        cap = cv2.VideoCapture(video_file_path)

        if not (os.path.isdir(save_folder_path)):
            os.makedirs(os.path.join(save_folder_path))

        count = 0
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                if(count%30==0):
                    save_file_path =  save_folder_path +"/" + name + "_{:d}.jpg".format(count)
                    cv2.imwrite(os.path.join(save_file_path), frame)
                count += 1
            else:
                break


range0 = 00000
range1 = 50000

t1 = threading.Thread(target=video_to_frame,args=(range0,range1 ))
t1.start()
t1.join()

print("Thread")
