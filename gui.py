from tkinter import *
from tkinter import messagebox
import math_functions as mf


class GUI:

    def __init__(self, window, notebook):

        self.window = window
        self.notebook = notebook

        self.notebook.pack()

        self.circle_frame = Frame(self.notebook, width=500, height=500)
        self.square_frame = Frame(self.notebook, width=500, height=500)
        self.rectangle_frame = Frame(self.notebook, width=500, height=500)
        self.triangle_frame = Frame(self.notebook, width=500, height=500)
        self.factorial_frame = Frame(self.notebook, width=500, height=500)
        self.power_frame = Frame(self.notebook, width=500, height=500)
        self.combination_frame = Frame(self.notebook, width=500, height=500)
        self.permutation_frame = Frame(self.notebook, width=500, height=500)

        self.circle_intro_label = Label(self.circle_frame, text='COMPUTES AREA OF A CIRCLE!')
        self.enter_radius_label = Label(self.circle_frame, text='ENTER RADIUS:')
        self.radius_text = Text(self.circle_frame, height=1, width=17)
        self.circle_evaluate_button = Button(self.circle_frame, text='Evaluate...',
                                             command=self.circle_eval_clicked)
        self.circle_result_label = Label(self.circle_frame, text='Your result is...')
        self.circle_result_text = Text(self.circle_frame, height=1, width=17)

        self.circle_intro_label.pack(side='top', pady=10)
        self.enter_radius_label.pack(side='top', pady=10)
        self.radius_text.pack()
        self.circle_evaluate_button.pack(pady=20)
        self.circle_result_label.pack(pady=35)
        self.circle_result_text.pack()

        self.square_intro_label = Label(self.square_frame, text='COMPUTES AREA OF A SQUARE!')
        self.enter_side_label = Label(self.square_frame, text='ENTER SIDE LENGTH')
        self.side_length_text = Text(self.square_frame, height=1, width=17)
        self.square_eval_button = Button(self.square_frame, text='Evaluate...', command=self.square_eval_clicked)
        self.square_result_label = Label(self.square_frame, text='Your result is...')
        self.square_result_text = Text(self.square_frame, height=1, width=17)

        self.square_intro_label.pack(side='top', pady=10)
        self.enter_side_label.pack(pady=10)
        self.side_length_text.pack()
        self.square_eval_button.pack(pady=20)
        self.square_result_label.pack(pady=35)
        self.square_result_text.pack()

        self.triangle_intro_label = Label(self.triangle_frame, text='COMPUTES AREA OF A TRIANGLE!')
        self.enter_base_tri = Label(self.triangle_frame, text='ENTER BASE LENGTH')
        self.base_tri_text = Text(self.triangle_frame, height=1, width=17)
        self.enter_height_tri = Label(self.triangle_frame, text='ENTER HEIGHT LENGTH')
        self.height_tri_text = Text(self.triangle_frame, height=1, width=17)
        self.tri_eval_button = Button(self.triangle_frame, text='Evaluate...', command=self.tri_eval_clicked)
        self.tri_result_label = Label(self.triangle_frame, text='Your result is...')
        self.tri_result_text = Text(self.triangle_frame, height=1, width=17)

        self.triangle_intro_label.pack(side='top', pady=10)
        self.enter_base_tri.pack(pady=10)
        self.base_tri_text.pack()
        self.enter_height_tri.pack(pady=10)
        self.height_tri_text.pack()
        self.tri_eval_button.pack(pady=20)
        self.tri_result_label.pack(pady=35)
        self.tri_result_text.pack()

        self.rect_intro_label = Label(self.rectangle_frame, text='COMPUTES AREA OF RECTANGLE')
        self.enter_base_rect = Label(self.rectangle_frame, text='ENTER BASE LENGTH')
        self.base_rect_text = Text(self.rectangle_frame, height=1, width=17)
        self.enter_height_rect = Label(self.rectangle_frame, text='ENTER HEIGHT LENGTH')
        self.height_rect_text = Text(self.rectangle_frame, height=1, width=17)
        self.rect_eval_button = Button(self.rectangle_frame, text='Evaluate...', command=self.rect_eval_clicked)
        self.rect_result_label = Label(self.rectangle_frame, text='Your result is...')
        self.rect_result_text = Text(self.rectangle_frame, height=1, width=17)

        self.rect_intro_label.pack(side='top', pady=10)
        self.enter_base_rect.pack(pady=10)
        self.base_rect_text.pack()
        self.enter_height_rect.pack(pady=10)
        self.height_rect_text.pack()
        self.rect_eval_button.pack(pady=20)
        self.rect_result_label.pack(pady=35)
        self.rect_result_text.pack()

        self.circle_frame.pack()
        self.square_frame.pack()
        self.rectangle_frame.pack()
        self.triangle_frame.pack()
        self.factorial_frame.pack()
        self.power_frame.pack()
        self.combination_frame.pack()
        self.permutation_frame.pack()

        self.notebook.add(self.circle_frame, text='CIRCLE')
        self.notebook.add(self.square_frame, text='SQUARE')
        self.notebook.add(self.rectangle_frame, text='RECTANGLE')
        self.notebook.add(self.triangle_frame, text='TRIANGLE')
        self.notebook.add(self.factorial_frame, text='!')
        self.notebook.add(self.power_frame, text='^')
        self.notebook.add(self.combination_frame, text='C')
        self.notebook.add(self.permutation_frame, text='P')

    def circle_eval_clicked(self):
        try:
            result = mf.area_of_circle(float(self.radius_text.get(1.0, END)))
            self.circle_result_text.insert(1.0, str(result))
            self.radius_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.circle_result_text.delete(1.0, END)
            self.radius_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.circle_result_text.delete(1.0, END)
            self.radius_text.delete(1.0, END)

    def square_eval_clicked(self):
        try:
            result = mf.area_of_square(float(self.side_length_text.get(1.0, END)))
            self.square_result_text.insert(1.0, result)
            self.side_length_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.square_result_text.delete(1.0, END)
            self.side_length_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.square_result_text.delete(1.0, END)
            self.side_length_text.delete(1.0, END)

    def tri_eval_clicked(self):
        try:
            result = mf.area_of_triangle(float(self.base_tri_text.get(1.0, END)),
                                         float(self.height_tri_text.get(1.0, END)))
            self.tri_result_text.insert(1.0, result)
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)
            self.tri_result_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)
            self.tri_result_text.delete(1.0, END)

    def rect_eval_clicked(self):
        try:
            result = mf.area_of_rectangle(float(self.base_rect_text.get(1.0, END)),
                                          float(self.height_rect_text.get(1.0, END)))
            self.rect_result_text.insert(1.0, result)
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)
            self.rect_result_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)
            self.rect_result_text.delete(1.0, END)










