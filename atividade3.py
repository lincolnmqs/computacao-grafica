import cv2

# Convertendo para HSV

imagem = cv2.imread("imagem.jpg")

# cv2.imshow('Imagem Original', imagem)

hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
cv2.imshow('Imagem - Filtro HSV', hsv)

# cv2.imwrite("imagem_hsv.jpg", hsv) # gera nova imagem   

imagem1 = cv2.imread("imagem_hsv.jpg")

fatia = imagem1[50:65, 170:190]

# cv2.imshow('Imagem Fatiada', fatia1)

(h1, s1, v1) = fatia[0][0]

for y in range(0, len(imagem1)):
	for x in range(0, len(imagem1[y])):
		
		(h2, s2, v2) = imagem1[y][x]

		if (((h1 + 10) <= h2) or ((h1 - 10) >= h2) and
		    ((s1 + 10) <= s2) or ((s1 - 10) >= s2) and
		    ((v1 + 10) <= v2) or ((v1 - 10) >= v2)):
			continue

		else: imagem1[y][x] = (255, 0, 0)

cv2.imshow("Imagem modificada", imagem1)

cv2.waitKey(0)