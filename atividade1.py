import cv2

imagem = cv2.imread("imagem.jpg")

cv2.imshow("Original", imagem)

# Valores da imagem

print ("Imagem Original:\n")

print ("Altura (height): %d pixels" % imagem.shape[0]) 
print ("Largura (width): %d pixels" % imagem.shape[1])
print ("Canais (channels): %d\n"    % imagem.shape[2])

(b, g, r) = imagem[0, 0]
print ("Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = imagem[105, 150]
print ("Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = imagem[30, 150]
print ("Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d\n" % (r, g, b))

fatia = imagem[50:65, 170:190]

# Fatiando a imagem

#imagem[20:60, 10:50] = (0, 0, 255) // modifica as cores em um intervalo

(b1, g1, r1) = fatia[0][0]

for y in range(0, len(imagem)):
	for x in range(0, len(imagem[y])):
		
		(b2, g2, r2) = imagem[y][x]

		if (((b1 + 10) <= b2) or ((b1 - 10) >= b2) and
		    ((g1 + 10) <= g2) or ((g1 - 10) >= g2) and
		    ((r1 + 10) <= r2) or ((r1 - 10) >= r2)):
			continue

		else: imagem[y][x] = (0, 255, 0)

cv2.imshow("Imagem modificada", imagem)

cv2.waitKey(0)