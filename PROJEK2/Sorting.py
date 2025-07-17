import csv

def shell_sort(data):
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and compare_priority(data[j - gap], temp):
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2

def compare_priority(p1, p2):
    priority_order = {"Prioritas": 1, "Reguler": 2, "Retur": 3}
    type1 = p1[5]
    type2 = p2[5]
    
    # Compare based on priority first
    if priority_order[type1] != priority_order[type2]:
        return priority_order[type1] > priority_order[type2]
    
    # If both have same priority, compare by type
    if p1[4] == p2[4]:
        # Convert receipt numbers to integers for proper comparison
        resi1 = int(p1[3])
        resi2 = int(p2[3])
        return resi1 > resi2
    
    # Compare by type
    return p1[4] > p2[4]

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Membaca data dari file CSV
file_name = 'database/Surabaya/package_out.csv'
data = read_csv(file_name)

# Mengabaikan baris header
header = data[0]
data = data[1:]

# Mengurutkan data menggunakan Shell Sort
shell_sort(data)

# Menambahkan kembali baris header
data = [header] + data

# Menulis data yang telah diurutkan kembali ke file CSV
sorted_file_name = 'sorted_data.csv'
write_csv(sorted_file_name, data)

print("Data telah diurutkan dan disimpan dalam file", sorted_file_name)
