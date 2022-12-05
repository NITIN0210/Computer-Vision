import numpy as np
import cv2

imgPath1=["buildingsSet1/rialto_team6-1.jpeg","buildingsSet1/rialto_team6-2.jpeg","buildingsSet1/rialto_team6-3.jpeg"]

#imgPath2=["buildingsSet2/sportsarena1","buildingsSet2/sportsarena2","buildingsSet2/sportsarena3"]

#imgPath3=["buildingsSet3/studentcenterwest1","buildingsSet3/studentcenterwest2","buildingsSet2/studentcenterwest3"]

#imgPath4=["buildingsSet4/urbanlife1.jpg","buildingsSet4/urbanlife2.jpg","buildingsSet4/urbanlife3.jpg"]

#imgPath5=["buildingsSet5/Art and humanities01_team6.jpg","buildingsSet5/Art and humanities02_team6.jpg","buildingsSet5/Art and humanities03_team6.jpg"]

imagePathArr = [imgPath1]
''',imgPath2,imgPath3,imgPath4,imgPath5'''
images = []

j=1
for i in imagePathArr:	
	images = []
	for path in i:
		image = cv2.imread(path)
		images.append(image)
	print(len(images))
	stitcher = cv2.Stitcher_create()
	(status, stitched) = stitcher.stitch(images)

	if status == 0:
		print("Image Stitching Successful")
		cv2.imshow("Stitched Image", stitched)
		cv2.imwrite("stichedSet" + str(j) +  ".png",stitched)
	else:
		print("[INFO] Failed Image Stitching ({})".format(status))
	j+=1
