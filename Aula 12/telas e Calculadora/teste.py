import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)


janela = QWidget()
janela.resize(400,400) # (x, y)

#Funções
def funcao_apertou():
    print("Você apertou o botão!")
    label.setText('SENAI')
    texto = linha_de_texto.text()
    label.setText(texto)
    
    
    
#CSS
with open('estilo_teste.css','r') as file:
    app.setStyleSheet(file.read())


#Inserindo elementos na tela
label= QLabel("QLabel",janela) #(O que vai escrito, onde é inserido)
label.setGeometry(10,5,380,20) # (x, y, largura,altura)
# label.setStyleSheet('background-color: blue;color:white; font-size: 20px; font: 14pt "MS Shell Dlg 2"; qproperty-alignment: AlignCenter;')

linha_de_texto = QLineEdit('',janela)
linha_de_texto.setGeometry(10,35,380,50)

botao = QPushButton('Enviar',janela)
botao.setGeometry(160,200,80,80)
botao.clicked.connect(funcao_apertou)
# botao.setStyleSheet('background-color: black;color:white; border-style: solid;border-color:red;border-width: 1px;border-radius: 5px;font-size: 20px;')

janela.show()
app.exec()


