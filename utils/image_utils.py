from PIL import ImageGrab
import numpy as np

def capture_screen_bbox(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    arr = np.array(img)
    return arr[:, :, ::-1].copy() 
