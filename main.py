
# packages
import cv2
import numpy as np
import pyautogui as pg


screenshot = pg.screenshot()

screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

#

# detect several objects on screenshot
for pawn in pg.locateAllOnScreen('pawn4.png', confidence=0.95):
    # draw rectangle around the object
    print(pawn)
    cv2.rectangle(
        screenshot,
        (pawn.left, pawn.top),
        (pawn.left + pawn.width, pawn.top + pawn.height),
        (0, 0, 255),
        2
    )


crop_image = screenshot[221: 221 + 741, 114: 144 + 743]


cv2.imshow('Screenshot', crop_image)


#Box(left=114, top=221, width=743, height=741)
# escape condition
cv2.waitKey(0)

# clean up windows
cv2.destroyAllWindows()