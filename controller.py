'''
from gui import *
from tkinter import *


def circle_eval_clicked(self):
    try:
        self.circle_result_text.delete(1.0, END)
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
        self.square_result_text.delete(1.0, END)
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
        self.tri_result_text.delete(1.0, END)
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
        self.rect_result_text.delete(1.0, END)
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


def exp_eval_clicked(self):
    try:
        self.exp_result_text.delete(1.0, END)
        result = mf.exponent(float(self.base_exp_text.get(1.0, END)), float(self.power_exp_text.get(1.0, END)))
        self.exp_result_text.insert(1.0, result)
        self.base_exp_text.delete(1.0, END)
        self.power_exp_text.delete(1.0, END)

    except TypeError:
        messagebox.showerror('showerror', 'Must type a number')
        self.exp_result_text.delete(1.0, END)
        self.base_exp_text.delete(1.0, END)
        self.power_exp_text.delete(1.0, END)
    except ValueError:
        messagebox.showerror('showerror', 'Must type a positive number')
        self.base_rect_text.delete(1.0, END)
        self.base_exp_text.delete(1.0, END)
        self.power_exp_text.delete(1.0, END)


def fact_eval_clicked(self):
    try:
        self.fact_result_text.delete(1.0, END)
        result = mf.factorial(float(self.num_fact_text.get(1.0, END)))
        self.fact_result_text.insert(1.0, result)
        self.num_fact_text.delete(1.0, END)

    except TypeError:
        messagebox.showerror('showerror', 'Must type a number')
        self.num_fact_text.delete(1.0, END)
        self.fact_result_text.delete(1.0, END)

    except ValueError:
        messagebox.showerror('showerror', 'Must type a positive number')
        self.num_fact_text.delete(1.0, END)
        self.fact_result_text.delete(1.0, END)


def comb_eval_clicked(self):
    try:
        self.comb_result_text.delete(1.0, END)
        result = mf.combination(int(self.comb_num1_text.get(1.0, END)), int(self.comb_num2_text.get(1.0, END)))
        self.comb_result_text.insert(1.0, result)
        self.comb_num1_text.delete(1.0, END)
        self.comb_num2_text.delete(1.0, END)

    except TypeError:
        messagebox.showerror('showerror', 'Must type a number')
        self.comb_result_text.delete(1.0, END)
        self.comb_num1_text.delete(1.0, END)
        self.comb_num2_text.delete(1.0, END)

    except ValueError:
        messagebox.showerror('showerror', 'Must type a positive number')
        self.comb_result_text.delete(1.0, END)
        self.comb_num1_text.delete(1.0, END)
        self.comb_num2_text.delete(1.0, END)


def perm_eval_clicked(self):
    try:
        self.perm_result_text.delete(1.0, END)
        result = mf.permutation(int(self.perm_num1_text.get(1.0, END)), int(self.perm_num2_text.get(1.0, END)))
        self.perm_result_text.insert(1.0, result)
        self.perm_num1_text.delete(1.0, END)
        self.perm_num2_text.delete(1.0, END)

    except TypeError:
        messagebox.showerror('showerror', 'Must type a number')
        self.perm_result_text.delete(1.0, END)
        self.perm_num1_text.delete(1.0, END)
        self.perm_num2_text.delete(1.0, END)

    except ValueError:
        messagebox.showerror('showerror', 'Must type a positive number')
        self.perm_result_text.delete(1.0, END)
        self.perm_num1_text.delete(1.0, END)
        self.perm_num2_text.delete(1.0, END)
'''
