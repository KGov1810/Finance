import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image

from Models.black_scholes import BlackScholes


class GUI:

    def __init__(self, **kwargs):
        self.principal_window = kwargs.get("main_window")

        self.entries = {}

        self.initial_frame = None
        self.model_frame = None
        self.label_call_result = None
        self.label_put_result = None

    def _select_model(self, model_name: str):
        """Select the model you want"""
        self.initial_frame.pack_forget()

        if model_name == "Black-Scholes":
            self._create_black_scholes_window()
        elif model_name == "Binomial":
            self.model_frame = tk.Frame(self.principal_window)
            self.model_frame.pack(fill='both', expand=True)

    def create_principal_window(self):
        """Create the principal window"""
        self.initial_frame = tk.Frame(self.principal_window)
        self.initial_frame.pack(fill='both', expand=True)

        tk.Label(self.initial_frame, text="Choose your pricing model").pack(pady=20)

        button_bs = tk.Button(self.initial_frame, text="Black Scholes Model",
                              command=lambda: self._select_model("Black-Scholes"))
        button_bs.pack(padx=20, pady=10)

        button_binomial = tk.Button(self.initial_frame, text="Binomial Model",
                                    command=lambda: self._select_model("Binomial"))
        button_binomial.pack(padx=20, pady=10)

    def _create_black_scholes_window(self):
        """Create specific window for the black-scholes model"""
        self.model_frame = tk.Frame(self.principal_window)
        self.model_frame.pack(fill='both', expand=True)

        labels = {
            "S": "Spot price (S):",
            "K": "Strike Price (K):",
            "T": "Maturity (T):",
            "r": "Risk Free Rate (r):",
            "sigma": "Volatility (sigma):"
        }
        defaults = {"S": 100,
                    "K": 100,
                    "T": 1,
                    "r": 0.05,
                    "sigma": 0.2}

        size_letter = tkfont.Font(family="Verdana", size=9, weight="bold")

        for i, (key, label_text) in enumerate(labels.items()):
            label = tk.Label(self.model_frame, text=label_text, font=size_letter)
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(self.model_frame, font=('Verdana', 9))
            entry.insert(0, str(defaults[key]))
            entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            self.entries[key] = entry

        row_index = len(labels)

        self.label_call_result = tk.Label(self.model_frame, text="Price of call: ", font=size_letter)
        self.label_call_result.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.label_put_result = tk.Label(self.model_frame, text="Price of put: ", font=size_letter)
        self.label_put_result.grid(row=row_index + 1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        button_calculate = tk.Button(self.model_frame, text="Calculate", command=self._calculate_price_button)
        button_calculate.grid(row=row_index + 2, column=1, padx=10, pady=10, sticky="e")

        button_back = tk.Button(self.model_frame, text="Back", command=self._show_initial_frame)
        button_back.grid(row=row_index + 2, column=0, padx=10, pady=10, sticky="e")

        try:
            formula_img = Image.open("Black-Scholes.png")
            formula_img = formula_img.resize((339, 220))
            self.formula_photo = ImageTk.PhotoImage(formula_img)
            formula_label = tk.Label(self.model_frame, image=self.formula_photo)
            formula_label.grid(row=0, column=2, rowspan=len(labels) + 2, padx=10, pady=10, sticky="nsew")
        except FileNotFoundError:
            messagebox.showerror("Error", "Formula image file not found!")

        self.model_frame.columnconfigure(1, weight=1)
        self.model_frame.columnconfigure(2, weight=1)

    def _calculate_price_button(self):
        """Calculation button command"""
        try:
            black_scholes_obj = BlackScholes(spot=float(self.entries["S"].get()),
                                             strike=float(self.entries["K"].get()),
                                             maturity=float(self.entries["T"].get()),
                                             risk_free=float(self.entries["r"].get()),
                                             sigma=float(self.entries["sigma"].get()))
            self.label_call_result.config(text=f"Price of call: {black_scholes_obj.calculate_call():.2f}")
            self.label_put_result.config(text=f"Price of put: {black_scholes_obj.calculate_put():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter numerical values !")

    def _show_initial_frame(self):
        """Function to go back to the main menu"""
        self.model_frame.pack_forget()
        self.initial_frame.pack(fill='both', expand=True)


