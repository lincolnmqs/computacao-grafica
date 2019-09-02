import cv2

# Convertendo para tons cinza

imagem = cv2.imread("imagem.jpg")

# cv2.imshow('Imagem Original', imagem)

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem - Filtro GRAY', gray)

# cv2.imwrite("imagem_gray.jpg", gray) # gera nova imagem   

fatia = gray[50:65, 170:190]

# cv2.imshow('Imagem Fatiada', fatia1)

val1 = fatia[0][0]
escuro = gray[0][0]

for y in range(0, len(gray)):
	for x in range(0, len(gray[y])):
		
		val2 = gray[y][x]

		if (((val1 + 30) <= val2) or ((val1 - 30) >= val2)):
			continue

		else: gray[y][x] = escuro

cv2.imshow("Imagem modificada", gray)

cv2.waitKey(0)
