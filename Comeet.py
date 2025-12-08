#CO-Meet

import os
import time

KreditScore = 100
Akun = []

def cls():
    time.sleep(3)
    os.system('cls')

def HomeBeforeLogin():
    print("Welcome to Comeet")
    choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.SignUp\n4.Login(1/2/3/4)>>")
    if choose == "1":
        search_usrname = input("Masukkan username yang anda cari: ")
        if search_usrname in Akun:
            print("Berhasil Ketemu")
        else:
            print("Username tidak ditemukan!")
    elif choose == "2":
        print("Silahkan login terlebih dahulu")
    elif choose == "3":
        SignUp()
    elif choose == "4":
        Login()
    else:
        print("Pilihan Tidak Tersedia!")

def HomeAfterLogin():
    print("Welcome to Comeet")
    choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.Check My Credit Score\n4.Logout(1/2/3)>>")
    if choose == "1":
        search_usrname = input("Masukkan username yang anda cari: ")
        if search_usrname in Akun:
            print("Berhasil Ketemu")
        else:
            print("Username tidak ditemukan!")
    elif choose == "2":
        pass
    elif choose == "3":
        print(f"Kredit Score Anda: {KreditScore}")
    elif choose == "4":
        print("Logout Berhasil")
        time.sleep(3)
        os.system('cls')

def SignUp():
    input("Masukkan Email: ")
    usrname_signup = input("Masukkan Username: ")
    pass_signup = input("Masukkan Password: ")
    signup = usrname_signup, pass_signup
    Akun.append(signup)
    print("Signup Berhasil")

def Login():
    usrname_login = input("Masukkan Username: ")
    pass_login = input("Masukkan Password: ")
    login = usrname_login, pass_login
    if login in Akun:
        print("Login Berhasil")
        time.sleep(3)
        os.system('cls')
        while True:
            HomeAfterLogin()
    else:
        print("Login Gagal")

while True:
    print("Welcome to Comeet")
    choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.SignUp\n4.Login(1/2/3/4)>>")
    if choose == "1":
        search_usrname = input("Masukkan username yang anda cari: ")
        for usrname, password in Akun:
            if search_usrname == usrname:
                print("Berhasil Ketemu")
                cls()
                break
        else:
            print("Username tidak ditemukan!")
            cls()
    elif choose == "2":
        print("Silahkan login terlebih dahulu")
        cls()
    elif choose == "3":
        SignUp()
        cls()
    elif choose == "4":
        usrname_login = input("Masukkan Username: ")
        pass_login = input("Masukkan Password: ")
        login = usrname_login, pass_login
        if login in Akun:
            print("Login Berhasil")
            time.sleep(3)
            os.system('cls')
            while True:
                print("Welcome to Comeet")
                choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.Check My Credit Score\n4.Logout(1/2/3)>>")
                if choose == "1":
                    search_usrname = input("Masukkan username yang anda cari: ")
                    for usrname, password in Akun:
                        if search_usrname == usrname:
                            print("Berhasil Ketemu")
                            cls()
                            break
                    else:
                        print("Username tidak ditemukan!")
                        cls()
                elif choose == "2":
                    pass
                elif choose == "3":
                    print(f"Kredit Score Anda: {KreditScore}")
                    cls()
                elif choose == "4":
                    print("Logout Berhasil")
                    time.sleep(3)
                    os.system('cls')
                    break
        else:
            print("Login Gagal")
            cls()
    else:
        print("Pilihan Tidak Tersedia!")
        cls()

