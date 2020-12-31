import PySimpleGUI as sg


import re
def match(content, expre):
    result = ''
    pattern = re.compile(expre)
    result = pattern.findall(content)
    return result

layout = [  [sg.Text('匹配内容')],
            [sg.Multiline(key='-content-')],
            [sg.Text('正则表达式')],
            [sg.Multiline(key='-expre-')],
            [sg.Button('查询'), sg.Button('退出')],
            [sg.Multiline(key='-result-')]
        ]

window = sg.Window('正则表达式匹配工具', layout)

while True:
    event, vlause = window.read()
    if event in (None, '退出'):
        break

    if event in ('查询'):
        res = match(str(vlause['-content-']), str(vlause['-expre-']))
        window['-result-'].update(res)

window.close()
