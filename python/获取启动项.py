import winreg  as wr


def getAutoRun():
    root1 = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)  # 获取LocalMachine Key
    root2 = wr.ConnectRegistry(None, wr.HKEY_CURRENT_USER)
    result = {}
    try:
        targ = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        print("****reading from ", targ, "****")
        key1 = wr.OpenKey(root1, targ)  # 打开localmachine的autorun列表
        key2 = wr.OpenKey(root2, targ)  # 打开currentuser的autorun列表
        cnt = 0
        try:
            for i in range(1024):
                try:
                    n, v, t = wr.EnumValue(key1, i)  # 迭代localmachine
                    result[n] = v
                    cnt += 1
                except EnvironmentError:
                    break
            for i in range(1024):
                try:
                    n, v, t = wr.EnumValue(key2, i)  # 迭代currentuser
                    result[n] = v
                    cnt += 1
                except EnvironmentError:
                    break
        finally:
            wr.CloseKey(key1)
            wr.CloseKey(key2)
    finally:
        wr.CloseKey(root1)
        wr.CloseKey(root2)
    return result


def main():
    autoRun = getAutoRun()
    [print(key,": " ,autoRun[key]) for key in autoRun]


if __name__ == "__main__":
    main()
