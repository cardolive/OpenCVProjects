import cv2
import numpy as np

img = cv2.imread("resources/planta.jpg")
print(img.shape)
print("hight, width, channel bgr")
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
redimecionar = cv2.resize(img, (1026, 906))

# borrado = cv2.GaussianBlur(cinza, (7, 7), 0)
# borda = cv2.Canny(img, 50, 50)
# kernel = np.ones((1, 2), np.uint8)
# precissaoBorda = cv2.dilate(borda, kernel, iterations=1)
# afinar = cv2.erode(precissaoBorda, kernel, iterations=1)

cv2.imshow("original", img)
cv2.imshow("cinza", cinza)
cv2.imshow("maior", redimecionar)
# cv2.imshow("borrado", borrado)
# cv2.imshow("borda", borda)
# cv2.imshow("precissao", precissaoBorda)
# cv2.imshow("afinar", afinar)
cv2.waitKey(0)   # 0 mostra sempre, 1000 mostra por 1 min

if cv2.waitKey(0) == ord('q'):
	cv2.destroyAllWindows()

