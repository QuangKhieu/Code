import cv2

catFaceCascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')



image = cv2.imread('D:\Quang\jpg\cats2.jpg')
cv2.imshow("test,image",image)

faces = catFaceCascade.detectMultiScale(image)
if len(faces) == 0:
 print("No faces found")

else:
 print("Number of faces detected: " + str(faces.shape[0]))

 for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))

 cv2.imshow('Image with faces', image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
