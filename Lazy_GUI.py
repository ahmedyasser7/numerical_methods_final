from tkinter import *
from tkinter import ttk
import sympy as sp  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import customtkinter as ctk  # type: ignore
from Functions import *
from GUI import *
mx_itr = 1000

# ################################ Calculations ################################


def CalculateBracketing(button_name, entry_function, entry_a, entry_b, entry_tol):
    # Convert data
    x = sp.Symbol('x')
    f_text = entry_function.get()
    # for i in str(f_text):
    #     if i == '^':
    #         i = '**'
    equ = sp.sympify(f_text.replace('^', '**'))
    f = sp.lambdify('x', f_text)

    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())

    # Calculate bisection method results
    if button_name == "Bisection":
        iterations_text, n, x_root, fx, a, b = Bisection(
            f, a, b, tol, max_iter=mx_itr)
    elif button_name == "Trisection":
        iterations_text, n, x_root, fx, a, b = Trisection(
            f, a, b, tol, max_iter=mx_itr)
    else:
        iterations_text, n, x_root, fx, a, b = False_position(
            f, a, b, tol, max_iter=mx_itr)

    # Create a new window for the results
    result_window = Toplevel(root)
    if button_name == "Bisection":
        result_window.title("Bisection Method Result")
    elif button_name == "Trisection":
        result_window.title("Trisection Method Result")
    else:
        result_window.title("False Position Method Result")
    # change_ico(result_window)

    # Display the results

    if button_name == "Bisection":
        result_label = Label(
            result_window, text="Bisection Method Result", font=("Helvetica", 16))
    elif button_name == "Trisection":
        result_label = Label(
            result_window, text="Trisection Method Result", font=("Helvetica", 16))
    else:
        result_label = Label(
            result_window, text="False Position Method Result", font=("Helvetica", 16))

    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, iterations_text)
    iterations_text_widget.pack(padx=10, pady=5)

    labels = ["Final Iteration", "Root",
              "Function Value", "Lower Bound", "Upper Bound"]
    results = [n, x_root, fx, a, b]

    for label, result in zip(labels, results):
        result_text = f"{label}: {result}"
        result_label = Label(
            result_window, text=result_text, font=("Helvetica", 12))
        result_label.pack(anchor="w", padx=10)


def Calculate_Newton(entry_function, entry_x0, entry_tol):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    x0 = float(entry_x0.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = Newton(f, x0, tol)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("Newton Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="Newton Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_x0.delete(0, END)
    entry_x0.insert(0, str(x0))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_Newton.configure(command=lambda: Calculate_Newton(  # type: ignore
        entry_function, entry_x0, entry_tol))


def Calculate_Secant(entry_function, entry_x0, entry_x1, entry_tol):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    x0 = float(entry_x0.get())
    x1 = float(entry_x1.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = Secant(f, x0, x1, tol)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("Secant Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="Secant Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_x0.delete(0, END)
    entry_x0.insert(0, str(x0))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_Secant.configure(command=lambda: Calculate_Secant(  # type: ignore
        entry_function, entry_x0, entry_x1, entry_tol))


def Calculate_MSecant(entry_function, entry_x0, entry_tol):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    x0 = float(entry_x0.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = Mod_Secant(f, x0, tol)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("MOD Secant Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="MOD Secant Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_x0.delete(0, END)
    entry_x0.insert(0, str(x0))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_MSecant.configure(command=lambda: Calculate_MSecant(  # type: ignore
        entry_function, entry_x0, entry_tol))


def Calculate_Directfit(entry_function, entry_x, entry_y):
    x_values = [float(x) for x in entry_x.get().split(",")]
    y_values = [float(y) for y in entry_y.get().split(",")]

    A = DirectFit(x_values, y_values)

    result_window = Toplevel(root)
    result_window.title("Direct Fit Method Result")

    result_label = Label(
        result_window, text="Direct Fit Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {(A)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    for i, coeff in enumerate(A):
        coeff_label = Label(
            result_window, text=f"Coefficient a{i}: {coeff}", font=("Helvetica", 12))
        coeff_label.pack(anchor="w", padx=10)

    entry_function.delete(0, END)
    entry_function.insert(0, "Direct Fit Polynomial Coefficients")

    # Update the button command
    btn_Direct_Fit.configure(command=lambda: Calculate_Directfit(  # type: ignore
        entry_function, entry_x, entry_y))


def Calculate_Lagrange(entry_function, entry_x, entry_y, entry_degree):
    x_values = [float(x) for x in entry_x.get().split(",")]
    y_values = [float(y) for y in entry_y.get().split(",")]
    x_int = float(entry_function.get())

    if len(x_values) != len(y_values):
        return

    y_int = Lagrange(x_values, y_values, x_int)

    result_window = Toplevel(root)
    result_window.title("Lagrange Method Result")

    result_label = Label(
        result_window, text=f"Lagrange Method Result for x = {x_int}", font=("Helvetica", 16))
    result_label.pack(pady=10)

    result_text = f"Interpolated Value: {y_int}"
    result_label = Label(result_window, text=result_text,
                         font=("Helvetica", 12))
    result_label.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {y_int}")
    entry_x.delete(0, END)
    entry_x.insert(0, str(x_int))
    entry_y.delete(0, END)
    entry_y.insert(0, str(y_int))
    entry_degree.delete(0, END)
    entry_degree.insert(0, str(y_int))

    # Update the button command
    btn_calc_Lagrange.configure(command=lambda: Calculate_Lagrange(  # type: ignore
        entry_function, entry_x, entry_y, entry_degree))


def Calculate_BlendBF(entry_function, entry_a, entry_b, entry_tol):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = blendBF(f, a, b, tol, max_iter=mx_itr)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("Bisection & FP Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="Bisection & FP Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_a.delete(0, END)
    entry_a.insert(0, str(a))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_BI_FP.configure(command=lambda: Calculate_BlendBF(  # type: ignore
        entry_function, entry_a, entry_b, entry_tol))


def Calculate_BlendTF(entry_function, entry_a, entry_b, entry_tol):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = blendTF(f, a, b, tol, max_iter=mx_itr)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("Trisection & FP Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="Trisection & FP Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_a.delete(0, END)
    entry_a.insert(0, str(a))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_Tri_FP.configure(command=lambda: Calculate_BlendTF(  # type: ignore
        entry_function, entry_a, entry_b, entry_tol))


def Calculate_False_ModSecant(entry_function, entry_a, entry_b, entry_tol, delta=1e-4):
    x = sp.Symbol('x')
    f_text = entry_function.get()
    f_text.replace('^', '**')
    f = sp.lambdify('x', f_text)

    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())

    # Call the newton function to find the root and iterations
    x_root, iterations = false_mod_secant(
        f, a, b, tol, max_iter=mx_itr, delta=1e-4)

    # Create a new window for the results
    result_window = Toplevel(root)
    result_window.title("Mod Secant & FP Method Result")
    # change_ico(result_window)

    result_label = Label(
        result_window, text="Mod Secant & FP Method Result", font=("Helvetica", 16))
    result_label.pack(pady=10)

    iterations_text_widget = Text(
        result_window, height=15, width=70, font=("Helvetica", 12))
    iterations_text_widget.insert(END, f"Root: {x_root}\n\nIterations:\n")
    for i, iteration in enumerate(iterations):
        iterations_text_widget.insert(END, f"Iteration {i+1}: {iteration}\n")
    iterations_text_widget.pack(padx=10, pady=5)

    # Display root and function value
    result_label_root = Label(
        result_window, text=f"Root: {x_root}", font=("Helvetica", 12))
    result_label_root.pack(anchor="w", padx=10)

    result_label_fx = Label(
        result_window, text=f"Function Value at Root: {f(x_root)}", font=("Helvetica", 12))
    result_label_fx.pack(anchor="w", padx=10)

    # Update the labels
    entry_function.delete(0, END)
    entry_function.insert(0, f"f(x) = {f_text}")
    entry_a.delete(0, END)
    entry_a.insert(0, str(a))
    entry_tol.delete(0, END)
    entry_tol.insert(0, str(tol))

    # Update the button command
    btn_calc_Mod_FP.configure(command=lambda: Calculate_False_ModSecant(  # type: ignore
        entry_function, entry_a, entry_b, entry_tol))


# def Calculate_FiniteDifference(entry_function, entery_x, h=1e-6):
#     pass


# ################################ Creating the GUI ################################
root = Tk()
root.title("Numerical Methods")
Font = ('Berlin Sans FB Demi', 20, 'bold')
root.configure(bg="#fff")
Padx = 0
Pady = 1
ButtonWidth = 15
ButtonHeight = 1


# def change_ico(x):
#     x.iconbitmap("D:\\NM.ico")


def center_screen(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # change_ico(window)
    window_width = screen_width - 200
    window_height = screen_height - 200

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ######################################## Entries ########################################


def Entries_bracketing(entry_function, entry_a, entry_b, entry_tol,
                       lbl_function, lbl_a, lbl_b, lbl_tol):
    # Resize function
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_a.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_b.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_tol.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_a.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_b.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_tol.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc = Button(inner_frame, text="Calculate", command=lambda: CalculateBracketing(entry_function, entry_a, entry_b, entry_tol), font=Font, bg='#3349FF',
                      width=ButtonWidth, height=ButtonHeight)
    btn_calc.grid(row=6, column=0, columnspan=2, padx=(Padx, 0), pady=Pady)


def Entries_Newton(button_name, entry_function, entry_x0, entry_tol,
                   lbl_function, lbl_x0, lbl_tol):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_x0.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_tol.grid(row=2, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x0.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_tol.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    if button_name == "Newton":
        btn_calc_Newton = Button(inner_frame, text="Calculate", command=lambda: Calculate_Newton(entry_function, entry_x0, entry_tol), font=Font, bg='#3349FF',
                                 width=ButtonWidth, height=ButtonHeight)
        btn_calc_Newton.grid(row=6, column=0, columnspan=2,
                             padx=(Padx, 0), pady=Pady)
    else:
        btn_calc_MSecant = Button(inner_frame, text="Calculate", command=lambda: Calculate_MSecant(entry_function, entry_x0, entry_tol), font=Font, bg='#3349FF',
                                  width=ButtonWidth, height=ButtonHeight)
        btn_calc_MSecant.grid(row=6, column=0, columnspan=2,
                              padx=(Padx, 0), pady=Pady)


def Entries_Secant(entry_function, entry_x0, entry_x1, entry_tol,
                   lbl_function, lbl_x0, lbl_x1, lbl_tol):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_x0.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_x1.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_tol.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x0.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x1.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_tol.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_Secant = Button(inner_frame, text="Calculate", command=lambda: Calculate_Secant(entry_function, entry_x0, entry_x1, entry_tol), font=Font, bg='#3349FF',
                             width=ButtonWidth, height=ButtonHeight)
    btn_calc_Secant.grid(row=6, column=0, columnspan=2,
                         padx=(Padx, 0), pady=Pady)


def Entries_DirectFit(entry_function, entry_x, entry_y,
                      lbl_function, lbl_x, lbl_y):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_x.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_y.grid(row=2, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_y.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_DirectFit = Button(inner_frame, text="Calculate", command=lambda: Calculate_Directfit(entry_function, entry_x, entry_y), font=Font, bg='#3349FF',
                                width=ButtonWidth, height=ButtonHeight)
    btn_calc_DirectFit.grid(row=6, column=0, columnspan=2,
                            padx=(Padx, 0), pady=Pady)


def Entries_Lagrange(entry_function, entry_x, entry_y, entry_degree,
                     lbl_function, lbl_x, lbl_y, lbl_degree):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_x.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_y.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_degree.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_y.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_degree.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_Lagrange = Button(inner_frame, text="Calculate", command=lambda: Calculate_Lagrange(entry_function, entry_x, entry_y, entry_degree), font=Font, bg='#3349FF',
                               width=ButtonWidth, height=ButtonHeight)
    btn_calc_Lagrange.grid(row=6, column=0, columnspan=2,
                           padx=(Padx, 0), pady=Pady)


def Entries_BlendBF(entry_function, entry_a, entry_b, entry_eps,
                    lbl_function, lbl_x, lbl_y, lbl_eps):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_a.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_b.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_eps.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_y.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_eps.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_BI_FP = Button(inner_frame, text="Calculate", command=lambda: Calculate_BlendBF(entry_function, entry_a, entry_b, entry_eps), font=Font, bg='#3349FF',
                            width=ButtonWidth, height=ButtonHeight)
    btn_calc_BI_FP.grid(row=6, column=0, columnspan=2,
                        padx=(Padx, 0), pady=Pady)


def Entries_BlendTF(entry_function, entry_a, entry_b, entry_eps,
                    lbl_function, lbl_a, lbl_b, lbl_eps):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_a.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_b.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_eps.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_a.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_b.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_eps.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_Tri_FP = Button(inner_frame, text="Calculate", command=lambda: Calculate_BlendTF(entry_function, entry_a, entry_b, entry_eps), font=Font, bg='#3349FF',
                             width=ButtonWidth, height=ButtonHeight)
    btn_calc_Tri_FP.grid(row=6, column=0, columnspan=2,
                         padx=(Padx, 0), pady=Pady)


def Entries_False_ModSecant(entry_function, entry_a, entry_b, entry_eps,
                            lbl_function, lbl_x, lbl_y, lbl_eps):
    entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
    entry_a.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
    entry_b.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
    entry_eps.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

    lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_x.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_y.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
    lbl_eps.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

    btn_calc_Mod_FP = Button(inner_frame, text="Calculate", command=lambda: Calculate_False_ModSecant(entry_function, entry_a, entry_b, entry_eps), font=Font, bg='#3349FF',
                             width=ButtonWidth, height=ButtonHeight)
    btn_calc_Mod_FP.grid(row=6, column=0, columnspan=2,
                         padx=(Padx, 0), pady=Pady)

# # ! Need edit
# def Entries_FiniteDifference(entry_function, entry_x, entry_y, entry_degree,
#                              lbl_function, lbl_x, lbl_y, lbl_degree):
#     entry_function.grid(row=0, column=1, padx=(0, Padx), pady=Pady)
#     entry_x.grid(row=1, column=1, padx=(0, Padx), pady=Pady)
#     entry_y.grid(row=2, column=1, padx=(0, Padx), pady=Pady)
#     entry_degree.grid(row=3, column=1, padx=(0, Padx), pady=Pady)

#     lbl_function.grid(row=0, column=0, padx=(Padx, 0), pady=Pady+3)
#     lbl_x.grid(row=1, column=0, padx=(Padx, 0), pady=Pady+3)
#     lbl_y.grid(row=2, column=0, padx=(Padx, 0), pady=Pady+3)
#     lbl_degree.grid(row=3, column=0, padx=(Padx, 0), pady=Pady+3)

#     btn_calc_FiniteDiff = Button(inner_frame, text="Calculate", command=lambda: Calculate_FiniteDifference(entry_function, entry_x, entry_y, entry_degree), font=Font, bg='#3349FF',
#                                  width=ButtonWidth, height=ButtonHeight)
#     btn_calc_FiniteDiff.grid(row=6, column=0, columnspan=2,
#                              padx=(Padx, 0), pady=Pady)


def update_content(button_name):
    content_label.config(text=f"{button_name} Method")
    # Reset entry fields
    for widget in inner_frame.winfo_children():
        widget.destroy()

    if button_name == "Bisection" or button_name == "False Position" or button_name == "Trisection":
        entry_function = Entry(inner_frame, font=Font)
        entry_a = Entry(inner_frame, font=Font)
        entry_b = Entry(inner_frame, font=Font)
        entry_tol = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_a = Label(inner_frame, font=Font, bg="#fff", text="A = ")
        lbl_b = Label(inner_frame, font=Font, bg="#fff", text="B = ")
        lbl_tol = Label(inner_frame, font=Font, bg="#fff", text="TOL = ")

        Entries_bracketing(entry_function, entry_a, entry_b, entry_tol,
                           lbl_function, lbl_a, lbl_b, lbl_tol)

        # Pass the arguments to calculate function
        btn_calc = Button(inner_frame, text="Calculate", command=lambda: CalculateBracketing(button_name, entry_function, entry_a, entry_b, entry_tol), font=Font, bg='#3349FF',
                          width=ButtonWidth, height=ButtonHeight)
        btn_calc.grid(row=6, column=0, columnspan=2, padx=(Padx, 0), pady=Pady)
    elif button_name == "Newton" or button_name == "Mod Secant":
        entry_function = Entry(inner_frame, font=Font)
        entry_x0 = Entry(inner_frame, font=Font)
        entry_tol = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x0 = Label(inner_frame, font=Font, bg="#fff", text="X0= ")
        lbl_tol = Label(inner_frame, font=Font, bg="#fff", text="TOL = ")

        Entries_Newton(button_name, entry_function, entry_x0, entry_tol,
                       lbl_function, lbl_x0, lbl_tol)
    elif button_name == "Secant":
        entry_function = Entry(inner_frame, font=Font)
        entry_x0 = Entry(inner_frame, font=Font)
        entry_x1 = Entry(inner_frame, font=Font)
        entry_tol = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x0 = Label(inner_frame, font=Font, bg="#fff", text="X0 = ")
        lbl_x1 = Label(inner_frame, font=Font, bg="#fff", text="X1 = ")
        lbl_tol = Label(inner_frame, font=Font, bg="#fff", text="TOL = ")

        Entries_Secant(entry_function, entry_x0, entry_x1, entry_tol,
                       lbl_function, lbl_x0, lbl_x1, lbl_tol)
    elif button_name == "Direct Fit":
        entry_function = Entry(inner_frame, font=Font)
        entry_x = Entry(inner_frame, font=Font)
        entry_y = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x = Label(inner_frame, font=Font, bg="#fff", text="X = ")
        lbl_y = Label(inner_frame, font=Font, bg="#fff", text="y = ")
        Entries_DirectFit(entry_function, entry_x, entry_y,
                          lbl_function, lbl_x, lbl_y)
    elif button_name == "Lagrange":
        entry_function = Entry(inner_frame, font=Font)
        entry_x = Entry(inner_frame, font=Font)
        entry_y = Entry(inner_frame, font=Font)
        entry_degree = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x = Label(inner_frame, font=Font, bg="#fff", text="X = ")
        lbl_y = Label(inner_frame, font=Font, bg="#fff", text="y = ")
        lbl_degree = Label(inner_frame, font=Font, bg="#fff", text="Degree = ")

        Entries_Lagrange(entry_function, entry_x, entry_y, entry_degree,
                         lbl_function, lbl_x, lbl_y, lbl_degree)

    elif button_name == "Bisection & False Position":
        entry_function = Entry(inner_frame, font=Font)
        entry_x = Entry(inner_frame, font=Font)
        entry_y = Entry(inner_frame, font=Font)
        entry_eps = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x = Label(inner_frame, font=Font, bg="#fff", text="X = ")
        lbl_y = Label(inner_frame, font=Font, bg="#fff", text="y = ")
        lbl_eps = Label(inner_frame, font=Font, bg="#fff", text="Eps = ")

        Entries_BlendBF(entry_function, entry_x, entry_y, entry_eps,
                        lbl_function, lbl_x, lbl_y, lbl_eps)
    elif button_name == "Trisection & False Position":
        entry_function = Entry(inner_frame, font=Font)
        entry_a = Entry(inner_frame, font=Font)
        entry_b = Entry(inner_frame, font=Font)
        entry_eps = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_a = Label(inner_frame, font=Font, bg="#fff", text="X = ")
        lbl_b = Label(inner_frame, font=Font, bg="#fff", text="y = ")
        lbl_eps = Label(inner_frame, font=Font, bg="#fff", text="Eps = ")

        Entries_BlendTF(entry_function, entry_a, entry_b, entry_eps,
                        lbl_function, lbl_a, lbl_b, lbl_eps)

    elif button_name == "Mod Secant & False Position":
        entry_function = Entry(inner_frame, font=Font)
        entry_x = Entry(inner_frame, font=Font)
        entry_y = Entry(inner_frame, font=Font)
        entry_eps = Entry(inner_frame, font=Font)

        lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
        lbl_x = Label(inner_frame, font=Font, bg="#fff", text="X = ")
        lbl_y = Label(inner_frame, font=Font, bg="#fff", text="y = ")
        lbl_eps = Label(inner_frame, font=Font, bg="#fff", text="Eps = ")

        Entries_False_ModSecant(entry_function, entry_x, entry_y, entry_eps,
                                lbl_function, lbl_x, lbl_y, lbl_eps)
    #     # ! Need edit
    # elif button_name == "Finite Difference":
    #     entry_function = Entry(inner_frame, font=Font)
    #     entry_x = Entry(inner_frame, font=Font)
    #     entry_y = Entry(inner_frame, font=Font)
    #     entry_degree = Entry(inner_frame, font=Font)

    #     lbl_function = Label(inner_frame, font=Font, bg="#fff", text="F = ")
    #     lbl_x = Label(inner_frame, font=Font, bg="#fff", text="X = ")
    #     lbl_y = Label(inner_frame, font=Font, bg="#fff", text="y = ")
    #     lbl_degree = Label(inner_frame, font=Font, bg="#fff", text="Degree = ")

    #     Entries_FiniteDifference(entry_function, entry_x, entry_y, entry_degree,
    #                              lbl_function, lbl_x, lbl_y, lbl_degree)


def Main_frame():
    center_screen(root)

    button_frame = Frame(root, bg="#fff")
    button_frame.pack(side=LEFT, fill=Y)

    global content_frame
    content_frame = LabelFrame(root, font=Font, bg="#fff")
    content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    global content_label
    content_label = Label(content_frame, text="", font=Font, bg="#fff")
    content_label.pack(padx=Padx, pady=Pady)

    global inner_frame
    inner_frame = Frame(content_frame, bg="#fff")
    inner_frame.pack(padx=Padx, pady=Pady)

    # Buttons
    btn_bisection = Button(button_frame, text="Bisection", command=lambda: update_content("Bisection"), font=Font, bg='#42a5f5',
                           width=ButtonWidth, height=ButtonHeight)
    btn_bisection.pack(side=TOP, padx=Padx, pady=Pady)

    btn_FalsePosition = Button(button_frame, text="FalsePosition", command=lambda: update_content("False Position"), font=Font, bg='#42a5f5',
                               width=ButtonWidth, height=ButtonHeight)
    btn_FalsePosition.pack(side=TOP, padx=Padx, pady=Pady)

    btn_Newton = Button(button_frame, text="Newton", command=lambda: update_content("Newton"), font=Font, bg='#2196f3', width=ButtonWidth,
                        height=ButtonHeight)
    btn_Newton.pack(side=TOP, padx=Padx, pady=Pady)

    btn_Secant = Button(button_frame, text="Secant", command=lambda: update_content("Secant"), font=Font, bg='#2196f3', width=ButtonWidth,
                        height=ButtonHeight)
    btn_Secant.pack(side=TOP, padx=Padx, pady=Pady)

    btn_ModSecant = Button(button_frame, text="Mod Secant", command=lambda: update_content("Mod Secant"), font=Font, bg='#2196f3',
                           width=ButtonWidth, height=ButtonHeight)
    btn_ModSecant.pack(side=TOP, padx=Padx, pady=Pady)

    btn_Direct_Fit = Button(button_frame, text="Direct Fit", command=lambda: update_content("Direct Fit"), font=Font, bg='#1e88e5',
                            width=ButtonWidth, height=ButtonHeight)
    btn_Direct_Fit.pack(side=TOP, padx=Padx, pady=Pady)

    btn_Larange = Button(button_frame, text="Lagrange", command=lambda: update_content("Lagrange"), font=Font, bg='#1e88e5', width=ButtonWidth,
                         height=ButtonHeight)
    btn_Larange.pack(side=TOP, padx=Padx, pady=Pady)

    btn_Trisection = Button(button_frame, text="Trisection", command=lambda: update_content("Trisection"), font=Font, bg='#1976d2',
                            width=ButtonWidth, height=ButtonHeight)
    btn_Trisection.pack(side=TOP, padx=Padx, pady=Pady)

    btn_BF = Button(button_frame, text="Bisection & FP", command=lambda: update_content("Bisection & False Position"), font=Font, bg='#1976d2',
                    width=ButtonWidth, height=ButtonHeight)
    btn_BF.pack(side=TOP, padx=Padx, pady=Pady)

    btn_TF = Button(button_frame, text="Trisection & FP", command=lambda: update_content("Trisection & False Position"), font=Font, bg='#1976d2',
                    width=ButtonWidth, height=ButtonHeight)
    btn_TF.pack(side=TOP, padx=Padx, pady=Pady)

    btn_MOD_FP = Button(button_frame, text="Mod Secant & FP", command=lambda: update_content("Mod Secant & False Position"), font=Font,
                        bg='#1976d2', width=ButtonWidth, height=ButtonHeight)
    btn_MOD_FP.pack(side=TOP, padx=Padx, pady=Pady)

    # btn_FD = Button(button_frame, text="Finite Difference", command=lambda: update_content("Finite Difference"), font=Font, bg='#1976d2',
    #                 width=ButtonWidth, height=ButtonHeight)
    # btn_FD.pack(side=TOP, padx=Padx, pady=Pady)


Main_frame()
root.mainloop()
