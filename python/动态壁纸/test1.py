'''
说明:pyglet 库并非必须,任何可可获取句柄的窗口都可以设置为壁纸.
'''

import win32gui, time, pyglet


def welcome():
    print("\033[1;33m 动态壁纸测试>>感谢您的尝试\n动态壁纸测试>>请在稍后弹出的页面中选择您的GIF文件\033[0m")
    print("\033[1;33m PS:本程序可拓展交互壁纸功能\033[0m")
    print("\033[1;33m 源程序依赖:win32gui time pyglet\n pip install <名称> 即可安装\033[0m")
    time.sleep(3)


# 获取壁纸层的句柄
def init():
    def _MyCallback(hwnd, extra):
        windows = extra
        temp = list()
        temp.append(hex(hwnd))
        temp.append(win32gui.GetClassName(hwnd))
        temp.append(win32gui.GetWindowText(hwnd))
        windows[hwnd] = temp

    def TestEnumWindows():
        windows = {}
        win32gui.EnumWindows(_MyCallback, windows)
        return windows

    w = TestEnumWindows()
    workerw = []
    check = ''
    # 匹配+搜索
    for i in w:
        if 'WorkerW' == w[i][1]:
            workerw.append(w[i][0])
    for i in w:
        if 'Progman' == w[i][1]:
            check = w[i][0]
    for i in workerw:
        if hex(win32gui.GetParent(eval(i))) == check:
            break

    print("\033[1;36m 初始化成功!!!\nhwnd:{}\033[0m".format(check))
    return i


# 设置窗口为背景,调用window api
def setbk(child,praent):
    win32gui.SetParent(eval(child),eval(praent))

# 创建GIF显示窗口
def main():
    praent_hwnd = init()
    welcome()
    # 文件对话框
    h = input('输入目标句柄>>')
    setbk(h,praent_hwnd)
    print('成功')


main()

