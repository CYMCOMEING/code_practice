import time
import os
import platform


if __name__ == "__main__":
    status = ""
    with os.popen("mode con", "r") as f:
        status = f.read()

    len = int(status.split()[6]) - 14
    # if len <= 14:
    #     os.system("mode con cols=20")
    #     print("mode con cols=20")
    #     len = 14

    sys = platform.system()
    if sys == "Windows":
        os.system("mode con cols={} lines=10".format(len + 14))
    elif sys == "Linux":
        pass
    else:
        pass

    print("start".center(len//2,"-"))
    start = time.perf_counter()
    for i in range(len+1):
        a = '*' * i
        b = '.' *(len-i)
        c = (i/len)*100
        d = time.perf_counter()-start
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,d),end="")
        time.sleep(0.05)
    print("\n"+"end".center(len//2,'-'))
