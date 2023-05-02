import cv2

# görüntüyü okuma
img = cv2.imread("D:\image_processing\parca1.jfif")

# Resmin boyutunu al
height, width = img.shape[:2]
# Resmi 400x400 boyutuna göre yeniden boyutlandır
resized_img = cv2.resize(img, (400, int(400 * (height / width))))

# parçanın renk aralığını belirleme
lower_color = (0, 0, 0) # koyu renkli bölgenin alt sınırı
upper_color = (50, 50, 50) # koyu renkli bölgenin üst sınırı

# görüntüyü HSV renk uzayına dönüştürme
hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

# renk aralığına göre maske oluşturma
mask = cv2.inRange(hsv, lower_color, upper_color)

# maskeyi görüntüye uygulama
res = cv2.bitwise_and(resized_img, resized_img, mask=mask)

# maske üzerinde kontur bulma
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# konturları döngüye alarak en büyük konturu bulma
max_contour = max(contours, key=cv2.contourArea)

# en büyük konturu çerçeve içine alma
x,y,w,h = cv2.boundingRect(max_contour)
cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),2)

# görüntüyü gösterme
cv2.imshow('Orjinal Görüntü', resized_img)
cv2.imshow('Parca', res)

#cv2.resizewindow('orjinal görüntü', 400,400)
#cv2.resizewindow('parca', 400,400)

cv2.waitKey(0)
cv2.destroyAllWindows()
