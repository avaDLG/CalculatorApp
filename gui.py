from tkinter import *
from tkinter import messagebox
import math_functions as mf


class GUI:
    """
    A class for the gui and tabs and the methods for when each button is clicked
    """

    def __init__(self, window, notebook) -> None:
        """
        Constructor to create the gui using the created window and notebook from the main class
        :param window: the tkinter window
        :param notebook: the tkinter notebook used to create the tabs with
        """

        self.window = window
        self.notebook = notebook

        # packs the notebook for the tabs
        self.notebook.pack()

        # creates each frame and places it in the notebook to create all the tabs
        self.circle_frame = Frame(self.notebook, width=600, height=600)
        self.square_frame = Frame(self.notebook, width=600, height=600)
        self.rectangle_frame = Frame(self.notebook, width=600, height=600)
        self.triangle_frame = Frame(self.notebook, width=600, height=600)
        self.factorial_frame = Frame(self.notebook, width=600, height=600)
        self.power_frame = Frame(self.notebook, width=600, height=600)
        self.combination_frame = Frame(self.notebook, width=600, height=600)
        self.permutation_frame = Frame(self.notebook, width=600, height=600)

        # creates all the widgets in the circle tab
        self.circle_intro_label = Label(self.circle_frame, text='COMPUTES AREA OF A CIRCLE!',
                                        font=('Arial', 20, 'bold'))
        self.enter_radius_label = Label(self.circle_frame, text='Enter Radius:', font=('Arial', 17, 'italic'))
        self.radius_text = Text(self.circle_frame, height=1, width=20, font=('Arial', 17))
        self.circle_evaluate_button = Button(self.circle_frame, text='Evaluate', height=3, width=10,
                                             font=('Arial', 17, 'bold'), command=self.circle_eval_clicked)
        self.circle_result_label = Label(self.circle_frame, text='Your result is...', font=('Arial', 17))
        self.circle_result_data_label = Label(self.circle_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs all the widgets in the circle tab
        self.circle_intro_label.pack(side='top', pady=15)
        self.enter_radius_label.pack(side='top', pady=10)
        self.radius_text.pack()
        self.circle_evaluate_button.pack(pady=20)
        self.circle_result_label.pack(pady=5)
        self.circle_result_data_label.pack()

        # creates all the widgets in the square tab
        self.square_intro_label = Label(self.square_frame, text='COMPUTES AREA OF A SQUARE!',
                                        font=('Arial', 20, 'bold'))
        self.enter_side_label = Label(self.square_frame, text='Enter Side Length:', font=('Arial', 17, 'italic'))
        self.side_length_text = Text(self.square_frame, height=1, width=20, font=('Arial', 17))
        self.square_eval_button = Button(self.square_frame, text='Evaluate', height=3, width=10,
                                         font=('Arial', 17, 'bold'), command=self.square_eval_clicked)
        self.square_result_label = Label(self.square_frame, text='Your result is...', font=('Arial', 17))
        self.square_result_new_label = Label(self.square_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs all the widgets in the square tab
        self.square_intro_label.pack(side='top', pady=15)
        self.enter_side_label.pack(pady=10)
        self.side_length_text.pack()
        self.square_eval_button.pack(pady=20)
        self.square_result_label.pack(pady=5)
        self.square_result_new_label.pack()

        # creates the widgets in the triangle tab
        self.triangle_intro_label = Label(self.triangle_frame, text='COMPUTES AREA OF A TRIANGLE!',
                                          font=('Arial', 20, 'bold'))
        self.enter_base_tri = Label(self.triangle_frame, text='Enter Base Length:', font=('Arial', 17, 'italic'))
        self.base_tri_text = Text(self.triangle_frame, height=1, width=20, font=('Arial', 17))
        self.enter_height_tri = Label(self.triangle_frame, text='Enter Height Length:', font=('Arial', 17, 'italic'))
        self.height_tri_text = Text(self.triangle_frame, height=1, width=20, font=('Arial', 17))
        self.tri_eval_button = Button(self.triangle_frame, text='Evaluate', height=3, width=10,
                                      font=('Arial', 17, 'bold'), command=self.tri_eval_clicked)
        self.tri_result_label = Label(self.triangle_frame, text='Your result is...', font=('Arial', 17))
        self.tri_result_data_label = Label(self.triangle_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs all the widgets in the square tab
        self.triangle_intro_label.pack(side='top', pady=15)
        self.enter_base_tri.pack(pady=10)
        self.base_tri_text.pack()
        self.enter_height_tri.pack(pady=10)
        self.height_tri_text.pack()
        self.tri_eval_button.pack(pady=20)
        self.tri_result_label.pack(pady=5)
        self.tri_result_data_label.pack()

        # creates the widgets in the rectangle tab
        self.rect_intro_label = Label(self.rectangle_frame, text='COMPUTES AREA OF RECTANGLE',
                                      font=('Arial', 20, 'bold'))
        self.enter_base_rect = Label(self.rectangle_frame, text='Enter Base Length:', font=('Arial', 17, 'italic'))
        self.base_rect_text = Text(self.rectangle_frame, height=1, width=20, font=('Arial', 17))
        self.enter_height_rect = Label(self.rectangle_frame, text='Enter Height Length:', font=('Arial', 17, 'italic'))
        self.height_rect_text = Text(self.rectangle_frame, height=1, width=20, font=('Arial', 17))
        self.rect_eval_button = Button(self.rectangle_frame, text='Evaluate', height=3, width=10,
                                       font=('Arial', 17, 'bold'), command=self.rect_eval_clicked)
        self.rect_result_label = Label(self.rectangle_frame, text='Your result is...', font=('Arial', 17))
        self.rect_result_data_label = Label(self.rectangle_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs the widgets in the rectangle tab
        self.rect_intro_label.pack(side='top', pady=15)
        self.enter_base_rect.pack(pady=10)
        self.base_rect_text.pack()
        self.enter_height_rect.pack(pady=10)
        self.height_rect_text.pack()
        self.rect_eval_button.pack(pady=20)
        self.rect_result_label.pack(pady=5)
        self.rect_result_data_label.pack()

        # creates the widgets in the exponent tab
        self.exponent_intro_label = Label(self.power_frame, text='COMPUTES EXPONENTS!', font=('Arial', 20, 'bold'))
        self.enter_base_exp = Label(self.power_frame, text='Enter The Base:', font=('Arial', 17, 'italic'))
        self.base_exp_text = Text(self.power_frame, height=1, width=20, font=('Arial', 17))
        self.enter_power_exp = Label(self.power_frame, text='Enter The Power:', font=('Arial', 17, 'italic'))
        self.power_exp_text = Text(self.power_frame, height=1, width=20, font=('Arial', 17))
        self.exp_eval_button = Button(self.power_frame, text='Evaluate', height=3, width=10,
                                      font=('Arial', 17, 'bold'), command=self.exp_eval_clicked)
        self.exp_result_label = Label(self.power_frame, text='Your result is...', font=('Arial', 17))
        self.exp_result_data_label = Label(self.power_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs the widgets in the exponent tab
        self.exponent_intro_label.pack(side='top', pady=15)
        self.enter_base_exp.pack(pady=10)
        self.base_exp_text.pack()
        self.enter_power_exp.pack(pady=10)
        self.power_exp_text.pack()
        self.exp_eval_button.pack(pady=20)
        self.exp_result_label.pack(pady=5)
        self.exp_result_data_label.pack()

        # creates the widgets in the factorial tab
        self.fact_intro_label = Label(self.factorial_frame, text='COMPUTES FACTORIALS!', font=('Arial', 20, 'bold'))
        self.enter_num_fact = Label(self.factorial_frame, text='Enter Your Number:', font=('Arial', 17, 'italic'))
        self.num_fact_text = Text(self.factorial_frame, height=1, width=20, font=('Arial', 17))
        self.fact_eval_button = Button(self.factorial_frame, text='Evaluate', height=3, width=10,
                                       font=('Arial', 17, 'bold'), command=self.fact_eval_clicked)
        self.fact_result_label = Label(self.factorial_frame, text='Your result is...', font=('Arial', 17))
        self.fact_result_data_label = Label(self.factorial_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs the widgets in the factorial tab
        self.fact_intro_label.pack(side='top', pady=15)
        self.enter_num_fact.pack(pady=10)
        self.num_fact_text.pack()
        self.fact_eval_button.pack(pady=20)
        self.fact_result_label.pack(pady=5)
        self.fact_result_data_label.pack()

        # creates the widgets in the combination tab
        self.comb_intro_label = Label(self.combination_frame, text='COMPUTES COMBINATIONS!', font=('Arial', 20, 'bold'))
        self.enter_num1_label = Label(self.combination_frame, text='Enter First Whole Number:',
                                      font=('Arial', 17, 'italic'))
        self.comb_num1_text = Text(self.combination_frame, height=1, width=20, font=('Arial', 17))
        self.enter_num2_label = Label(self.combination_frame, text='Enter Second Whole Number:',
                                      font=('Arial', 17, 'italic'))
        self.comb_num2_text = Text(self.combination_frame, height=1, width=20, font=('Arial', 17))
        self.comb_eval_button = Button(self.combination_frame, text='Evaluate', height=3, width=10,
                                       font=('Arial', 17, 'bold'), command=self.comb_eval_clicked)
        self.comb_result_label = Label(self.combination_frame, text='Your result is...', font=('Arial', 17))
        self.comb_result_data_label = Label(self.combination_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs the widgets in the combination tab
        self.comb_intro_label.pack(side='top', pady=15)
        self.enter_num1_label.pack(pady=10)
        self.comb_num1_text.pack()
        self.enter_num2_label.pack(pady=10)
        self.comb_num2_text.pack()
        self.comb_eval_button.pack(pady=20)
        self.comb_result_label.pack(pady=5)
        self.comb_result_data_label.pack()

        # creates the widgets in the permutation tab
        self.perm_intro_label = Label(self.permutation_frame, text='COMPUTES PERMUTATIONS!', font=('Arial', 20, 'bold'))
        self.enter_perm_num1_label = Label(self.permutation_frame, text='Enter First Whole Number:',
                                           font=('Arial', 17, 'italic'))
        self.perm_num1_text = Text(self.permutation_frame, height=1, width=20, font=('Arial', 17))
        self.enter_perm_num2_label = Label(self.permutation_frame, text='Enter Second Whole Number:',
                                           font=('Arial', 17, 'italic'))
        self.perm_num2_text = Text(self.permutation_frame, height=1, width=20, font=('Arial', 17))
        self.perm_eval_button = Button(self.permutation_frame, text='Evaluate', height=3, width=10,
                                       font=('Arial', 17, 'bold'), command=self.perm_eval_clicked)
        self.perm_result_label = Label(self.permutation_frame, text='Your result is...', font=('Arial', 17))
        self.perm_result_data_label = Label(self.permutation_frame, text='', height=4, width=20, font=('Arial', 20))

        # packs the widgets in the permutation tab
        self.perm_intro_label.pack(side='top', pady=15)
        self.enter_perm_num1_label.pack(pady=10)
        self.perm_num1_text.pack()
        self.enter_perm_num2_label.pack(pady=10)
        self.perm_num2_text.pack()
        self.perm_eval_button.pack(pady=20)
        self.perm_result_label.pack(pady=5)
        self.perm_result_data_label.pack()

        # packs the frames
        self.circle_frame.pack()
        self.square_frame.pack()
        self.rectangle_frame.pack()
        self.triangle_frame.pack()
        self.factorial_frame.pack()
        self.power_frame.pack()
        self.combination_frame.pack()
        self.permutation_frame.pack()

        # adds the frames into the notebook
        self.notebook.add(self.circle_frame, text='CIRCLE')
        self.notebook.add(self.square_frame, text='SQUARE')
        self.notebook.add(self.rectangle_frame, text='RECTANGLE')
        self.notebook.add(self.triangle_frame, text='TRIANGLE')
        self.notebook.add(self.factorial_frame, text='!')
        self.notebook.add(self.power_frame, text='^')
        self.notebook.add(self.combination_frame, text='C')
        self.notebook.add(self.permutation_frame, text='P')

    def circle_eval_clicked(self) -> None:
        """
        method when the circle eval button is clicked
        :return: nothing just changes the circle result data label
        """
        try:
            self.circle_result_data_label['text'] = ''
            result = mf.area_of_circle(float(self.radius_text.get(1.0, END)))
            self.circle_result_data_label['text'] = result
            self.radius_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.circle_result_data_label['text'] = ''
            self.radius_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.circle_result_data_label['text'] = ''
            self.radius_text.delete(1.0, END)

    def square_eval_clicked(self) -> None:
        """
        method when the square eval button is clicked
        :return: nothing / changes the rect data label
        """
        try:
            self.square_result_new_label['text'] = ''
            result = mf.area_of_square(float(self.side_length_text.get(1.0, END)))
            self.square_result_new_label['text'] = result
            self.side_length_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.square_result_new_label['text'] = ''
            self.side_length_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.square_result_new_label['text'] = ''
            self.side_length_text.delete(1.0, END)

    def tri_eval_clicked(self) -> None:
        """
        method when the triangle eval button is clicked
        :return: nothing / changes the tri data label
        """
        try:
            self.tri_result_data_label['text'] = ''
            result = mf.area_of_triangle(float(self.base_tri_text.get(1.0, END)),
                                         float(self.height_tri_text.get(1.0, END)))
            self.tri_result_data_label['text'] = result
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)
            self.tri_result_data_label['text'] = ''
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.base_tri_text.delete(1.0, END)
            self.height_tri_text.delete(1.0, END)
            self.tri_result_data_label['text'] = ''

    def rect_eval_clicked(self) -> None:
        """
        method when the rect eval button is clicked
        :return: nothing / changes the rect data label
        """
        try:
            self.rect_result_data_label['text'] = ''
            result = mf.area_of_rectangle(float(self.base_rect_text.get(1.0, END)),
                                          float(self.height_rect_text.get(1.0, END)))
            self.rect_result_data_label['text'] = result
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)
            self.rect_result_data_label['text'] = ''
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.base_rect_text.delete(1.0, END)
            self.height_rect_text.delete(1.0, END)
            self.rect_result_data_label['text'] = ''

    def exp_eval_clicked(self) -> None:
        """
        method when the exponent eval button is clicked
        :return: nothing / changes the exp data label
        """
        try:
            self.exp_result_data_label['text'] = ''
            result = mf.exponent(float(self.base_exp_text.get(1.0, END)), float(self.power_exp_text.get(1.0, END)))
            self.exp_result_data_label['text'] = result
            self.base_exp_text.delete(1.0, END)
            self.power_exp_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.exp_result_data_label['text'] = ''
            self.base_exp_text.delete(1.0, END)
            self.power_exp_text.delete(1.0, END)
        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.exp_result_data_label['text'] = ''
            self.base_exp_text.delete(1.0, END)
            self.power_exp_text.delete(1.0, END)

    def fact_eval_clicked(self) -> None:
        """
        method when the factorial eval button is clicked
        :return: nothing / changes the factorial result data label
        """
        try:
            self.fact_result_data_label['text'] = ''
            result = mf.factorial(float(self.num_fact_text.get(1.0, END)))
            self.fact_result_data_label['text'] = result
            self.num_fact_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.num_fact_text.delete(1.0, END)
            self.fact_result_data_label['text'] = ''

        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.num_fact_text.delete(1.0, END)
            self.fact_result_data_label['text'] = ''

    def comb_eval_clicked(self) -> None:
        """
        method when the combination eval button is clicked
        :return: nothing / changes the combination result data tabel
        """
        try:
            self.comb_result_data_label['text'] = ''
            result = mf.combination(int(self.comb_num1_text.get(1.0, END)), int(self.comb_num2_text.get(1.0, END)))
            self.comb_result_data_label['text'] = result
            self.comb_num1_text.delete(1.0, END)
            self.comb_num2_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.comb_result_data_label['text'] = ''
            self.comb_num1_text.delete(1.0, END)
            self.comb_num2_text.delete(1.0, END)

        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.comb_result_data_label['text'] = ''
            self.comb_num1_text.delete(1.0, END)
            self.comb_num2_text.delete(1.0, END)

    def perm_eval_clicked(self) -> None:
        """
        method for when the permutation eval button is clicked
        :return: nothing / changes the permutation result data label
        """
        try:
            self.perm_result_data_label['text'] = ''
            result = mf.permutation(int(self.perm_num1_text.get(1.0, END)), int(self.perm_num2_text.get(1.0, END)))
            self.perm_result_data_label['text'] = result
            self.perm_num1_text.delete(1.0, END)
            self.perm_num2_text.delete(1.0, END)

        except TypeError:
            messagebox.showerror('showerror', 'Must type a number')
            self.perm_result_data_label['text'] = ''
            self.perm_num1_text.delete(1.0, END)
            self.perm_num2_text.delete(1.0, END)

        except ValueError:
            messagebox.showerror('showerror', 'Must type a positive number')
            self.perm_result_data_label['text'] = ''
            self.perm_num1_text.delete(1.0, END)
            self.perm_num2_text.delete(1.0, END)
