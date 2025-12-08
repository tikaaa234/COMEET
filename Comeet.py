#CO-Meet

import os
import time

KreditScore = 100
Schedule = []
JadwalTemu = []
Akun = []
Notif = []

def cls():
    time.sleep(3)
    os.system('cls')

def schedule():
    choose = input("Silahkan pilih salah satu dibawah ini\n1.Tambah Schedule\n2.Hapus Schedule\n3.Lihat Jadwal\n4.Hide Schedule\n(1/2/3/4)>>")
    if choose == "1":
        hari = input("Masukkan Hari: ")
        tanggal = input("Masukkan Tanggal: ")
        jam_mulai = input("Masukkan Jam Mulai: ")
        jam_selesai = input("Masukkan Jam Selesai: ")
        jadwal_update = usrname_login, hari, tanggal, jam_mulai, jam_selesai
        Schedule.append(jadwal_update)
    elif choose == "2":
        for usrname_login, hari, tanggal, jam_mulai, jam_selesai in Schedule:
            print(f"{hari}, {tanggal}, {jam_mulai} s/d {jam_selesai}")

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
    choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.SignUp\n4.Login\n(1/2/3/4)>>")
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
                choose = input("Choose what you want\n1.Search Username\n2.Edit My Schedule\n3.Check My Credit Score\n4.Logout\n5.Liat Notif\n(1/2/3/4/5)>>")
                if choose == "1":
                    search_usrname = input("Masukkan username yang anda cari: ")
                    found = False
                    for usrname, password in Akun:
                        if search_usrname == usrname:
                            print("Berhasil Ketemu")
                            cls()
                            found = True
                            break
                    if found:
                        while True:
                            choose = input(f"1.Lihat Schedule {search_usrname}\n2.Buat Pengajuan Jadwal Temu\n3.Kembali\n(1/2/3)>>")
                            if choose == "1":
                                cls()
                                for usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju in Schedule:
                                    if usrname == search_usrname:
                                        print(f"{hari}, {tanggal} {bulan} {tahun}. Jam: {jam_mulai} s/d {jam_selesai} bersama {nama_pengaju}")
                                break
                            elif choose == "2":
                                hari_notif = input("Masukkan Hari: ")
                                tanggal_notif = input("Masukkan Tanggal: ")
                                bulan_notif = input("Masukkan Bulan: ")
                                tahun_notif = input("Tahun: ")
                                jam_mulai_notif = input("Masukkan Jam Mulai: ")
                                jam_selesai_notif = input("Masukkan Jam Selesai: ")
                                nama_pengaju = usrname_login
                                notif = search_usrname, hari_notif, tanggal_notif, bulan_notif, tahun_notif, jam_mulai_notif, jam_selesai_notif, nama_pengaju
                                Notif.append(notif)
                                print("Pengajuan Telah Dikirim!")
                                cls()
                            elif choose == "3":
                                cls()
                                break
                    else:
                        print("Username tidak ditemukan!")
                        cls()
                elif choose == "2":
                    cls()
                    while True:
                        choose = input("Silahkan pilih salah satu dibawah ini\n1.Tambah Schedule\n2.Hapus Schedule\n3.Lihat Schedule\n4.Kembali\n(1/2/3/4)>>")
                        if choose == "1":
                            hari = input("Masukkan Hari: ")
                            tanggal = input("Masukkan Tanggal: ")
                            bulan = input("Masukkan Bulan: ")
                            tahun = input("Tahun: ")
                            jam_mulai = input("Masukkan Jam Mulai: ")
                            jam_selesai = input("Masukkan Jam Selesai: ")
                            nama_pengaju = "Pribadi"
                            jadwal_update = usrname_login, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju
                            Schedule.append(jadwal_update)
                            cls()
                        elif choose == "2":
                            for usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju in Schedule:
                                if usrname == usrname_login:
                                    print(f"{hari}, {tanggal} {bulan} {tahun}. Jam: {jam_mulai} s/d {jam_selesai} bersama {nama_pengaju}")
                            choose_hapus = input("Masukkan hari,tanggal,bulan yang ingin dihapus (contoh: senin,1,Januari): ").split(",")
                            choose_hapus = [x.strip() for x in choose_hapus]
                            hapus_hari, hapus_tanggal, hapus_bulan = choose_hapus
                            for item in Schedule:
                                usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju = item
                                if usrname == usrname_login and (hari == hapus_hari and tanggal == hapus_tanggal and bulan == hapus_bulan):
                                    Schedule.remove(item)
                                    print("Jadwal Berhasil Dihapus!")
                                    cls()
                                    break
                                else:
                                    print("Jadwal Tidak Ditemukan!")
                                    cls()
                        elif choose == "3":
                            for usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju in Schedule:
                                if usrname == usrname_login:
                                    print(f"{hari}, {tanggal} {bulan} {tahun}. Jam: {jam_mulai} s/d {jam_selesai} bersama {nama_pengaju}")
                            break

                        elif choose == "4":
                            cls()
                            break
                elif choose == "3":
                    print(f"Kredit Score Anda: {KreditScore}")
                    cls()
                elif choose == "4":
                    print("Logout Berhasil")
                    time.sleep(3)
                    os.system('cls')
                    break
                elif choose == "5":
                    while True:
                        choose = input("1.Accept/Reject Notif\n2.Kembali\n(1/2)>>")
                        if choose == "1":
                            for usrname, hari_notif, tanggal_notif, bulan_notif, tahun_notif, jam_mulai_notif, jam_selesai_notif, nama_pengaju in Notif:
                                if usrname == usrname_login:
                                    print(f"{hari_notif}, {tanggal_notif} {bulan_notif} {tahun_notif}. Jam: {jam_mulai_notif} s/d {jam_selesai_notif} diajukan oleh {nama_pengaju}")
                            choose_accept = input("1.Accept\n2.Reject\n3.Kembali\n(1/2)>>")
                            if choose_accept == "1":
                                accept = input("Masukkan hari,tanggal,bulan,nama pengaju yang ingin di accept\n(contoh: senin,1,januari,budi)>>").split(",")
                                accept = [x.strip() for x in accept]
                                accept_hari, accept_tanggal, accept_bulan, accept_nama_pengaju = accept
                                for item in Notif:
                                    hari_notif = hari
                                    tanggal_notif = tanggal
                                    bulan_notif = bulan
                                    tahun_notif = tahun
                                    jam_mulai_notif = jam_mulai
                                    jam_selesai_notif = jam_selesai
                                    usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju = item
                                    if usrname == usrname_login and (hari == accept_hari and tanggal == accept_tanggal and bulan == accept_bulan and nama_pengaju == accept_nama_pengaju):
                                        Schedule.append(item)
                                        Notif.remove(item)
                                        print("Jadwal Berhasil Diaccept!")
                                        cls()
                                        break
                                    else:
                                        print("Jadwal Tidak Ada")
                                        cls()
                            elif choose_accept == "2":
                                reject = input("Masukkan hari,tanggal,bulan,nama pengaju yang ingin di reject\n(contoh: senin,1,januari,budi)>>").split(",")
                                reject = [x.strip() for x in reject]
                                reject_hari, reject_tanggal, reject_bulan, reject_nama_pengaju = reject
                                for item in Notif:
                                    hari_notif = hari
                                    tanggal_notif = tanggal
                                    bulan_notif = bulan
                                    tahun_notif = tahun
                                    jam_mulai_notif = jam_mulai
                                    jam_selesai_notif = jam_selesai
                                    usrname, hari, tanggal, bulan, tahun, jam_mulai, jam_selesai, nama_pengaju = item
                                    if usrname == usrname_login and (hari == reject_hari and tanggal == reject_tanggal and bulan == reject_bulan and nama_pengaju == reject_nama_pengaju):
                                        Notif.remove(item)
                                        print("Jadwal Berhasil Direject!")
                                        cls()
                                        break
                                    else:
                                        print("Jadwal Tidak Ada")
                                        cls()
                            elif choose_accept == "3":
                                cls()
                                break
                        elif choose == "2":
                            cls()
                            break
        else:
            print("Login Gagal")
            cls()
    else:
        print("Pilihan Tidak Tersedia!")
        cls()

