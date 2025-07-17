
import csv
from tkinter import ttk, filedialog, Tk, messagebox

# Global variable to store the current file path
current_file_path = ''

def clear_treeview(tree):
    tree.delete(*tree.get_children()) # ini biar ngosongin treeview dulu, jadi klo sebelumnya ada data, dia ga ketumpuk

def openFile_keberangkatan(tree):
    global current_file_path
    # Uncomment the following line to enable file dialog for selecting the CSV file
    # current_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    current_file_path = 'database\Jakarta\package_out.csv' 

    if current_file_path:
        with open(current_file_path, 'r') as file:
            csvreader = csv.reader(file)
            headers = next(csvreader)

            clear_treeview(tree)

            tree["column"] = headers
            tree["show"] = "headings"

            for col in tree["column"]:
                tree.heading(col, text=col)

            for row in csvreader:
                tree.insert("", "end", values=row)

        tree.pack()

def move_selected_row(tree, target_file_path):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No selection", "Please select a row to move.")
        return

    row_values = tree.item(selected_item, "values")
    
    # Move row to target CSV file
    with open(target_file_path, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(row_values)

    # Remove row from the treeview and the original CSV file
    tree.delete(selected_item)
    remove_row_from_csv(current_file_path, row_values)

def remove_row_from_csv(file_path, row_values):
    with open(file_path, 'r') as file:
        rows = list(csv.reader(file))
    
    with open(file_path, 'w', newline='') as file:
        csvwriter = csv.writer(file)
        for row in rows:
            if row != list(row_values):
                csvwriter.writerow(row)

def main():
    root = Tk()
    tree = ttk.Treeview(root)
    open_button = ttk.Button(root, text="Open File", command=lambda: openFile_keberangkatan(tree))
    move_button = ttk.Button(root, text="Move Selected Row", command=lambda: move_selected_row(tree, "database/Surabaya/Package_in_copy.csv" ))

    open_button.pack()
    move_button.pack()
    tree.pack()

    root.mainloop()

if __name__ == "__main__":
    main()