import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def text_from_img(file_loc,crop_pixs = None):
    ''' 
    file_loc = path of file
    crop = list with [xl,xr,yl,yr]
    converts image to black and whtie and outputs text.
    '''
    img = cv2.imread(file_loc)
    if crop_pixs is not None:
        img = crop(img,crop_pixs)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)

    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    out = pytesseract.image_to_string(img)
    print(out)
    if __name__ == "__main__":
        cv2.imshow("img",img)
        cv2.waitKey(0)
    return out

def crop(img,pixels):
    return img[pixels[0]:pixels[1],pixels[2]:pixels[3]]
    
if __name__ =="__main__":
    pixs = [400,520,480,1500]
    text_from_img("screenshots\screen.png", pixs)
# cv2.imshow("img",img)
# cv2.waitKey(0)