import cv2
import pytesseract

img = cv2.imread('images/1.jpg')

rois = [
	((550, 820), (450, 520)),
	((520, 820), (510, 570)),
	((310, 820), (560, 630))
]
# while True:
h, w, _ = img.shape
print(h, w)
crop_img = img[100:1000, 0:1100]
draws_img = crop_img.copy()

for i, coords in enumerate(rois):
	sub_crop = crop_img[coords[1][0]:coords[1][1], coords[0][0]:coords[0][1]]
	text = pytesseract.image_to_string(sub_crop)
	print(f'Text found on ROI {1}: {text}')
	cv2.imshow(f'Sub {i}', sub_crop)
	cv2.rectangle(draws_img, (coords[0][0], coords[1][0]), (coords[0][1], coords[1][1]), (0, 255, 0), 2)

cv2.imshow('Frame', draws_img)

key = cv2.waitKey(0)
# if key == ord('q'):
# 	break

cv2.destroyAllWindows()