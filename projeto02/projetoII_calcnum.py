import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# truncar um número por conta de erros de aproximação de float
# exemplo: na terceira iteração do loop nos métodos, em vez de x = 1.2, x = 1.20000000000000002
def truncar(num: float, casas_decimais: int) -> float:
    fator = 10 ** casas_decimais
    
    return math.trunc(num * fator) / fator

def funcao(x, y):
    return 1/(x**2) - y/x - y**2

def euler_aperfeicoado(h: float, x_min: float, x_max: float, y_inicial: float) -> list:
    x = x_min
    y = y_inicial
    pontos_x = []
    pontos_y = [y_inicial]

    # aplica o método de Euler Aperfeiçoado
    while (x < x_max):
        k1 = funcao(x, y)
        k2 = funcao(x + h, y + h*k1)
        y = y + (h/2) * (k1 + k2) # fórmula do método
        pontos_y.append(y) # adiciona os pontos na lista
        pontos_x.append(x)
        x = truncar(x + h, 1)

    pontos_x.append(x_max) # falta inserir o último x na lista

    return pontos_x, pontos_y

def runge_kutta_ordem_4(h: float, x_min: float, x_max: float, y_inicial: float) -> list:
    x = x_min
    y = y_inicial
    pontos_y = [y_inicial]

    # aplica o método de Runge-Kutta de 4ª ordem
    while (x < x_max):
        k1 = funcao(x, y)
        k2 = funcao(x + h/2, y + h*k1/2)
        k3 = funcao(x + h/2, y + h*k2/2)
        k4 = funcao(x + h, y + h*k3)
        y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4) # fórmula do método
        pontos_y.append(y) # adiciona os pontos na lista
        x = truncar(x + h, 1)

    return pontos_y

# gera os pontos da solução analítica para colocar no gráfico
def pontos_analiticos(x_min, x_max) -> list:
    h = 0.0001
    x = x_min
    pontos_x = []
    pontos_y = []

    while (x <= x_max):
        y = -1/x
        pontos_x.append(x)
        pontos_y.append(y)
        x += h

    return pontos_x, pontos_y

# faz o gráfico dos três métodos e o imprime na tela
def grafico(x: list, y_euler: list, y_rk: list, x_analitico: list, y_analitico: list):
    fig, varx = plt.subplots()
    varx.plot(x, y_euler, label = 'Euler Aperfeiçoado')
    varx.plot(x, y_rk, label = 'Runge-Kutta de 4ª ordem')
    varx.plot(x_analitico, y_analitico, label = 'Solução Analítica')
    varx.set_xlabel('Pontos xi')
    varx.set_ylabel('Aproximações yi')
    varx.set_title('Pontos xi x Aproximações yi')
    varx.legend()
    plt.show()

pontos_xi, pontos_yi_euler = euler_aperfeicoado(0.1, 1.0, 2.0, -1.0)
print(f'Aproximações por Euler Aperfeiçoado: {pontos_yi_euler}')
print('')

pontos_yi_rk = runge_kutta_ordem_4(0.1, 1.0, 2.0, -1.0)
print(f'Aproximações por Runge-Kutta de 4ª ordem: {pontos_yi_rk}')

pontos_xi_analiticos, pontos_yi_analiticos = pontos_analiticos(1.0, 2.0)
grafico(pontos_xi, pontos_yi_euler, pontos_yi_rk, pontos_xi_analiticos, pontos_yi_analiticos)

# Fim da Parte 1

# faz a tabela comparativa dos pontos
def tabela(lista1: list, lista2: list, lista3: list):
    table = pd.DataFrame()
    table['t'] = lista1
    table['P(t) - odeint'] = lista2
    table['P(t) - sol. exata'] = lista3
    print(table)
    table.to_excel('Tabela_Parte2_PCII.xlsx', index = False)

# define uma lista contendo os pontos da solução exata calculada em cada t
def sol_exata() -> list:
    pontos = []
    for i in range(9):
        t = i * 10
        e = math.e
        pontos.append((89.7617 * (e**(0.02*t))) / (1 + 0.1795 * (e**(0.02*t))))

    return pontos

# retorna a derivada de P
def model(P, t):
    a = 0.02
    b = 0.00004

    dPdt = a*P - b*(P**2)

    return dPdt

# calcula a EDO utilizando odeint() e faz a tabela de pontos comparando os dois métodos
def edo(P_inicial: float):
    t = np.linspace(0, 80, 9)
    P = odeint(model, P_inicial, t)
    exata = sol_exata()

    for i in range(len(P)):
        P[i] = truncar(float(P[i]), 6) # não tem como ter frações de habitantes

    tabela(t.tolist(), P, exata)

edo(76.1)

# Fim da Parte 2