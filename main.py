from functions_ctes import *
from random import randint

# Criacao de um ambiente fisico / parametros iniciais
v_init, a, dt = phys_env();

# Criacao dos objetos
bola = sphere(pos = pos_init_A(), color = color.cyan);
alvo = sphere(pos = pos_init_B(), color = color.green);
cartesianCSAxis(0, 0, 0, color.yellow);

# Pesos e posicoes iniciais
p_init_x, p_init_z = decision_weight(bola, alvo)
dist_init = mag(bola.pos - alvo.pos)

# Trecho de aprendizado
for i in range( int( tests() ) ):

    # Variacao da velocidade conforme os pesos
    v_init = v_init + vector(p_init_x, 0, p_init_z)

    # Montagem de duas novas velocidades, uma com o valor inicial em si, outra com o valor permitindo variacoes
    v_con = v_init
    v_var = v_init

    # Reset da posicao da bolinha principal
    bola.pos = pos_init_A()

    # Execucao do movimento usando-se dos parametros iniciais
    while bola.pos.y >= 0:
        bola.pos = bola.pos + v_var * dt    
        v_var = v_var + a * dt
    
    # Obtendo a distancia final
    dist = mag(bola.pos - alvo.pos)

    # Tomada de decisao
    if dist <= dist_init:
        v_init = v_con
        dist_init = dist

    # Estipulacao de novos pesos pre-reset
    p_init_x, p_init_y = decision_weight(bola, alvo)

bola.pos = pos_init_A()

# Definindo uma curva-guia para fins esteticos.
c = curve(color = color.red)

# Display principal do movimento, com 1000 iteracoes/s
while bola.pos.y >= 0:
    rate(1000)

    bola.pos = bola.pos + (v_init * dt)
    v_init = v_init + (a * dt)

    c.append(bola.pos)