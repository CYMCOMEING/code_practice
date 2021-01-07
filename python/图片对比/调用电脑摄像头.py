
import tkinter
import cv2
import PySimpleGUI as sg
USE_CAMERA = 0
window, cap = sg.Window('简易的计算机视觉系统', [[sg.Image(filename='', key='image')], ], location=(
    0, 0), grab_anywhere=True), cv2.VideoCapture(USE_CAMERA)
while window(timeout=20)[0] != sg.WIN_CLOSED:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
