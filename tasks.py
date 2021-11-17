import pyautogui
pyautogui.PAUSE = 0.3
import time
from screen import Screen
from font import Font
import sys

def setRangeQuestions():
    '''
    :return range_questions: the range of questions
    '''
    initial_question = int(pyautogui.prompt(text="Insira o número da questão inicial.", title="Primeira Questão"))
    final_question = int(pyautogui.prompt(text="Insira o número da última questão.", title="Última Questão"))
    return (initial_question, final_question)

def getQuestionsPositions(range_questions:tuple):
    '''
    :param range_questions: the range of questions
    :return questions_positions: list of mouse positions of questions
    '''
    pyautogui.alert("Vá para a janela do documento com as questões e certifique-se que ele está no topo.")
    questions_positions = []
    initial_question, final_question = range_questions
    for i in range(initial_question, final_question+1):
        down_page = pyautogui.confirm(text=f"Necessário rolar a página para baixo para capturar a questão {i} inteiramente?", title="Descer Página", buttons=["Sim", "Não"])
        nPress_down = 0
        if (down_page[0].lower() == 's'):
            pyautogui.alert("Posicione a página da maneira que deseja, pressionando a tecla 'down' (seta para baixo).\nOBS: Conte o número de vezes que você pressionou a tecla!")
            nPress_down = int(pyautogui.prompt(text="Quantas vezes a tecla 'down' foi pressionada?", title="Tecla Down"))
        pyautogui.alert(f"Posicione o mouse sobre o inicio da questão {i}.")
        mouseX_questionStart, mouseY_questionStart = pyautogui.position()
        pyautogui.alert(f"Posicione o mouse sobre o fim da questão {i}.")
        mouseX_questionEnd, mouseY_questionEnd = pyautogui.position()
        questionPosition = []
        questionPosition.append((mouseX_questionStart, mouseY_questionStart))
        questionPosition.append((mouseX_questionEnd, mouseY_questionEnd))
        questionPosition.append(nPress_down)

        questions_positions.append(questionPosition)

    return questions_positions

def enumerate(mouseX_enumerator:int, mouseY_enumerator:int):
    pyautogui.click(mouseX_enumerator, mouseY_enumerator)

def checkDownPage(questionProperties: list):
    if (questionProperties[2] > 0):
        nPress_down = questionProperties[2]
        pyautogui.press("down", presses=nPress_down)

def copyQuestion(questionProperties:list):
    '''
    :param questionProperties: [(mouseX_questionStart, mouseY_questionStart), (mouseX_questionEnd, mouseY_questionEnd), nPress_down]
    '''
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)
    checkDownPage(questionProperties)
    mouseX_questionStart, mouseY_questionStart = questionProperties[0]
    mouseX_questionEnd, mouseY_questionEnd = questionProperties[1]
    pyautogui.moveTo(mouseX_questionStart, mouseY_questionStart)
    pyautogui.mouseDown()
    pyautogui.moveTo(x=mouseX_questionStart, y=mouseY_questionEnd, duration=0.1)
    pyautogui.moveTo(x=mouseX_questionEnd, y=mouseY_questionEnd, duration=0.1)
    pyautogui.mouseUp()
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)
    pyautogui.hotkey("alt", "tab")

def pasteQuestion():
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "shift", "up")

def defineFont(font: Font, mouseX_positions: list, mouseY_positions: list):
    '''
    :param font: font
    :param mouseX_positions: [mouseX_boxFont, mouseX_boxFontSize]
    :param mouseY_positions: [mouseY_boxFont, mouseY_boxFontSize]
    '''
    pyautogui.click(mouseX_positions[0], mouseY_positions[0])
    time.sleep(0.1)
    pyautogui.write(font.fontFamily, interval=0.05)
    pyautogui.press("backspace")
    pyautogui.press("enter")
    pyautogui.click(mouseX_positions[1], mouseY_positions[1])
    time.sleep(0.1)
    pyautogui.write(font.fontSize, interval=0.05)
    pyautogui.press("enter")
    time.sleep(0.1)

def insertTable(mouseX_positions: list, mouseY_positions: list):
    '''
    :param mouseX_positions: [mouseX_sectionInserir, mouseX_optionTabela, mouseX_createTabela]
    :param mouseY_positions: [mouseY_sectionInserir, mouseY_optionTabela, mouseY_createTabela]
    '''
    pyautogui.press("enter")
    pyautogui.press("backspace")
    pyautogui.click(mouseX_positions[0], mouseY_positions[0])
    time.sleep(0.5)
    pyautogui.click(mouseX_positions[1], mouseY_positions[1])
    time.sleep(0.5)
    pyautogui.click(mouseX_positions[2], mouseY_positions[2])
    time.sleep(0.1)

def copyCode():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.keyDown("ctrl")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("ctrl")

def pasteCode(mouseX_sectionPagInitial:int, mouseY_sectionPagInitial:int):
    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "shift", "right")
    pyautogui.click(mouseX_sectionPagInitial, mouseY_sectionPagInitial)
    time.sleep(0.1)

def prepareNextQuestion():
    pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.5)
    confirm = pyautogui.confirm(text="Continuar?", title="", buttons=["Sim", "Não"])
    if (confirm[0] == "N"):
        sys.exit()

def execMainTask(screen:Screen, fontQuestion:Font, fontCode:Font, range_questions:tuple, questions_positions:list):
    initial_question, final_question = range_questions
    n_questions = final_question-initial_question+1
    for i in range(0, n_questions):
        enumerate(screen.mouseX_enumerator, screen.mouseY_enumerator)
        copyQuestion(questions_positions[i])
        pasteQuestion()
        defineFont(fontQuestion, [screen.mouseX_boxFont, screen.mouseX_boxFontSize],
                         [screen.mouseY_boxFont, screen.mouseY_boxFontSize])
        insertTable([screen.mouseX_sectionInserir, screen.mouseX_optionTabela, screen.mouseX_createTabela],
                          [screen.mouseY_sectionInserir, screen.mouseY_optionTabela, screen.mouseY_createTabela])
        copyCode()
        pasteCode(screen.mouseX_sectionPagInitial, screen.mouseY_sectionPagInitial)
        enumerate(screen.mouseX_enumerator, screen.mouseY_enumerator)
        defineFont(fontCode, [screen.mouseX_boxFont, screen.mouseX_boxFontSize],
                         [screen.mouseY_boxFont, screen.mouseY_boxFontSize])
        prepareNextQuestion()