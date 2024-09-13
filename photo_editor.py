import customtkinter as ctk
from image_widgets import ImageImport, ImageOutput
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor') 
        self.minsize(800, 500) # cannot make it smaller than 800x500
        
        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)
        
        # all the widgets
        self.image_import = ImageImport(self, self.import_image)
        
    def import_image(self, path):
        self.image = Image.open(path)
        self.image_import.grid_forget() # unmap this widget or get rid of it from the screen
        
        self.image_output = ImageOutput(self) # show the new widget with image after image has been chosen in files
        
           
if __name__ == '__main__':
    app = App()
    app.mainloop()