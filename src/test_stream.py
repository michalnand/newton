import libs_common

key_read    = libs_common.KeyRead()

capture     = libs_common.CVCapture()


while True:
    key = key_read.read()
    if key != -1:
        print("key = ", key)
    if key == 'q':
        break
    im_raw_np, im_np = capture.get_frame()

    libs_common.cv_show(im_np)

