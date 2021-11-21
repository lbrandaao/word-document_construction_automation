import pyautogui
pyautogui.PAUSE = 0.3
from screen import Screen
from font import Font
import tasks

'''
Author: Leonardo Barbosa Brandão - Computer Science Student
Linkedin: https://www.linkedin.com/in/leonardo-brand%C3%A3o-118aa4211/

NOTE: Read the 'README.md' file before starting to use the automation.
'''

screen = Screen()
fontQuestion = Font("Calibri Light", "12")
fontCode = Font("Calibri", "11")

range_questions = tasks.setRangeQuestions()
questions_positions = tasks.getQuestionsPositions(range_questions)

pyautogui.alert("Volte para a tela do Word e verifique, pressionando 'alt+tab' se as telas estão na sequência:\n- Documento do Word;\n- Documento com as Questões (reposicionado no topo);\n- IDE (com as questões abertas em ordem crescente);")

tasks.execMainTask(screen=screen, fontQuestion=fontQuestion, fontCode=fontCode, range_questions=range_questions, questions_positions=questions_positions)