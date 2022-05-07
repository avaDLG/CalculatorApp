from gui import *
from tkinter import ttk


def main():
    window = Tk()
    window.title('Math Functions')
    window.geometry('600x600')
    window.resizable(False, False)
    notebook = ttk.Notebook(window)

    widgets = GUI(window, notebook)
    window.mainloop()


if __name__ == '__main__':
    main()
