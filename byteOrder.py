import tkinter as tk
from tkinter import filedialog
import struct
import os

class ByteOrderConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self)
        self.open_button["text"] = "Open File"
        self.open_button["command"] = self.open_file
        self.open_button.pack(side="top")
        self.file_path_label = tk.Label(self)
        self.file_path_label.pack(side="top")
        self.convert_button = tk.Button(self)
        self.convert_button["text"] = "Convert Byte Order"
        self.convert_button["command"] = self.convert_byte_order
        self.convert_button.pack(side="top")
        self.status_label = tk.Label(self, text="")
        self.status_label.pack(side="top")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_label.configure(text="File: " + file_path)
            self.file_path = file_path

    def convert_byte_order(self):
        if not hasattr(self, 'file_path'):
            self.status_label.configure(text="No file selected")
            return

        try:
            with open(self.file_path, "rb") as f:
                data = f.read()
                value = struct.unpack(">I", data)[0]  
            new_data = struct.pack("<I", value) 
            file_name, file_extension = os.path.splitext(self.file_path)
            output_file_path = file_name + "_little_endian" + file_extension
            with open(output_file_path, "wb") as f:
                f.write(new_data)

            self.status_label.configure(text="Byte order converted successfully")
        except Exception as e:
            self.status_label.configure(text="Error: " + str(e))

root = tk.Tk()
app = ByteOrderConverter(master=root)
app.mainloop()
