import cv2
from matplotlib import pyplot as plt

# Convertendo para tons cinza

imagem1 = cv2.imread("imagem.jpg")
imagem2 = cv2.imread("imagem_gray.jpg")

cv2.imshow("Imagem RGB", imagem1)

color = ('b', 'g', 'r')

for channel, col in enumerate(color):
    hist = cv2.calcHist([imagem1], [channel], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.title('Histograma RGB')
plt.show()

cv2.waitKey(0)

cv2.imshow("Imagem GRAY", imagem2)

hist = cv2.calcHist([imagem2], [0], None, [256], [0, 256])
plt.plot(hist, color = 'gray')

plt.title('Histograma GRAY')
plt.show()

cv2.waitKey(0)