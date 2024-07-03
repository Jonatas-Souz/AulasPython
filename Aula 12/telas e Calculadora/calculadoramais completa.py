import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(345,550)

operador1 = QLineEdit('')
operador2 = QLineEdit('')
sinal = QLineEdit('')

def raiz():
    operador1.setText(visor.text())
    sinal.setText('R')
    visor.setText("")

def potencia():
    operador1.setText(visor.text())
    sinal.setText('*')
    visor.setText("")

def divisao():
    operador1.setText(visor.text())
    sinal.setText('/')
    visor.setText("")

def porcentagem():
    operador1.setText(visor.text())
    sinal.setText('%')
    visor.setText("")

def multiplicar():
    operador1.setText(visor.text())
    sinal.setText('x')
    visor.setText("")

def subtrair():
    operador1.setText(visor.text())
    sinal.setText('-')
    visor.setText("")

def somar():
    operador1.setText(visor.text())
    sinal.setText('+')
    visor.setText("")

def calcular():
    operador2.setText(visor.text())

    if sinal.text() == '+':
        somaValores = float(operador1.text()) + float(operador2.text())
        visor.setText(str(somaValores))
    if sinal.text() == '-':
        somaValores = float(operador1.text()) - float(operador2.text())
        visor.setText(str(somaValores))
    if sinal.text() == 'x':
        somaValores = float(operador1.text()) * float(operador2.text())
        visor.setText(str(somaValores))
    if sinal.text() == '/':
        somaValores = float(operador1.text()) / float(operador2.text())
        visor.setText(str(somaValores))
    if sinal.text() == '%':
        somaValores = float(operador1.text()) /100* float(operador2.text())
        visor.setText(str(somaValores))
    if sinal.text() == '*':
        potValores = float(operador1.text()) ** int(operador2.text())
        visor.setText(str(potValores))
    if sinal.text() == 'R':
        somaValores = float(operador1.text()) **  1/(int(operador2.text()))
        visor.setText(str(somaValores))

def zerar():
    visor.setText('')

def exibirNoVisor(valor):
    print(valor)
    conteudoVisor = visor.text() + valor
    visor.setText(conteudoVisor)

visor = QLineEdit('',janela)
visor.setGeometry(5,5,335,100)

with open('style.css', 'r') as file:
    app.setStyleSheet(file.read())

#linha 1
btnNumeroC = QPushButton('C', janela)
btnNumeroC.setGeometry(5,120,80,80)
btnNumeroC.clicked.connect(zerar)

btnNumero2 = QPushButton('R', janela)
btnNumero2.setGeometry(90,120,80,80)
btnNumero2.clicked.connect(raiz)

btnNumero3 = QPushButton('%', janela)
btnNumero3.setGeometry(175,120,80,80)
btnNumero3.clicked.connect(porcentagem)

btnNumero4 = QPushButton('/', janela)
btnNumero4.setGeometry(260,120,80,80)
btnNumero4.clicked.connect(divisao)

#linha 2
btnNumero7 = QPushButton('7', janela)
btnNumero7.setGeometry(5,205,80,80)
btnNumero7.clicked.connect(lambda: exibirNoVisor('7'))

btnNumero8 = QPushButton('8', janela)
btnNumero8.setGeometry(90,205,80,80)
btnNumero8.clicked.connect(lambda: exibirNoVisor('8'))

btnNumero9 = QPushButton('9', janela)
btnNumero9.setGeometry(175,205,80,80)
btnNumero9.clicked.connect(lambda: exibirNoVisor('9'))

btnNumeroX = QPushButton('x', janela)
btnNumeroX.setGeometry(260,205,80,80)
btnNumeroX.clicked.connect(multiplicar)


# linha 3
btnNumero4 = QPushButton('4', janela)
btnNumero4.setGeometry(5,290,80,80)
btnNumero4.clicked.connect(lambda: exibirNoVisor('4'))

btnNumero5 = QPushButton('5', janela)
btnNumero5.setGeometry(90,290,80,80)
btnNumero5.clicked.connect(lambda: exibirNoVisor('5'))

btnNumero6 = QPushButton('6', janela)
btnNumero6.setGeometry(175,290,80,80)
btnNumero6.clicked.connect(lambda: exibirNoVisor('6'))


btnNumeroMenos = QPushButton('-', janela)
btnNumeroMenos.setGeometry(260,290,80,80)
btnNumeroMenos.clicked.connect(subtrair)

#linha 4
btnNumero1 = QPushButton('1', janela)
btnNumero1.setGeometry(5,375,80,80)
btnNumero1.clicked.connect(lambda: exibirNoVisor('1'))

btnNumero2 = QPushButton('2', janela)
btnNumero2.setGeometry(90,375,80,80)
btnNumero2.clicked.connect(lambda: exibirNoVisor('2'))

btnNumero3 = QPushButton('3', janela)
btnNumero3.setGeometry(175,375,80,80)
btnNumero3.clicked.connect(lambda: exibirNoVisor('3'))

btnNumeroMais = QPushButton('+', janela)
btnNumeroMais.setGeometry(260,375,80,80)
btnNumeroMais.clicked.connect(somar)

#linhaa 5
btnNumeroPotencia = QPushButton('*', janela)
btnNumeroPotencia.setGeometry(5,460,80,80)
btnNumeroPotencia.clicked.connect(potencia)

btnNumero0 = QPushButton('0', janela)
btnNumero0.setGeometry(90,460,80,80)
btnNumero0.clicked.connect(lambda: exibirNoVisor('0'))


btnNumero15 = QPushButton('.', janela)
btnNumero15.setGeometry(175,460,80,80)
btnNumero15.clicked.connect(lambda: exibirNoVisor('.'))

btnNumeroIgual = QPushButton('=', janela)
btnNumeroIgual.setGeometry(260,460,80,80)
btnNumeroIgual.clicked.connect(calcular)







janela.show()
app.exec()