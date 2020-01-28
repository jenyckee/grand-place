import cv2
vidcap = cv2.VideoCapture('ccd019a1-524c-4b25-8174-9e6b611e7516.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1