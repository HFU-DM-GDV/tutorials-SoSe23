# hint about reading image data came from https://stackoverflow.com/questions/17170752/python-opencv-load-image-from-byte-string

import cv2
import numpy as np
import requests
import html


# grab some image from the web and optionally save it
def grab_image(query, save_image=False, filename="image.jpg"):
    response = requests.get("https://source.unsplash.com/random{0}".format(html.escape(query)))
    # that does not work like this
    nparr = np.frombuffer(response.content, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("result", img_np)
    if save_image:
        cv2.imwrite(filename, img_np)
    cv2.waitKey(0)
    return img_np


query = input("Enter your query: ")
grab_image('/1280x720/?' + query, True, "{0}.jpg".format(query))