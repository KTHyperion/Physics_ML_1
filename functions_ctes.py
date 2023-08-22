from vpython import *

"""
(1): A funcao phys_env retorna algumas constantes fisicas, como um starting point
para a velocidade, a aceleracao da gravidade (medida no IAG-USP), e
o passo temporal.

(2): A funcao decision_weight estipula um peso para a variacao que a maquina ira executar,
usando como base a comparacao entre a posicao cartesiana em cada eixo. Assim, temos que a
maquina ira alterar a velocidade para mais ou para menos naquela direcao. Nota-se que o
lancamento sera feito alterando apenas os parametros x e z, pois tanto o alvo quanto a bolinha
estao inicialmente na mesma altitude y = 0. (Este valor pode ser alterado neste documento.)
"""

def tests(): # Define o numero de estudos que o computador ira fazer.
    return 1000 # Sinta-se livre para alterar conforme quiser!

def phys_env(): # Nota (1)
    return vector(0, 10, 0), vector(0, -9.7864, 0), 0.001

def pos_init_A(): # Posicao da bolinha
    return vector(-25, 0, 0)

def pos_init_B (): # Posicao do alvo
    return vector(25, 0, 0)

def cartesianCSAxis(x, y, z, c): # Cria eixos cartesianos centrados em x, y e z, com a cor c.
    arrow(pos = vector(x, y, z), axis = vector(10, 0, 0), shaftwidth = 0.5, color = c) # x
    arrow(pos = vector(x, y, z), axis = vector(0, 10, 0), shaftwidth = 0.5, color = c) # y    
    arrow(pos = vector(x, y, z), axis = vector(0, 0, 10), shaftwidth = 0.5, color = c) # z

def decision_weight(obj1, obj2): # Nota (2)
    if obj1.pos.x > obj2.pos.x:
        w_x = -0.1
    elif obj1.pos.x == obj2.pos.x:
        w_x = 0
    elif obj1.pos.x < obj2.pos.x:
        w_x = 0.1

    if obj1.pos.z > obj2.pos.z:
        w_z = -0.1
    elif obj1.pos.z == obj2.pos.z:
        w_z = 0
    elif obj1.pos.z < obj2.pos.z:
        w_z = 0.1
    return w_x, w_z