import csv
from collections import deque

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

file_path = "database/cabang_1/Package_in_copy.csv"
search_term = 'jp0008'

package_search = PackageSearch(file_path)
result = package_search.bfs_search(search_term)

if result:
    nama_pengirim, nama_penerima, alamat_pengirim, alamat_penerima, nomor_paket, jenis_pengiriman, berat_barang = result
    print(f"Nama Pengirim: {nama_pengirim}")
    print(f"Nama Penerima: {nama_penerima}")
    print(f"Alamat Pengirim: {alamat_pengirim}")
    print(f"Alamat Penerima: {alamat_penerima}")
    print(f"Nomor Paket: {nomor_paket}")
    print(f"Jenis Pengiriman: {jenis_pengiriman}")
    print(f"Berat Barang: {berat_barang}")
else:
    print("Error")