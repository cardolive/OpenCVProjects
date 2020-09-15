import cv2

# url = 'rtsp://kardopoly:v1c4l1v3@10.0.0.124:554/cam/realmonitor?channel=1&subtype=0'
# url = 0  # webcam do computador
# 1 webcam auxiliar (usb)

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brilho

# cap2 = cv2.VideoCapture(1)
# cap2.set(3, 640)  # width
# cap2.set(4, 480)  # height
# cap2.set(10, 100)  # brilho


def seg_cam(capt):
	ok2, img2 = capt.read()
	cv2.imshow("camera2", img2)


while True:
	ok, img = cap.read()
	cv2.imshow("camera", img)
	# seg_cam(cap2)
	if cv2.waitKey(100) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
