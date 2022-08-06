# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
from multiprocessing import Pool, cpu_count
from time import time


from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox

from global_alignment import GlobalAlignment
from local_alignment import LocalAlignment
from score import Score

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import matplotlib.pyplot as plt


from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

score = Score(
    match=10,
    mismatch=-5,
    gap=-7
)

cbx=""
tempoSequencial = []
tempoParalelo = []
class Ui_frmPrincipal(QMainWindow):
    def setupUi(self, frmPrincipal):
        frmPrincipal.setObjectName("frmPrincipal")
        frmPrincipal.resize(721, 568)
        self.centralWidget = QtWidgets.QWidget(frmPrincipal)
        self.centralWidget.setObjectName("centralWidget")
        self.txtCaminho = QtWidgets.QLineEdit(self.centralWidget)
        self.txtCaminho.setGeometry(QtCore.QRect(240, 76, 351, 20))
        self.txtCaminho.setObjectName("txtCaminho")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 381, 31))
        self.label_2.setObjectName("label_2")
        self.lstSenquncia = QtWidgets.QTextEdit(self.centralWidget)
        self.lstSenquncia.setGeometry(QtCore.QRect(20, 120, 671, 331))
        self.lstSenquncia.setObjectName("lstSenquncia")
        self.btnProcurar = QtWidgets.QPushButton(self.centralWidget)
        self.btnProcurar.setGeometry(QtCore.QRect(600, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnProcurar.setFont(font)
        self.btnProcurar.setObjectName("btnProcurar")
        self.btnProcurar.clicked.connect(self.clickCaminho)
        self.btnAlinhar = QtWidgets.QPushButton(self.centralWidget)
        self.btnAlinhar.setGeometry(QtCore.QRect(30, 470, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAlinhar.setFont(font)
        self.btnAlinhar.setObjectName("btnAlinhar")
        self.btnAlinhar.clicked.connect(self.clickAlinha)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 271, 31))
        self.label.setObjectName("label")
        self.btnSair = QtWidgets.QPushButton(self.centralWidget)
        self.btnSair.setGeometry(QtCore.QRect(600, 470, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSair.setFont(font)
        self.btnSair.setObjectName("btnSair")
        self.btnSair.clicked.connect(self.clickSair)
        self.btnCpu = QtWidgets.QPushButton(self.centralWidget)
        self.btnCpu.setGeometry(QtCore.QRect(330, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCpu.setFont(font)
        self.btnCpu.setObjectName("btnCpu")
        self.btnCpu.clicked.connect(self.clickCpu)
        self.btnGrafico = QtWidgets.QPushButton(self.centralWidget)
        self.btnGrafico.setGeometry(QtCore.QRect(230, 470, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnGrafico.setFont(font)
        self.btnGrafico.setObjectName("btnGrafico")
        self.btnGrafico.clicked.connect(self.clickGrafico)


        self.cbxTipoAlin = QtWidgets.QComboBox(self.centralWidget)
        self.cbxTipoAlin.setGeometry(QtCore.QRect(130, 470, 91, 31))
        self.cbxTipoAlin.addItem('Global')
        self.cbxTipoAlin.addItem('Local')
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cbxTipoAlin.setFont(font)
        self.cbxTipoAlin.setObjectName("cbxTipoAlin")

        frmPrincipal.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(frmPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menuBar.setObjectName("menuBar")
        frmPrincipal.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(frmPrincipal)
        self.mainToolBar.setObjectName("mainToolBar")
        frmPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(frmPrincipal)
        self.statusBar.setObjectName("statusBar")
        frmPrincipal.setStatusBar(self.statusBar)

        self.retranslateUi(frmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(frmPrincipal)


    def clickCaminho(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
        self.txtCaminho.setText(name)


    def clickAlinha(self):
        # self.lstSenquncia.setText("Calculando aguarde ....")
        if ".txt" in self.txtCaminho.text():
            cbx = self.cbxTipoAlin.currentText()

            texto=""
            start_time = time()
            run_file_serial(self.txtCaminho.text())
            end_time = time()
            start_time_paralelo = time()
            run_file_thread(self.txtCaminho.text())
            end_time_paralelo = time()
            for index in range(len(paraleloSimilar)):
                texto=texto+"Similaridade: "+format(paraleloSimilar[index])
                texto=texto+"\n\nS="+format(paraleloS[index])
                texto=texto+"\n\nT="+format(paraleloT[index])
                texto = texto + "\n\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                  # +" \nT:"+paraleloT.__getitem__(0)+" \nS:"+paraleloS.__getitem__(0)
            # print('Tempo de execução serial {0} seconds ='.format(end_time - start_time))

            global tempoParalelo,tempoSequencial
            tempoParalelo.clear()
            tempoSequencial.clear()
            tempoParalelo.append(end_time_paralelo - start_time_paralelo)
            tempoSequencial.append(end_time - start_time)
            texto = texto +"\n\nTempo de execução paralela {0} seconds ".format(tempoParalelo)
            texto = texto +"\nTempo de execução serial {0} seconds ".format(tempoSequencial)

            self.lstSenquncia.setText(texto)

            paraleloSimilar.clear()
            paraleloS.clear()
            paraleloT.clear()
        else:
            QMessageBox.question(self,'Atenção',"Escolha um arquivo do formato .txt",QMessageBox.Ok)


    def clickGrafico(self):

        global tempoParalelo, tempoSequencial
        cria_grafico(1,(''),(tempoParalelo),(tempoSequencial))

    def clickCpu(self):
        self.txtCaminho.setText("clickCpu")

    def clickSair(self):
        sys.exit()



    def retranslateUi(self, frmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        frmPrincipal.setWindowTitle(_translate("frmPrincipal", "Alinhamento"))
        self.label_2.setText(_translate("frmPrincipal", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Programa para alinhamento de biosequências </span></p></body></html>"))
        self.btnProcurar.setText(_translate("frmPrincipal", "Procurar"))
        self.btnAlinhar.setText(_translate("frmPrincipal", "Alinhar"))
        self.label.setText(_translate("frmPrincipal", "<html><head/><body><p><span style=\" font-size:11pt;\">Insira a lista de sequências (txt):</span></p></body></html>"))
        self.btnSair.setText(_translate("frmPrincipal", "Sair"))
        self.btnCpu.setText(_translate("frmPrincipal", "CPU Monitor"))
        self.btnGrafico.setText(_translate("frmPrincipal", "Grafico"))

def generate_sequences(filename):
    """
    Esta função gera duas sequências s e t de entrada a cada linha lida do arquivo.
    Também conhecido como generator:

    LER MAIS EM ===> http://pythonclub.com.br/python-generators.html

    Args:
        filename (str): Nome do arquivo de entrada

    """
    with open(filename, 'r') as f:
        s = f.readline()
        t = f.readline()

        yield [s.rstrip(), t.rstrip()]

        for line in f:
            s = t
            t = line.rstrip()

            yield [s, t]

def run(sequences):
    """
    Executa o alinhamento global de duas sequências passadas por parâmetro.

    Args:
        sequences[0]: sequência s
        sequences[1]: sequência t

    Returns: Similaridade entre as sequências s e t.
    """
    s = sequences[0]
    t = sequences[1]

    local_alignment = LocalAlignment(
        s=s,
        t=t,
        score = score
    )
    local_alignment.run()

    global_alignment = GlobalAlignment(
        s=s,
        t=t,
        score=score
    )

    global_alignment.run()

    #mostra as sequencias e a similaridade, retorno multiplo

    if "Global" in str(cbx):
        similarity = global_alignment.get_similarity()
        sequences = global_alignment.get_alignments()
    else:
    #as duas linhas abaixo imprimi o alinhamento local
        similarity = local_alignment.get_similarity()
        sequences = local_alignment.get_alignments()

    return similarity,sequences

serialSimilar = []
serialS = []
serialT = []
serialTempo = []

def run_file_serial(filename):
    for sequences in generate_sequences(filename):
        run(sequences)


def run_file_thread(filename):
    #define usar o numero de nucleos de cpu existentes para processar, inves de determinar numero fixo de processos
    pool = Pool(cpu_count())
    results = pool.map_async(run, generate_sequences(filename))
    pool.close()
    pool.join()
    sequences_results = results.get()

    for similarity, sequences in sequences_results:
        print_sequencies(similarity, sequences)

    return sequences_results # retorna um array com os valores de similaridade (SAIDA DO PROGRAMA)

paraleloSimilar = []
paraleloS = []
paraleloT = []
paraleloTempo = []

def print_sequencies(similarity, sequences):
    global paraleloSimilar,paraleloS,paraleloT
    paraleloSimilar.append(similarity)
    [s, t] = sequences
    paraleloS.append(s)
    paraleloT.append(t)

def cria_grafico(grupos,nomeSequencias,tempoSeq,TempoPar):
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(grupos)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, tempoSeq, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Paralelo')

    rects2 = plt.bar(index + bar_width, TempoPar, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Serial')

    plt.xlabel('Sequencias')
    plt.ylabel('Tempo em segundos')
    plt.title('Alinhamento '+cbx)
    plt.xticks(index + bar_width, nomeSequencias)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_frmPrincipal()
    ui.setupUi(frmPrincipal)
    frmPrincipal.show()
    sys.exit(app.exec_())

