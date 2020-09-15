import glob
import os
import cv2

save_path = 'resources/video_fotos.avi'
img_dir = "resources/orquidea/"

img_array = []
image_list = glob.glob(f"{img_dir}/*.jpg")
sorted_images = sorted(image_list, key=os.path.getmtime)
cont = len(image_list)
frames_per_seconds = 1
dims = 640, 480  # tamanho(largura, altura)

for filename in sorted_images:
	src = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
	img = cv2.resize(src, dims)
	height, width, layers = src.shape
	dim_o = (width, height)
	img_array.append(img)
	print("Fazendo ", cont)
	print(dim_o, dims)
	cont -= 1
# caminho ou nome do video, codec, frames por segundos, tamanho(largura, altura)
out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'DIVX'), frames_per_seconds, dims)

for i in range(len(img_array)):
	out.write(img_array[i])
	print("Construindo ", i)

clear_images = False
if clear_images:
	for file in image_list:
		os.remove(file)

cap = cv2.VideoCapture(save_path)

# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
cap.set(10, 100)  # brilho

while True:
	ok, im = cap.read()
	cv2.imshow("video", im)
	if cv2.waitKey(100) == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()
