import cv2
import os
path="Images/"
images=[]
for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in [".gif",".png",".jpg"]:
        file_name=path+"/"+file
        images.append(file_name)
count=len(images)
frame=cv2.imread(images[0])
height,width,channel=frame.shape
size=(width,height)
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
print("done")