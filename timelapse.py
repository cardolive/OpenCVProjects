# joincfe.com/github/
# lessons/
# https://www.youtube.com/playlist?list=PLEsfXFp6DpzRyxnU-vfs3vk-61Wpt7bOS
import datetime
import time
import os
import cv2
import glob

from utils import CFEVideoConf

cap = cv2.VideoCapture(0)


def make_1080p():
	cap.set(3, 1920)  # width
	cap.set(4, 1080)  # height


def make_720p():
	cap.set(3, 1280)
	cap.set(4, 720)


def make_480p():
	cap.set(3, 640)
	cap.set(4, 480)


def change_res(width, height):
	cap.set(3, width)
	cap.set(4, height)


def rescale_frame(quadro, percent=75):
	width = int(quadro.shape[1] * percent / 100)
	height = int(quadro.shape[0] * percent / 100)
	dim = (width, height)
	return cv2.resize(quadro, dim, interpolation=cv2.INTER_AREA)


save_path = 'resources/timelapse.avi'
frames_per_seconds = 24.0
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
seconds_duration = 15
seconds_between_shots = .30

timelapse_img_dir = "resources/timelapse/"
# se o diretório não existir, cria
if not os.path.exists(timelapse_img_dir):
	os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=seconds_duration)

i = 0

# make_480p()  # setando o tamanho do video

while datetime.datetime.now() < finish_time:
	# Capture frame-by-frame
	ret, frame = cap.read()
	filename = f"{timelapse_img_dir}/{i}.jpg"
	i += 1
	cv2.imwrite(filename, frame)
	# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# out.write(frame)
	# Display the resulting frame
	# cv2.imshow('frame',frame)
	print("Fazendo...", i)
	time.sleep(seconds_between_shots)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# clear_images = True


def images_to_video(vw, img_dir, clear_images=True):
	image_list = glob.glob(f"{img_dir}/*.jpg")
	sorted_images = sorted(image_list, key=os.path.getmtime)
	for file in sorted_images:
		image_frame = cv2.imread(file)
		vw.write(image_frame)
	if clear_images:
		for file in image_list:
			os.remove(file)


images_to_video(out, timelapse_img_dir, clear_images=True)
# When everything done, release the capture


# mostrando o video feito

vdcap = cv2.VideoCapture(save_path)

vdcap.set(3, 640)  # width
vdcap.set(4, 480)  # height
vdcap.set(10, 100)  # brilho

while True:
	ok, im = vdcap.read()
	cv2.imshow("video", im)
	if cv2.waitKey(100) == ord('q'):
		break

vdcap.release()
cap.release()
out.release()
cv2.destroyAllWindows()
