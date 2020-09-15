import cv2


cap = cv2.VideoCapture("resources/gaivotas.mp4")

while True:
	ok, img = cap.read()
	cv2.imshow("Video", img)
	if cv2.waitKey(100) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

