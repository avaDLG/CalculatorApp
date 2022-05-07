from gui import *
from tkinter import ttk


def main():
    # creating the gui window
    window = Tk()
    # titling the window
    window.title('Math Functions')
    # setting the window dimensions
    window.geometry('600x600')
    # setting it to non-resizable
    window.resizable(False, False)
    # creating the notebook and passing through the window
    notebook = ttk.Notebook(window)

    widgets = GUI(window, notebook)
    window.mainloop()


if __name__ == '__main__':
    main()
