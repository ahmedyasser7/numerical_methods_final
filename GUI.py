import sympy as sp  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
import streamlit as st
mx_itr = 1000


def Bisection(f, a, b, tol, max_iter=mx_itr):
    n = 0
    iterations_text = ""
    while n < max_iter:
        n += 1
        x = (a + b) / 2
        fx = f(x)
        fa = f(a)
        if abs(fx) <= tol:
            break
        if fa * fx < 0:
            b = x
        else:
            a = x
        iterations_text += f"Iteration {n}: Root = {
            x:.16f}, Function Value = {fx:.16f}\n"
    return iterations_text, n, x, fx, a, b


def False_position(f, a, b, tol, max_iter=mx_itr):
    n = 0
    iterations_text = ""
    while n < max_iter:
        n += 1
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))
        fx = f(x)
        fa = f(a)
        if abs(fx) <= tol:
            break
        elif fa * fx < 0:
            b = x
        else:
            a = x
        iterations_text += f"Iteration {n}: Root = {
            x:.16f}, Function Value = {fx:.16f}\n"
    return iterations_text, n, x, fx, a, b


def Newton(f, x0, tol, max_iter=mx_itr):
    def f_prime(x): return (f(x + tol) - f(x - tol)) / (2 * tol)
    x = x0
    iterations = []
    while abs(f(x)) > tol and len(iterations) < max_iter:
        x = x - f(x) / f_prime(x)
        iterations.append(x)
    return x, iterations


def Secant(f, x0, x1, tol, max_iter=mx_itr):
    iterations = []
    i = 1
    while i < max_iter:
        i += 1
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append(x2)
        if abs(f(x2)) <= tol:
            break
        x0 = x1
        x1 = x2
    return x2, iterations


def Trisection(f, a, b, tol, max_iter=mx_itr):
    n = 0
    iterations_text = ""
    while n < max_iter:
        n += 1
        x1 = (b + 2*a) / 3
        x2 = (2*b + a) / 3
        fx1 = f(x1)
        fx2 = f(x2)
        fa = f(a)
        if abs(fx1) < abs(fx2):
            x = x1
            fx = fx1
        else:
            x = x2
            fx = fx2
        if abs(fx) <= tol:
            break
        elif fa * fx1 < 0:
            b = x1
        elif fx1 * fx2 < 0:
            a = x1
            b = x2
        else:
            a = x2
        iterations_text += f"Iteration {n}: Root = {
            x:.16f}, Function Value = {fx:.16f}\n"
    return iterations_text, n, x, fx, a, b


def Mod_Secant(f, x0, tol, max_iter=mx_itr, delta=1e-4):
    iterations = []
    n = 0
    x = x0
    while n < max_iter:
        n += 1
        fx = f(x)
        gx = (f(x + delta) - fx) / delta
        x = x - fx / gx
        iterations.append(x)
        fx = f(x)
        if abs(fx) <= tol:
            break
    return x, iterations


def DirectFit(x, y):
    V = np.vander(x, increasing=True)
    A = np.linalg.solve(V, y)
    return A


def Evaluate(A, x_int):
    y_int = 0
    for i, a in enumerate(A):
        y_int += a * (x_int ** i)

    return y_int


def Lagrange(x, y, x_int):
    n = len(x)
    y_int = 0
    for i in range(n):
        basis = 1
        for j in range(n):
            if i != j:
                basis *= (x_int - x[j]) / (x[i] - x[j])

        y_int += y[i] * basis

    return y_int


def blendBF(f, a, b, tol, max_iter=mx_itr):
    n = 0
    a1 = a
    b1 = b
    a2 = a
    b2 = b
    while n < max_iter:
        n += 1
        fa = f(a)
        fb = f(b)
        xB = (a + b) / 2
        fxB = f(xB)
        xF = (a*fb - b*fa) / (fb - fa)
        fxF = f(xF)
        if abs(fxB) < abs(fxF):
            x = xB
            fx = fxB
        else:
            x = xF
            fx = fxF
        if abs(fx) <= tol:
            break
        if fa*fxB < 0:
            b1 = xB
        else:
            a1 = xB
        if fa*fxF < 0:
            b2 = xF
        else:
            a2 = xF
        a = max(a1, a2)
        b = min(b1, b2)
    return fx, n


def blendTF(f, a, b, tol, max_iter=mx_itr):
    n = 0
    a1 = a
    b1 = b
    a2 = a
    b2 = b
    while n < max_iter:
        n += 1
        fa = f(a)
        fb = f(b)
        xT1 = (b + 2*a) / 3
        xT2 = (2*b + a) / 3
        fxT1 = f(xT1)
        fxT2 = f(xT2)
        xF = a - (fa*(b-a)) / (fb-fa)
        fxF = f(xF)
        x = xT1
        fx = fxT1
        if abs(fxT2) < abs(fx):
            x = xT2
            fx = fxT2

        if abs(fxF) < abs(fx):
            x = xF
            fx = fxF
        if abs(fx) <= tol:
            break
        if fa * fxT1 < 0:
            b1 = xT1
        elif fxT1 * fxT2 < 0:
            a1 = xT1
            b1 = xT2
        else:
            a1 = xT2
        if fa * fxF < 0:
            b2 = xF
        else:
            a2 = xF
        a = max(a1, a2)
        b = min(b1, b2)
    return n, x, fx, a, b


def false_mod_secant(f, a, b, tol, max_iter=mx_itr, delta=1e-4):
    n = 0
    while n < max_iter:
        n += 1
        fa = f(a)
        fb = f(b)
        x = (a*fb - b*fa) / (fb - fa)
        fx = f(x)
        if abs(fx) <= tol:
            break
        else:
            f_delta = f(delta + x)
            xS = x - (delta * fx) / (f_delta - fx)
            fxS = f(xS)
            if (abs(fxS) < abs(fx)) and (xS > a and xS < b):
                if fa * fxS < 0:
                    b = xS
                else:
                    a = xS
            else:
                if fa * fx < 0:
                    b = x
                else:
                    a = x
    return n, x, fx, a, b


def forward_difference(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h=1e-6):
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h=1e-6):
    return (f(x + h/2) - f(x - h/2)) / h

# #########################################


# Calculations:
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

# #####################################################
# The GUI part:

def show_introduction():
    st.header("Introduction")
    st.image("LazyProject_NM_v5/coala.jpg", caption="we are a lazy team!")

def show_calculator():
    st.header("Calculator")

    method = st.sidebar.selectbox("Select Method", [
        "Bisection", "False Position", "Newton", "Secant", "Mod Secant",
        "Direct Fit", "Lagrange", "Trisection", "Bisection & False Position",
        "Trisection & False Position", "Mod Secant & False Position"
    ])

    if method == "Bisection" or method == "False Position":
        function = st.text_input("Enter the function (F):")
        a = st.number_input("Enter value for a:")
        b = st.number_input("Enter value for b:")
        tol = st.number_input("Enter tolerance (TOL):")

        if st.button("Calculate"):
            if method == "Bisection":
                CalculateBracketing(function, a, b, tol)
            else:
                CalculateBracketing(function, a, b, tol)
        elif method == "Newton" or method == "Mod Secant":
            function = st.text_input("Enter the function (F):")
            x0 = st.number_input("Enter initial guess (X0):")
            tol = st.number_input("Enter tolerance (TOL):")

        if st.button("Calculate"):
            if method == "Newton":
                Calculate_Newton(function, x0, tol)
            else:
                Calculate_MSecant(function, x0, tol)
        elif method == "Secant":
            function = st.text_input("Enter the function (F):")
            x0 = st.number_input("Enter first initial guess (X0):")
            x1 = st.number_input("Enter second initial guess (X1):")
            tol = st.number_input("Enter tolerance (TOL):")

        if st.button("Calculate"):
            Calculate_Secant(function, x0, x1, tol)
        elif method == "Direct Fit":
            function = st.text_input("Enter the function (F):")
            x = st.text_input(
                "Enter values of X separated by commas (e.g., 1,2,3):")
            y = st.text_input(
                "Enter values of Y separated by commas (e.g., 4,5,6):")

        if st.button("Calculate"):
            Calculate_Directfit(function, x, y)
        elif method == "Lagrange":
            function = st.text_input("Enter the function (F):")
            x = st.text_input(
                "Enter values of X separated by commas (e.g., 1,2,3):")
            y = st.text_input(
                "Enter values of Y separated by commas (e.g., 4,5,6):")
            degree = st.number_input("Enter degree:")

        if st.button("Calculate"):
            Calculate_Lagrange(function, x, y, degree)
        elif method == "Trisection":
            function = st.text_input("Enter the function (F):")
            a = st.number_input("Enter value for a:")
            b = st.number_input("Enter value for b:")
            eps = st.number_input("Enter epsilon (EPS):")

        if st.button("Calculate"):
            Calculate_BlendTF(function, a, b, eps)
        elif method == "Bisection & False Position":
            function = st.text_input("Enter the function (F):")
            a = st.number_input("Enter value for a:")
            b = st.number_input("Enter value for b:")
            eps = st.number_input("Enter epsilon (EPS):")

        if st.button("Calculate"):
            Calculate_BlendBF(function, a, b, eps)
        elif method == "Trisection & False Position":
            function = st.text_input("Enter the function (F):")
            a = st.number_input("Enter value for a:")
            b = st.number_input("Enter value for b:")
            eps = st.number_input("Enter epsilon (EPS):")

        if st.button("Calculate"):
            Calculate_BlendTF(function, a, b, eps)
        elif method == "Mod Secant & False Position":
            function = st.text_input("Enter the function (F):")
            x = st.number_input("Enter value for x:")
            y = st.number_input("Enter value for y:")
            eps = st.number_input("Enter epsilon (EPS):")

        if st.button("Calculate"):
            Calculate_False_ModSecant(function, x, y, eps)

def main():
    st.title("Numerical Methods Calculator")

    # Create tabs
    tabs = ["Introduction", "Calculator"]
    selected_tab = st.radio("Select Tab", tabs)

    # Display content based on selected tab
    if selected_tab == "Introduction":
        show_introduction()
    elif selected_tab == "Calculator":
        show_calculator()


if __name__ == "__main__":
    main()
