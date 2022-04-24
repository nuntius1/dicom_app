from tkinter import *
from tkinter import ttk
from tkinter import filedialog


window_x = 960
window_y = 730

window = Tk()
window.geometry(str(window_x) + 'x' + str(window_y))
window.title('DICOM VIEWER APP')
window.configure()






# print(window.configure().keys())
pw = ttk.Panedwindow(window, orient=HORIZONTAL)
f1 = ttk.Labelframe(pw, text='Pane1', width=window_x/2, height=window_y/2)
f2 = ttk.Labelframe(pw, text='Pane2', width=window_x/2, height=window_y/2)   

def select_file():
    filetypes = (
       
    )

    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
#file button
ttk.Button(f1, text="Open a file", command=select_file).grid()

pw.add(f1)
pw.add(f2)

pw.grid()
# frm = ttk.Frame(window, padding=10)


# frm.grid()
# ttk.Label(frm, text="Hello World! ... things just go interesting init").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)
window.mainloop()