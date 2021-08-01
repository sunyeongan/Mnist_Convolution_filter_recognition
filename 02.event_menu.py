from paint_init import *
from paint_utils import *

image = np.full((500, 900, 3), 255, np.uint8)
icons = place_icons(image, (60, 60))
x,y,w,h = icons[-1]

palette_roi = (0,y+h+2, 120, 120)
hueIndex_roi = (0,y+h+124, 120, 15)
icons.append(palette_roi)
icons.append(hueIndex_roi)
create_colorPlatte(image,0,icons[PALETTE])
create_hueIndex(image,icons[HUE_IDX])

cv2.imshow("paintCV",image)
cv2.waitKey(0)