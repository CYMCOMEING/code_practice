# 窗口查询器
import win32gui,time


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
    print("Enumerated a total of  windows with {} classes".format(len(windows)))
    print('HWND      ▮ClassName           ▮Text')
    for item in windows:
        h, n, t = windows[item]
        print('{:<10}▮{:<20}▮{:<10}'.format(h,n,t))
    return windows


def search(m, a, w):
    result = []
    index = 0 if m == 'hwnd' else 1 if m == 'cname' else 2
    if index == 0:
        for i in w:
            if a == w[i][index]:
                result.append(w[i])
                break
    else:
        a = a.upper()
        for i in w:
            if a == w[i][index].upper():
                result.append(w[i])
    print('_______FINISH________')
    if result:
        for i in result:
            h, n, t = i
            print('{:<10}▮{:<20}▮{:<10}'.format(h, n, t))
    else:
        print('NANO')


print("Enumerating all windows...")
win = TestEnumWindows()
print("All tests done!")

print('search语法:\n<search mode> [arg]\n<search mode>:\nhwnd\ncname\ntext\neg:\nsearch >> cname WorkerW')
time.sleep(1)
print('####search####')
while True:
    s = input('search >> ')
    mode, arg = s.split(' ')
    search(mode, arg, win)
