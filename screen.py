import pyautogui
pyautogui.PAUSE = 0.2
import os
import sys

class Screen():
    def setMousePositions(self):
        file = open("mouse_positions.txt", "w")

        file.write("mouseX_enumerator,mouseY_enumerator=")
        pyautogui.alert("Posicione o mouse sobre o enumerador do Word.")
        mouseX_enumerator, mouseY_enumerator = pyautogui.position()
        file.write(f"({mouseX_enumerator},{mouseY_enumerator})\n")

        file.write("mouseX_boxFont,mouseY_boxFont=")
        pyautogui.alert("Posicione o mouse sobre a caixa de fonte.")
        mouseX_boxFont, mouseY_boxFont = pyautogui.position()
        file.write(f"({mouseX_boxFont},{mouseY_boxFont})\n")

        file.write("mouseX_boxFontSize,mouseY_boxFontSize=")
        pyautogui.alert("Posicione o mouse sobre a caixa de tamanho da fonte.")
        mouseX_boxFontSize, mouseY_boxFontSize = pyautogui.position()
        file.write(f"({mouseX_boxFontSize},{mouseY_boxFontSize})\n")

        file.write("mouseX_sectionInserir,mouseY_sectionInserir=")
        pyautogui.alert("Posicione o mouse sobre a seção 'Inserir' no topo do documento.")
        mouseX_sectionInserir, mouseY_sectionInserir = pyautogui.position()
        file.write(f"({mouseX_sectionInserir},{mouseY_sectionInserir})\n")

        file.write("mouseX_optionTabela,mouseY_optionTabela=")
        pyautogui.alert("Clique na seção 'Inserir' e posicione o mouse sobre a opção 'Tabela'.")
        mouseX_optionTabela, mouseY_optionTabela = pyautogui.position()
        file.write(f"({mouseX_optionTabela},{mouseY_optionTabela})\n")

        file.write("mouseX_createTabela,mouseY_createTabela=")
        pyautogui.alert("Clique na opção 'Tabela' e posicione o mouse sobre o primeiro quadrado à esquerda para a criação de uma tabela 1x1.")
        mouseX_createTabela, mouseY_createTabela = pyautogui.position()
        file.write(f"({mouseX_createTabela},{mouseY_createTabela})\n")

        file.write("mouseX_sectionPagInitial,mouseY_sectionPagInitial=")
        pyautogui.alert("Posicione o mouse sobre a seção 'Página Inicial' no topo do documento.")
        mouseX_sectionPagInitial, mouseY_sectionPagInitial = pyautogui.position()
        file.write(f"({mouseX_sectionPagInitial},{mouseY_sectionPagInitial})")
        file.close()

        self.getMousePositions()

    def getMousePositions(self):
        isEmpty = os.stat("mouse_positions.txt").st_size==0
        if (isEmpty):
            setMousePositions = pyautogui.confirm(text="Antes de utilizar a aplicação é necessário setar algumas configurações de tela. Deseja fazer isso?", title="Configurações", buttons=["Sim", "Não"])
            if (setMousePositions[0].lower()=="s"):
                self.setMousePositions()
            else:
                pyautogui.alert("Não será possível utilizar a aplicação.")
                sys.exit()
        else:
            file = open("mouse_positions.txt", "r")
            reading = file.readlines()
            self.mouse_positions = []
            # REF: https://pt.stackoverflow.com/questions/521595/pegar-trecho-de-uma-string-entre-dois-caracteres
            for line in reading:
                position = line.split('(')[1].split(')')[0].split(',')
                self.mouse_positions.append(position)
            file.close()

    def __init__(self):
        self.getMousePositions()
        self.mouseX_enumerator, self.mouseY_enumerator = (int(self.mouse_positions[0][0]), int(self.mouse_positions[0][1]))
        self.mouseX_boxFont, self.mouseY_boxFont = (int(self.mouse_positions[1][0]), int(self.mouse_positions[1][1]))
        self.mouseX_boxFontSize, self.mouseY_boxFontSize = (int(self.mouse_positions[2][0]), int(self.mouse_positions[2][1]))
        self.mouseX_sectionInserir, self.mouseY_sectionInserir = (int(self.mouse_positions[3][0]), int(self.mouse_positions[3][1]))
        self.mouseX_optionTabela, self.mouseY_optionTabela = (int(self.mouse_positions[4][0]), int(self.mouse_positions[4][1]))
        self.mouseX_createTabela, self.mouseY_createTabela = (int(self.mouse_positions[5][0]), int(self.mouse_positions[5][1]))
        self.mouseX_sectionPagInitial, self.mouseY_sectionPagInitial = (int(self.mouse_positions[6][0]), int(self.mouse_positions[6][1]))