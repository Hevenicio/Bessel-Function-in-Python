#Feito por Hevenicio Silva

# Importação de biblitecas
from IPython.display import display, Markdown, Latex
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import numpy as np

# Entrada de dados
dados = pd.read_csv("dados.csv")
df = pd.DataFrame(dados)

# Função Fatorial
def fatorial(n):
    if(n == 0):
        return 1
    else:
        return n*fatorial(n - 1)


# Formatação dos dados impressos - Latex
def printmd(string):
    display(Markdown(string))
    #display(Latex(string))

f = sym.symbols('$_{0}$')
g = sym.symbols('$_{1}$')
h = sym.symbols('$_{2}$')


# Definindo as Funções de Bessel
def J0(x):
    k = 0
    soma = 0
    termo = 1
    while(1.0e-4 <= termo):
        termo = pow(x/2, (2*k))/(fatorial(k)*fatorial(k))
        soma += pow(-1, k)*termo
        k += 1
    return soma

def J1(x):
    k = 0
    soma = 0
    termo = 1
    while(1.0e-4 <= termo):
        termo = pow(x/2, (2*k + 1))/(fatorial(k)*fatorial(k + 1))
        soma += pow(-1, k)*termo
        k += 1
    return soma

def J2(x):
    k = 0
    soma = 0
    termo = 1
    while(1.0e-4 <= termo):
        termo = pow(x/2, (2*k + 2))/(fatorial(k)*fatorial(k + 2))
        soma += pow(-1, k)*termo
        k += 1
    return soma

# Amplitude da função de Bessel
y = np.sqrt(2/(np.pi*df['entrada']))

z = -np.sqrt(2/(np.pi*df['entrada']))

# Resultados obtidos
l =[]
m = []
n = []
o = []
p = [l, m, n, o]
for i in df['entrada']:
    l.append(i)
    m.append(J0(i))
    n.append(J1(i))
    o.append(J2(i))
    #printmd('**$J${}({}):  {: 0.5f} $|$ $J${}({}):  {: 0.5f} $|$ $J${}({}):  {: 0.5f}**'.format(f, i, J0(i), g, i, J1(i), h, i, J2(i)))
    a = pd.DataFrame(p)
a = a.rename(index={0:"x", 1:"J0(x)", 2: "J1(x)", 3:"J2(x)"}).T
print(a)

# Plotando os resultados obtidos
plt.title('Funções de Bessel - J$_{0}(x)$, J$_{1}(x)$ e J$_{2}(x)$')
plt.plot(df['entrada'], m, 'g', label = 'J$_{0}(x)$')
plt.plot(df['entrada'], n, 'limegreen', label = 'J$_{1}(x)$')
plt.plot(df['entrada'], o, 'lawngreen', label = 'J$_{2}(x)$')
plt.plot(df['entrada'], y, 'c--', label = '$\sqrt{2 / \pi x}$')
plt.plot(df['entrada'], z, 'b--', label = '$ - \sqrt{2 / \pi x}$')
plt.legend(framealpha=1, frameon=True)
plt.grid(color = 'black')
plt.style.use('seaborn')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()