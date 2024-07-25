#Algoritmo de rasterização de pontos de Bresenham
import matplotlib.pyplot as plt

def rasterizacao(x1, y1, x2, y2):
    dx = x2 - x1 
    dy = y2 - y1
    d = 2 * dy - dx
    incremento_E = 2 * dy
    incremento_NE = 2 * (dy - dx)
    
    x = x1
    y = y1
    pontos = [(x, y)]
    
    while not (x == x2 and y == y2):
        if d <= 0:
            d += incremento_E
            x += 1
        else:
            d += incremento_NE
            x += 1
            y += 1
        pontos.append((x, y))
    
    return pontos


x1 = int(input('x1:'))
y1 = int(input('y1:'))
x2 = int(input('x2:'))
y2 = int(input('y2:'))

pontos = rasterizacao(x1, y1, x2, y2)

x_coords, y_coords = zip(*pontos)

# Plotagem
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'bo-', label='Segmento de Reta')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Algoritmo de Bresenham para Rasterização de Segmento de Reta')
plt.grid()
plt.legend()
plt.show()
