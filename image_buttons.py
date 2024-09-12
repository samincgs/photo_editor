import customtkinter as ctk

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_image):
        super().__init__(parent)
        self.grid(row=0, column=0, columnspan=2)
        self.import_image = import_image
        
        # button
        self.import_btn = ctk.CTkButton(self, text='open image', command=self.open_dialog)
        self.import_btn.grid()
        
    def open_dialog(self):
        path = 'test'
        self.import_image(path)
        