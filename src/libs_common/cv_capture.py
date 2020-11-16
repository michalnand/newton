import numpy
import cv2
from PIL import Image

class CVCapture:
    def __init__(self, camera = 0, height = 128, width = 128, raw_height=240, raw_width=320, fps=10):
        self.cap    = cv2.VideoCapture(camera)
        self.height = height
        self.width  = width

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(raw_width))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(raw_height))
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def get_frame(self):
        ret, frame = self.cap.read()

        if ret == True:
            im = Image.fromarray(frame, "RGB")
            self.im_raw_np = self._normalize(numpy.array(im))

            im = im.resize((self.height, self.width))

            self.im_np = numpy.array(im)
            self.im_np = self._normalize(self._rgb2gray(self.im_np))

        return self.im_raw_np, self.im_np
        
    def _rgb2gray(self, rgb_image):
        return numpy.dot(rgb_image[...,:3], [0.299, 0.587, 0.144])

    def _normalize(self, x):
        max = numpy.max(x)
        min = numpy.min(x)

        k   = 1.0/(max - min)
        q   = 1.0 - k*max

        return k*x + q


if __name__ == "__main__":
    capture = CVCapture()

    im_raw_np, im_np = capture.get_frame()
    
    print(">>>> ", im_np.min(), im_np.max())
    print(">>>> ", im_raw_np.min(), im_raw_np.max())