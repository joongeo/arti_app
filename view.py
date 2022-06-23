import cv2
import os
import glob

#saves target dir
file_list = glob.glob('/Users/joong/.pyenv/versions/3.10.0/envs/metabox/uploads/*')
#saves latest file path
latest_file = max(file_list, key = os.path.getctime)

im = cv2.imread(latest_file)
cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(latest_file)
