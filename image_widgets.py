import customtkinter as ctk
from tkinter import filedialog, Canvas

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_image):
        super().__init__(parent)
        self.grid(row=0, column=0, columnspan=2)
        self.import_image = import_image
        
        # button
        self.import_btn = ctk.CTkButton(self, text='open image', command=self.open_dialog)
        self.import_btn.grid()
        
    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_image(path)
        

class ImageOutput(Canvas):
    def __init__(self, parent):
        super().__init__(parent, background='red')
        self.grid(row=0, column=1, sticky='nsew')