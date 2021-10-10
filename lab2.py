import os
import threading
import time
import aam2107.st03.main
import asm2105.st04.app
import aam2107.st04.main
import asm2105.st20.main
import asm2105.st14.run
import asm2105.st14.main
import asm2104.st17.main


MENU = [
    ["[2104-00] Образец 2104", "asm2104/st00/main.py"],
    ["[2105-00] Образец 2105", "asm2105/st00/main.py"],
    ["[2107-00] Образец 2107", "aam2107/st00/main.py"],
    ["[2104-13] Pezhemsky", "asm2104/st14/main.py"],
    #		добавить пункт меню для вызова своей главной функции по шаблону:
    #		["[<код группы>-<номер по журналу>] <Фамилия>", "<путь до модуля>"],

    # ["[2107-03] Gladkov", aam2107.st03.main.main()],
    ["[2105-04] Dautov", "asm2105/st04/app.py"],
    ["[2105-20] Kharisov", "asm2105/st20/runserver.py"],
    ["[2105-14] Samushkova", "asm2105/st14/run.py"],
    ["[2104-16] Saichkina", "asm2104/st16/runserv.py"],
    ["[2104-08] Korotkova", "asm2104/st08/main.py"],
    ["[2105-02] Astafeva", "asm2105/st02/run.py"],
    ["[2104-15] Polyakova", "asm2104/st15/main.py"],
    ["[2105-03] Bogdanova", "asm2105/st03/run.py"],
    ["[2105-18] Tukhvatullina", "asm2105/st18/main.py"],
    ["[2104-17] Svirkov", "asm2104/st17/main.py"]
    # ["[2107-04] Zhilina", aam2107.st04.main.main()],
]


def launcher():
    time.sleep(3)
    os.system("start http://localhost:5000/")


def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


try:
    while True:
        try:
            app = sorted(MENU)[menu()][1]
            threading.Thread(target=launcher).start()
            if os.system("python3 " + app):
                os.system("python " + app)
        except KeyboardInterrupt:
            pass
except Exception as ex:
    print(ex, "\nbye")
