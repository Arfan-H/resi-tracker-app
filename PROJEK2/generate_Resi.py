# import csv

# def generate_nomor_resi():
#     last_number = 0

#     # Membaca file CSV
#     with open('./cabang_1/Package_in.csv', 'r') as file:
#         reader = csv.DictReader(file)
#         # Mencari angka terakhir yang belum di-generate
#         for row in reader:
#             number = int(row['Nomor Paket'][2:])  # Mengambil angka dari nomor resi
#             if number > last_number:
#                 last_number = number

#     # Meng-generate nomor resi baru
#     new_number = last_number + 1
#     nomor_resi = 'JP{:04d}'.format(new_number)  # Format nomor resi dengan 4 digit angka
#     print(nomor_resi)


# # Contoh penggunaan
# nomor_resi_baru = generate_nomor_resi()


import csv

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

def generate_nomor_resi():
    last_number = 0
    data = LinkedList()

    # Membaca file CSV dan mencari angka terakhir yang belum di-generate
    with open('database/Jakarta/package_in_copy.csv', 'r') as file:
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
    nomor_resi = 'JP{:04d}'.format(new_number)  # Format nomor resi dengan 4 digit angka

    # Menulis nomor resi baru ke file CSV
    # with open('cabang_1\package_in_copy.csv', 'a', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['', nomor_resi])  # Menambahkan nomor resi baru dengan jenis Reguler

    return nomor_resi

# Contoh penggunaan
nomor_resi_baru = generate_nomor_resi()
print(nomor_resi_baru)