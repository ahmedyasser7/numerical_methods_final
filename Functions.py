from Numircal_project_GUI import *
from tkinter import *
from tkinter import ttk
import sympy as sp  # type: ignore
import numpy as np  # type: ignore
import customtkinter as ctk  # type: ignore
mx_itr = 1000

# ############################################################################################## #
# ################################ Bisection and Falsi Position ################################
# ############################################################################################## #


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

        iterations_text += f"Iteration {n}: Root = {\
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
        iterations_text += f"Iteration {n}: Root = {\
            x:.16f}, Function Value = {fx:.16f}\n"

    return iterations_text, n, x, fx, a, b

# ################################ Newton ################################


def Newton(f, x0, tol, max_iter=mx_itr):
    def f_prime(x): return (f(x + tol) - f(x - tol)) / \
        (2 * tol)  # Approximate derivative

    x = x0
    iterations = []
    while abs(f(x)) > tol and len(iterations) < max_iter:
        x = x - f(x) / f_prime(x)
        iterations.append(x)

    return x, iterations

# ################################ Secant ################################


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

# ################################ Trisection ################################


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
        iterations_text += f"Iteration {n}: Root = {\
            x:.16f}, Function Value = {fx:.16f}\n"

    return iterations_text, n, x, fx, a, b

# ################################ Mod Secant ################################


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

# ################################ Direct Fit ################################


def DirectFit(x, y):
    V = np.vander(x, increasing=True)
    A = np.linalg.solve(V, y)
    return A


def Evaluate(A, x_int):
    y_int = 0
    for i, a in enumerate(A):
        y_int += a * (x_int ** i)

    return y_int

# ############################### Lagrange ################################


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

# ################################# Bisection & FP ######################################

# ################################# Trisection & FP ######################################

# ################################# Mod Secant & FP ######################################

# ################################# Finite Difference #####################################


def forward_difference(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h=1e-6):
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h=1e-6):
    return (f(x + h/2) - f(x - h/2)) / h
