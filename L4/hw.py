import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to add a book to the library
def add_book():
    book_name = book_name_entry.get()
    if book_name.strip() == "":
        messagebox.showerror("Error", "Please enter a book name.")
        return
    book_listbox.insert(tk.END, book_name)
    book_name_entry.delete(0, tk.END)
    update_progress()

# Function to remove a book from the library
def remove_book():
    selected_book_index = book_listbox.curselection()
    if not selected_book_index:
        messagebox.showerror("Error", "Please select a book to remove.")
        return
    book_listbox.delete(selected_book_index)
    update_progress()

# Function to update the progress bar
def update_progress():
    total_books = len(book_listbox.get(0, tk.END))
    progress_var.set(total_books)

# Create the main window
root = tk.Tk()
root.title("Library Management System")

# Create and place widgets
book_name_label = tk.Label(root, text="Book Name:")
book_name_label.grid(row=0, column=0, padx=5, pady=5)

book_name_entry = tk.Entry(root)
book_name_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=0, column=2, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.grid(row=0, column=3, padx=5, pady=5)

book_listbox = tk.Listbox(root, height=10)
book_listbox.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=book_listbox.yview)
scrollbar.grid(row=1, column=4, sticky="ns")

book_listbox.config(yscrollcommand=scrollbar.set)

progress_label = tk.Label(root, text="Total Books:")
progress_label.grid(row=2, column=0, padx=5, pady=5)

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, length=200, mode='determinate', variable=progress_var, maximum=10)
progress_bar.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

# Start the tkinter event loop
root.mainloop()
