import cv2
import numpy as np
import pytesseract

img = cv2.imread('images/1.jpg')
h, w = img.shape[:2]

print(h, w)

rois = [
	((190, 100), (800, 210)),
	((940, 100), (1550, 230)),
	((1690, 140), (2240, 270)),

	((190, 1890), (800, 2000)),
	((940, 1890), (1530, 2000)),
	((1620, 1880), (2170, 2010)),

]

LOW = np.array([0, 0, 0])
UPP = np.array([180, 255, 150])

# while True:
tags = []
img_copy = img.copy()

resized_image = cv2.resize(img_copy, (1024, 720))
cv2.imshow('Frame', resized_image)

for roi in rois:
	cv2.rectangle(img_copy, roi[0], roi[1], (0, 255, 0), 5)
	# Calculate roi center
	center_x = int((roi[1][0] - roi[0][0])/2 + roi[0][0])
	center_y = int((roi[1][1] - roi[0][1])/2 + roi[0][1])

	upp_left = (center_x - 350, center_y - 80)
	low_right = (upp_left[0] + 650, upp_left[1] + 1850)
	tag_roi = (upp_left, low_right)
	# print('roi')
	# print(roi)
	# print('tag_roi')
	# print(tag_roi)
	# print('\n')
	# print('\n')

	tag_img = img_copy[upp_left[1]:low_right[1], upp_left[0]:low_right[0]]
	tags.append(tag_img)

	resized_image = cv2.resize(img_copy, (1024, 720))
	cv2.imshow('Frame', resized_image)
	cv2.waitKey(1000)
	# cv2.rectangle(img_copy, tag_roi[0], tag_roi[1], (0, 0, 255), 5)

text_coords = ((20, 1000), (620, 1400))
for i, tag in enumerate(tags):
	h, w = tag.shape[:2]
	print(h, w)

	sub_crop = tag[text_coords[1][0]:text_coords[1][1], text_coords[0][0]:text_coords[0][1]]
	text = pytesseract.image_to_string(sub_crop)
	print(f'Text found on ROI {1}: {text}')
	# cv2.imshow(f'Sub {i}', sub_crop)
	# cv2.rectangle(draws_img, (coords[0][0], coords[1][0]), (coords[0][1], coords[1][1]), (0, 255, 0), 2)

	cv2.rectangle(tag, text_coords[0], text_coords[1], (0, 255, 0), 5)
	# resized_tag = cv2.resize(tag, (1024, 720))
	# cv2.imshow(f'{i}', resized_tag)
	resized_image = cv2.resize(img_copy, (1024, 720))
	cv2.imshow('Frame', resized_image)
	cv2.waitKey(1000)


resized_image = cv2.resize(img_copy, (1024, 720))
cv2.imshow('Frame', resized_image)

key = cv2.waitKey(1)
	# if key == ord('q'):
	# 	break

cv2.destroyAllWindows()
