import libs_common
import numpy


key_read    = libs_common.KeyRead()

left_camera      = libs_common.CVCapture(camera=2)
right_camera     = libs_common.CVCapture(camera=0)


step = 0

while True:
    step+= 1
    key = key_read.read()
    if key != -1:
        print("key = ", key)
    if key == 'q':
        break

    im_left_raw_np, im_left_np   = left_camera.get_frame()
    im_right_raw_np, im_right_np = right_camera.get_frame()

    
    result = numpy.concatenate((im_left_raw_np, im_right_raw_np), axis=1)
    libs_common.cv_show(result)

