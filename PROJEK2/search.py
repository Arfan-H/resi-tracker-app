# # import csv

# # # Membaca data dari file CSV dan membuat dictionary nomor paket
# # data = {}
# # with open("./cabang_1/Package_in.csv", 'r') as file:
# #     reader = csv.reader(file)
# #     for row in reader:
# #         data[row[0]] = row[1]

# # # Mencari nomor paket yang mengandung '054'
# # search_package = 'da'.lower()
# # found = False

# # for package_id, number in data.items():
# #     if search_package in number or search_package in package_id:
# #         print(f"Nomor paket yang mengandung {search_package} ditemukan:")
# #         print("Package ID:", package_id)
# #         print("Number:", number)
# #         found = True

# # if not found:
# #     print(f"Nomor paket yang mengandung {search_package} tidak ditemukan.")

# # import csv

# # def read_csv(file_path):
# #     data = {}
# #     with open(file_path, 'r') as file:
# #         reader = csv.reader(file)
# #         next(reader)  # Skip header
# #         for row in reader:
# #             data[row[1]] = row[2]  # Memperbaiki indeks kolom saat membaca data
# #     return data

# # def bfs_search(data, search_term):
# #     queue = [("", "")]  # Tuple: (Package ID, Number)
# #     visited = set()

# #     while queue:
# #         package_id, number = queue.pop(0)

# #         if search_term in package_id or search_term in number:
# #             print(f"Nomor paket yang mengandung {search_term} ditemukan:")
# #             print("Package ID:", package_id)
# #             print("Number:", number)
# #             return True
            

# #         if package_id in visited:
# #             continue

# #         visited.add(package_id)

# #         for package_id, number in data.items():
# #             if package_id not in visited:
# #                 queue.append((package_id, number))

# #     return False

# # # Main program
# # file_path = "./cabang_1/Package_in.csv"
# # data = read_csv(file_path)
# # search_term = "jp"

# # if not bfs_search(data, search_term):
# #     print(f"Nomor paket yang mengandung {search_term} tidak ditemukan.")

# import csv

# def read_csv(file_path):
#     data = {}
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header
#         for row in reader:
#             data[row[0]] = row[1]  # Memperbaiki indeks kolom saat membaca data
#     return data

# def bfs_search(data, search_term):
#     queue = [("", "")]  # Tuple: (Package ID, Number)
#     visited = set()
#     displayed_entries = set()  # Set untuk melacak entri yang sudah ditampilkan

#     while queue:
#         package_id, number = queue.pop(0)

#         if search_term in package_id or search_term in number:
#             if (package_id, number) in displayed_entries:
#                 continue
#             print(f"Nomor paket yang mengandung {search_term} ditemukan:")
#             print("Package ID:", package_id)
#             print("Number:", number)
#             displayed_entries.add((package_id, number))  # Tambahkan entri ke set yang sudah ditampilkan
#             # return True  # Jika ingin menghentikan pencarian setelah menemukan satu hasil, aktifkan baris ini

#         if package_id in visited:
#             continue

#         visited.add(package_id)

#         for package_id, number in data.items():
#             if package_id not in visited:
#                 queue.append((package_id, number))

#     return False

# # Main program
# file_path = "database/cabang_1/Package_in.csv"
# data = read_csv(file_path)
# search_term = "06"

# if not bfs_search(data, search_term):
#     print(f"Nomor paket yang mengandung {search_term} tidak ditemukan.")

# double = lambda x: x * 2
# print(double(5))  # Output: 10

# import datetime

# sekarang = datetime.datetime.now()

# tanggal = sekarang.strftime("%d/%m/%Y %H:%M:%S")
# jam = sekarang.strftime("%H:%M:%S")

# print("Tanggal:", tanggal)
# print("Jam:", jam)
# print(tanggal+';'+jam)

from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
from tkinter import Entry, Button
from PIL import Image, ImageTk
import csv
from collections import deque
from tkinter import ttk, filedialog, Tk
import datetime
from time import strftime



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.filename = ""

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def generate_nomor_resi(self, filename):
        last_number = 0
        data = LinkedList()

        # Membaca file CSV dan mencari angka terakhir yang belum di-generate
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Mengabaikan baris header
            for row in reader:
                number = int(row[4][2:])  # Mengambil angka dari nomor resi
                data.append(number)
                if number > last_number:
                    last_number = number

        # Meng-generate nomor resi baru
        new_number = last_number + 1
        while new_number in data:
            new_number += 1
        nomor_resi = 'jp{:04d}'.format(new_number)  # Format nomor resi dengan 4 digit angka

        return nomor_resi

 #------------------------------------------------------------------------------------------------------------------------------------------------     

class PackageSearch:
    def __init__(self, file_path):
        self.data = self.read_csv(file_path)

    def read_csv(self, file_path):
        data = {}
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Lewati header
            for row in reader:
                if len(row) >= 7:
                    nomor_paket = row[4]
                    data[nomor_paket] = row
        return data

    def bfs_search(self, search_term):
        queue = deque()
        visited = set()

        for nomor_paket, row in self.data.items():
            # print('Ini contoh',nomor_paket,row)
            if search_term in nomor_paket:
                queue.append(row)
                visited.add(nomor_paket)
                break

        while queue:
            row = queue.popleft()
            nomor_paket = row[4]

            if nomor_paket == search_term:
                return row

            for neighbor in self.get_neighbors(nomor_paket):
                if neighbor not in visited:
                    queue.append(self.data[neighbor])
                    visited.add(neighbor)

        return None

    def get_neighbors(self, nomor_paket):
        neighbors = []
        for row in self.data.values():
            if row[4] != nomor_paket:
                neighbors.append(row[4])
        return neighbors



class InformasiBarangApp(tk.Tk):
    def __init__(self, file_path):
        super().__init__()
        self.configure()
        width, height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{width}x{height}")
        self.title('Informasi Barang')
        self.search_text = tk.StringVar()
        self.resi_label = None
        self.penerima_label = None
        self.pengirim_label = None
        self.dari_label = None
        self.tujuan_label = None
        self.jenis_paket_label = None
        self.linked_list = LinkedList()
        self.package_search = PackageSearch(file_path)
        
        self.Tracking()


 #------------------------------------------------------------------------------------------------------------------------------------------------       
    def Tracking(self):
        self.img_lacak_barang = Image.open('images/1.png')
        self.img_hal = self.img_lacak_barang.resize((1280,800))
        self.photo_lacak_barang = ImageTk.PhotoImage(self.img_hal)
        
        self.titik_img = Image.open("images/titik.png")
        self.titik_img = self.titik_img.resize((75, 75))
        self.photo_titik = ImageTk.PhotoImage(self.titik_img)
        
        self.label_lacak_barang = tk.Label(self, image=self.photo_lacak_barang, bg='white', bd=0)
        self.label_lacak_barang.place(x=0, y=0)
        
        self.resi = Entry(self, width=25, fg='black', border=0, bg='#D79F38', font=('Poppins',16))
        self.resi.place(x=300, y=460)
        self.resi.insert(0,'Masukkan No. Resi')
        self.resi.bind('<FocusIn>', self.on_enter)
        self.resi.bind('<FocusOut>', self.on_leave)
        
        self.tombol_cari = Button(self, text="Cari", command=self.search_resi, font=("Poppins", 16), bg='#D13123', border=0, activebackground='#D13123',activeforeground="white", cursor="hand2")
        self.tombol_cari.place(x=370, y=540)
        
        self.titik_login_button = Button(self, image=self.photo_titik, command=self.hamburger_menu, bd=0, bg='#FEF7E4', activebackground='#FEF7E4',cursor="hand2")
        self.titik_login_button.place(x=1170, y=50)
        
    def on_enter(self, e):
        self.resi.delete(0,'end')

    def on_leave(self, e):
        name = self.resi.get()
        if name == '':
            self.resi.insert(0,'Masukkan No. Resi')

    def search_resi(self):
        self.img_Informasi_barang = Image.open('images/2.png')
        self.img_hal = self.img_Informasi_barang.resize((1280,800))
        self.photo_Informasi_barang = ImageTk.PhotoImage(self.img_hal)
        
        self.kembali_merah_img = Image.open("images/red arrow.png")
        self.kembali_merah_img = self.kembali_merah_img.resize((60, 60))
        self.photo_kembali_merah = ImageTk.PhotoImage(self.kembali_merah_img)
        
        self.label_Informasi_barang = tk.Label(self, image=self.photo_Informasi_barang, bg='white', bd=0)
        self.label_Informasi_barang.place(x=0, y=0)
        
        self.kembali_merah_button = Button(self, image=self.photo_kembali_merah, bd=0, bg='#FFFFFF', activebackground='#FFFFFF', cursor="hand2", command=self.Tracking)
        self.kembali_merah_button.place(x=1170, y=50)

        self.resi_label = tk.Label(self, text="",font=('poppins',18),bg='#D79F38')
        self.resi_label.place(x= 280,y=335)
        
        self.pengirim_label = tk.Label(self, text="",font=('poppins',18),bg='#D79F38')
        self.pengirim_label.place(x= 280,y=374)
        
        self.penerima_label = tk.Label(self, text="",font=('poppins',18),bg='#D79F38')
        self.penerima_label.place(x= 280,y=412)
        
        self.tujuan_label = tk.Label(self, text="",font=('poppins',18),bg='#D79F38')
        self.tujuan_label.place(x= 280,y=449)
        
        self.jenis_pengiriman_label = tk.Label(self, text="",font=('poppins',18),bg='#D79F38')
        self.jenis_pengiriman_label.place(x= 280,y=485)
        
        self.Cari_Label()
        # self.dari_label = tk.Label(self, text="",font=('poppins',12),bg='#D79F38')
        # self.dari_label.place(x= 280,y=400)
         
        
        # self.berat_label = tk.Label(self, text="",font=('poppins',12),bg='#D79F38')
        # self.berat_label.place(x= 280,y=475)
#------------------------------------------------------------------------------------------------------------------------------------------------
    def Cari_Label(self):
        search_term = self.resi.get()
        result = self.package_search.bfs_search(search_term)
    
        file_path = "database/Jakarta/Package_in.csv"

        package_search = PackageSearch(file_path)
        result = package_search.bfs_search(search_term)

        if result:
            nama_pengirim, nama_penerima, alamat_pengirim, alamat_penerima, nomor_paket, jenis_pengiriman, berat_barang, Tanggal, Cabang_Tujuan = result
            self.pengirim_label.config(text=f"{nama_pengirim}")
            self.penerima_label.config(text=f"{nama_penerima}")
            self.tujuan_label.config(text=f"{alamat_penerima}")
            self.resi_label.config(text=f"{nomor_paket}")
            self.jenis_pengiriman_label.config(text=f"{jenis_pengiriman}")
            self.dari_label.config(text=f"{alamat_pengirim}")
            self.berat_label.config(text=f"{berat_barang}")
        else:
            showerror("Error","Tidak ditemukan data")
 #-----------------------------------------------------------------------------------------------------------------------------------------------------

    def hamburger_menu(self):
        self.img_3 = Image.open('images/3.png')
        self.img_hal = self.img_3.resize((1280,800))
        self.photo_3 = ImageTk.PhotoImage(self.img_hal)
        
        self.kembali_hitam_img = Image.open("images/back.png")
        self.kembali_hitam_img = self.kembali_hitam_img.resize((50, 50))
        self.photo_kembali_hitam = ImageTk.PhotoImage(self.kembali_hitam_img)
        
        self.label_3 = tk.Label(self, image=self.photo_3, bg='white', bd=0)
        self.label_3.place(x=0, y=0)
        
        self.user = Entry(self, width=25, fg='black', border=0, bg='#D79F38', font=('Poppins',16))
        self.user.place(x=300, y=460)
        self.user.insert(0,'Masukkan No. Resi')
        self.user.bind('<FocusIn>', self.on_enter)
        self.user.bind('<FocusOut>', self.on_leave)
        
        self.tombol_cari = Button(self, text="Cari", command=self.tombol_cari, font=("Poppins", 16), bg='#D13123', border=0, activebackground='#D13123', cursor="hand2")
        self.tombol_cari.place(x=370, y=540)
        
        self.kembali_hitam_button = Button(self, image=self.photo_kembali_hitam, bd=0, bg='#D79F38', activebackground='#D79F38', cursor="hand2", command=self.Tracking)
        self.kembali_hitam_button.place(x=940, y=41)
        
        self.tombol_login = Button(self, text="Login", font=("Poppins", 18), bd=0, bg='#D79F38', activebackground='#D79F38', cursor="hand2",activeforeground="white",command=self.LogIn)
        self.tombol_login.place(x= 1060, y=160)
        
        self.tombol_about = Button(self, text="About", font=("Poppins", 18), bd=0, bg='#D79F38', activebackground='#D79F38', cursor="hand2", activeforeground="white",command=self.aboutUs)
        self.tombol_about.place(x= 1060, y=245)

#------------------------------------------------------------------------------------------------------------------------------------------------
    def aboutUs(self):
        self.img_about = Image.open('images/4.png')
        self.img_hal = self.img_about.resize((1280,800))
        self.photo_about = ImageTk.PhotoImage(self.img_hal)
        
        self.kembali_merah_4_img = Image.open("images/red arrow.png")
        self.kembali_merah_4_img = self.kembali_merah_4_img.resize((60, 60))
        self.photo_kembali_merah_4 = ImageTk.PhotoImage(self.kembali_merah_4_img)
        
        self.label_about = tk.Label(self, image=self.photo_about, bg='white', bd=0)
        self.label_about.place(x=0, y=0)
        
        self.kembali_merah_button = Button(self, image=self.photo_kembali_merah_4, command=self.Tracking, bd=0, bg='#FEF7E4', activebackground='#FEF7E4',cursor="hand2")
        self.kembali_merah_button.place(x=1170, y=50)


#------------------------------------------------------------------------------------------------------------------------------------------------
    def LogIn(self):
        self.img_login = Image.open('images/5.png')
        self.img_hal = self.img_login.resize((1280,800))
        self.photo_login = ImageTk.PhotoImage(self.img_hal)
        self.hide_image = ImageTk.PhotoImage(file='images\\show.png')
        self.show_image = ImageTk.PhotoImage(file='images\\hide.png')
        
        self.titik_img = Image.open("images/red arrow.png")
        self.titik_img = self.titik_img.resize((60, 60))
        self.photo_titik = ImageTk.PhotoImage(self.titik_img)
        
        self.label_login = tk.Label(self, image=self.photo_login, bg='white', bd=0)
        self.label_login.place(x=0, y=0)
        
        self.user = Entry(self, width=22, fg='black', border=0, bg='#D13123', font=('Poppins',16))
        self.user.place(x=755, y=275)
        self.user.insert(0,'Masukkan email')
        self.user.bind('<FocusIn>', self.on_enterUser)
        self.user.bind('<FocusOut>', self.on_leaveUser)
        
        self.password = Entry(self, width=22, fg='black', border=0, bg='#D13123', font=('Poppins',16))
        self.password.place(x=700, y=350)
        self.password.insert(0,'Masukkan password')
        self.password.bind('<FocusIn>', self.on_enterUser)
        self.password.bind('<FocusOut>', self.on_leaveUser)
        
        self.tombol_login = Button(self, text="Login", command=self.userName, font=("Poppins", 16), bg='#D13123', border=0, activebackground='#D13123', cursor="hand2")
        self.tombol_login.place(x=825, y=430)
        
        self.titik_login_button = Button(self, image=self.photo_titik, command=self.Tracking, bd=0, bg='#FFFFFF', activebackground='#FFFFFF',cursor="hand2")
        self.titik_login_button.place(x=1170, y=50)

        self.show_button = Button(self, image=self.show_image, command=self.show, relief=FLAT,activebackground="#D13123", borderwidth=0, background="#D13123", cursor="hand2")
        self.show_button.place(x=930, y=355)

    def show(self):
        self.hide_button = Button(self, image=self.hide_image, command=self.hide, relief=FLAT,activebackground="#D13123", borderwidth=0, background="#D13123", cursor="hand2")
        self.hide_button.place(x=930, y=355)
        self.password.config(show='*')
 
    def hide(self):
        self.show_button1 = Button(self, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="#D13123"
                                  , borderwidth=0, background="#D13123", cursor="hand2")
        self.show_button1.place(x=930, y=355)
        self.password.config(show='') 

    def on_enterUser(self, e):
        widget = e.widget
        widget.delete(0, 'end')
    
    def on_leaveUser(self, e):
        widget = e.widget
        if widget.get() == '':
            if widget == self.user:
                widget.insert(0, 'Masukkan email')
            elif widget == self.password:
                widget.insert(0, 'Masukkan password')


    def userName(self):
        with open('database/User_Auth.csv', mode='r') as file:
            reader = csv.reader(file,delimiter=",")
            if self.user.get() == 0 or self.user.get() == 'Username':
                showerror('Error','Username belum diisi')
            else:
                for i in reader:
                    if i == [self.user.get(), self.password.get()]:
                        showinfo(title="Login Success", message="You Successfully Login")
                        self.Main_Menu()
                        return
                showinfo(title="Error", message="Invalid Password")

#------------------------------------------------------------------------------------------------------------------------------------------------

    def Main_Menu(self):
        self.img_cabang = Image.open('images/6.png')
        self.img_hal = self.img_cabang.resize((1280,800))
        self.photo_cabang = ImageTk.PhotoImage(self.img_hal)
        
        self.kembali_merah_img = Image.open("images/red arrow.png")
        self.kembali_merah_img = self.kembali_merah_img.resize((60, 60))
        self.photo_kembali_merah = ImageTk.PhotoImage(self.kembali_merah_img)
        
        self.label_cabang = tk.Label(self, image=self.photo_cabang, bg='white', bd=0)
        self.label_cabang.place(x=0, y=0)
        
        self.kembali_merah_button = Button(self, image=self.photo_kembali_merah, command=self.kembali_merah, bd=0, bg='#FEF7E4', activebackground='#FEF7E4', cursor="hand2")
        self.kembali_merah_button.place(x=1170, y=50)
        
        self.tombol_pengiriman = Button(self, text="Click", command=self.pengiriman, font=("Poppins", 16), bg='#D13123', border=0, activebackground='#D13123', cursor="hand2")
        self.tombol_pengiriman.place(x=250, y=670)
        
        self.tombol_pemantauan = Button(self, text="Click", command=self.tombol_click_pemantauan, font=("Poppins", 16), bg='#D13123', border=0, activebackground='#D13123', cursor="hand2")
        self.tombol_pemantauan.place(x=670, y=670)

        
        self.label = tk.Label(self, font=('calibri', 82, 'bold'), background='#D79F38', foreground='#3B435F')
        self.label.place(x=950, y=620)  
        
        self.waktu()
        
    def waktu(self):
        string_waktu = strftime('%H:%M')
        self.label.config(text=string_waktu)
        self.label.after(1000, self.waktu)  
        
    def kembali_merah(self):  
        sure = askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.Tracking()

#------------------------------------------------------------------------------------------------------------------------------------------------

    def pengiriman(self):
        self.img_pendataan_barang = Image.open('gambar/7.png')
        self.img_hal = self.img_pendataan_barang.resize((1280,800))
        self.photo_pendataan_barang = ImageTk.PhotoImage(self.img_hal)
        
        self.kembali_merah_7_img = Image.open("gambar/red arrow.png")
        self.kembali_merah_7_img = self.kembali_merah_7_img.resize((60, 60))
        self.photo_kembali_merah_7 = ImageTk.PhotoImage(self.kembali_merah_7_img)
        
        self.label_pendataan_barang = tk.Label(self, image=self.photo_pendataan_barang, bg='white', bd=0)
        self.label_pendataan_barang.place(x=0, y=0)
        
        self.kembali_merah_7_button = Button(self, image=self.photo_kembali_merah_7, command=self.Main_Menu, bd=0, bg='#FEF7E4', activebackground='#FEF7E4', cursor='hand2')
        self.kembali_merah_7_button.place(x=1170, y=50)
        
        self.tombol_proses_7 = Button(self, text="Proses", command=self.Proses_barang, font=("Poppins", 18), bg='#D13123', border=0, activebackground='#D13123',cursor='hand2')
        self.tombol_proses_7.place(x=845, y=618)
        
        cabang_tujuan = ["Jakarta", "Surabaya"]
        jenis_pengiriman = ["Reguler", "Prioritas"]
        
        self.input_pengirim = Entry(self, width=26, fg='black', border=0, bg='#CD8746', font=('Poppins',16))
        self.input_pengirim.place(x=140,y=226)

        self.input_penerima = Entry(self, width=26, fg='black', border=0, bg='#CD8746', font=('Poppins',16))
        self.input_penerima.place(x=140,y=321)

        self.input_alamat_pengirim = Entry(self, width=26, fg='black', border=0, bg='#CD8746', font=('Poppins',16))
        self.input_alamat_pengirim.place(x=140,y=423)

        self.input_alamat_tujuan = Entry(self, width=26, fg='black', border=0, bg='#CD8746', font=('Poppins',16))
        self.input_alamat_tujuan.place(x=140,y=525)

        self.input_berat = Entry(self, width=10, fg='black', border=0, bg='#CD8746', font=('Poppins',18))
        self.input_berat.place(x=610,y=421)

        self.input_cabangTujuan = ttk.Combobox(self, background='black', values=cabang_tujuan,width=26, font=('Poppins',16))
        self.input_cabangTujuan.place(x=130,y=630)

        self.input_jenisPengiriman = ttk.Combobox(self, background='black', values=jenis_pengiriman,width=26, font=('Poppins',16))
        self.input_jenisPengiriman.place(x=610,y=318)

        
    def Proses_barang(self):
        self.filename = f"database/{self.user.get()}/Package_in.csv"
        
        self.nomor_resi = self.linked_list.generate_nomor_resi(self.filename)
        # data_baru = self.input_pengirim.get(), self.input_penerima.get(), self.input_alamat_pengirim.get(), self.input_alamat_tujuan.get(), self.nomor_resi, self.input_jenisPengiriman.get(), self.input_berat.get()


        with open(self.filename, 'a+', newline='') as f:
            data_baru = [self.input_pengirim.get(), self.input_penerima.get(), self.input_alamat_pengirim.get(), self.input_alamat_tujuan.get(), self.nomor_resi, self.input_jenisPengiriman.get(), self.input_berat.get()]
            write = csv.writer(f, data_baru)
            write.writerow(data_baru)
            showinfo("success", "Data sudah berhasil diinput")
            showinfo("Info",f"nomor resi anda adalah : {self.nomor_resi}")
        

#------------------------------------------------------------------------------------------------------------------------------------------------
    def tombol_click_pemantauan(self):
        self.img_Pemantauan = Image.open('images/8.png')
        self.img_hal = self.img_Pemantauan.resize((1280,800))
        self.photo_Pemantauan = ImageTk.PhotoImage(self.img_hal)

        self.kembali_merah_8 = Image.open('images/red arrow.png')
        self.kembali_merah_8 = self.kembali_merah_8.resize((60, 60))
        self.photo_kembali_merah_8 = ImageTk.PhotoImage(self.kembali_merah_8)
        
        self.label_Pemantauan = tk.Label(self, image=self.photo_Pemantauan, bg='white', bd=0)
        self.label_Pemantauan.place(x=0, y=0)

        self.kembali_merah_8_button = Button(self, image=self.photo_kembali_merah_8, command=self.Main_Menu, bd=0, bg='#FEF7E4', activebackground='#FEF7E4',cursor='hand2')
        self.kembali_merah_8_button.place(x=1170, y=50)
        
        self.tombol_kedatangan = Button(self, text="Click", command=self.tombol_click_kedatangan, font=("Poppins", 18), bg='#D13123', border=0, activebackground='#D13123',cursor='hand2')
        self.tombol_kedatangan.place(x=385, y=567)
        
        self.tombol_keberangkatan = Button(self, text="Click", command=print(), font=("Poppins", 18), bg='#D13123', border=0, activebackground='#D13123',cursor='hand2')
        self.tombol_keberangkatan.place(x=835, y=567)

    def tombol_click_kedatangan(self):
        # Create a frame for the buttons and treeview
        # self.frame = Frame(self)
        # self.frame.pack(side="top", fill="both", expand=True)
            
            # Load the image
        self.img = PhotoImage(file="images/11.png")
            
        # Display the image
        self.img_label = Label(self, image=self.img,bg='white', bd=0)
        self.img_label.place(x=0, y=0)
            
        self.tree = ttk.Treeview(self)
        self.open_button = ttk.Button(self, text="Open File", command=self.openFile_keberangkatan)
        self.move_button = ttk.Button(self, text="Move Selected Row", command=self.move_selected_row)
            
        self.open_button.place(x=1000, y=10)
        self.move_button.place(x=1000, y=50)
        self.tree.place(x=330, y=100, width=790, height=450)

    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())  # Clear the treeview

    def openFile_keberangkatan(self):
        self.current_file_path2 = 'database\Jakarta\package_out.csv'
        if self.current_file_path2:
            with open(self.current_file_path2, 'r') as file:
                csvreader = csv.reader(file)
                headers = next(csvreader)

                self.clear_treeview()

                self.tree["columns"] = headers
                self.tree["show"] = "headings"

                for col in headers:
                    self.tree.heading(col, text=col)

                for row in csvreader:
                    self.tree.insert("", "end", values=row)

    def move_selected_row(self):
        target_file_path = f'database/{self.user.get()}/Pakcage_in.csv'
        move = askyesno('Move', 'Apakah Anda ingin memindah data ini?')
        if move == True:
            selected_item = self.tree.selection()
            if not selected_item:
                showwarning("No selection", "Please select a row to move.")
                return

            row_values = self.tree.item(selected_item, "values")

        # Move row to target CSV file
        with open(target_file_path, 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(row_values)

        # Remove row from the treeview and the original CSV file
        self.tree.delete(selected_item)
        self.remove_row_from_csv(self.current_file_path, row_values)

    def remove_row_from_csv(self, row_values):
        file_path = f'database/{self.user.get()}/Pakcage_in.csv'
        with open(file_path, 'r') as file:
            rows = list(csv.reader(file))

        with open(file_path, 'w', newline='') as file:
            csvwriter = csv.writer(file)
            for row in rows:
                if row != list(row_values):
                    csvwriter.writerow(row)

#------------------------------------------------------------------------------------------------------------------------------------------------



file_path = "database/Jakarta/Package_in.csv"

if __name__ == "__main__":
    app = InformasiBarangApp(file_path)
    app.mainloop()
