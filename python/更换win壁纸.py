import ctypes
# pip install pywin32
import win32api, win32gui, win32con
import os

def setWallPaper(Imag):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,Imag, win32con.SPIF_SENDWININICHANGE)

if __name__ == '__main__':
    path = os.path.abspath('测试用图片.jpg')
    # ctypes.windll.user32.SystemParametersInfoW(20,  0, path, 0) #替换壁纸
    setWallPaper(path)