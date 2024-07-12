import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

from Configurations.config_gui import CONFIG_GUI
from GUI.model_gui import ModelGUI
from Models.black_scholes import BlackScholes


class BlackScholesGUI(ModelGUI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.principal_window = kwargs.get("principal_window")
        self.initial_frame = kwargs.get("initial_frame")
        self.formula_photo = None

    def create_model_window(self):
        """Create the window of the black-scholes model"""
        super().create_model_window()
        for i, (key, label_text) in enumerate(CONFIG_GUI.LABELS_PRICING.items()):
            label = tk.Label(self.model_frame, text=label_text, font=self.size_letter)
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(self.model_frame, font=('Verdana', 9))
            entry.insert(0, str(CONFIG_GUI.DEFAULTS_PRICING[key]))
            entry.grid(row=i, column=1, padx=10, pady=10, sticky="w")
            self.entries[key] = entry

        row_index = len(CONFIG_GUI.LABELS_PRICING)

        self.label_call_result = tk.Label(self.model_frame, text="Price of call: ", font=self.size_letter)
        self.label_call_result.grid(row=row_index, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.label_put_result = tk.Label(self.model_frame, text="Price of put: ", font=self.size_letter)
        self.label_put_result.grid(row=row_index + 1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        button_calculate = tk.Button(self.model_frame, text="Calculate", command=self._calculate_price_button)
        button_calculate.grid(row=row_index + 2, column=1, padx=10, pady=10, sticky="e")

        button_back = tk.Button(self.model_frame, text="Back", command=self.show_initial_frame)
        button_back.grid(row=row_index + 2, column=0, padx=10, pady=10, sticky="e")

        formula_img = Image.open("Black-Scholes.png")
        formula_img = formula_img.resize((339, 220))
        self.formula_photo = ImageTk.PhotoImage(formula_img)
        formula_label = tk.Label(self.model_frame, image=self.formula_photo)
        formula_label.grid(row=0, column=5, rowspan=len(CONFIG_GUI.LABELS_PRICING) + 2, padx=10, pady=10, sticky="nsew")

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
