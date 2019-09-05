import cv2
import numpy as np
import keyboard
def draw_hist(name, gray):
    hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    
    MAX = max(hist)
    plot = np.zeros((512,1024))
    for i in range(255):
        x1 = 4*i
        x2 = 4*(i+1)
        y1 = hist[i]*512/MAX
        y2 = hist[i+1]*512/MAX
        cv2.line(plot, (x1,y1), (x2,y2), 1, 3)
    cv2.imshow(name + "-gray", gray)
    cv2.imshow(name + "-hist", plot)


def main():
   clahe = cv2.createCLAHE()
   cam = cv2.VideoCapture(0)
   while True:
      ret, img = cam.read()
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      claheEq = clahe.apply(gray)
      frame4 = cv2.equalizeHist(gray)
      draw_hist("cam",gray)
      draw_hist("CLAHE", claheEq)
      draw_hist("Global Equalizer", frame4)
      
      key = cv2.waitKey(1)

      if keyboard.is_pressed('q'):
         break

if __name__=="__main__":
    main()

