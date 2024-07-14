import tkinter as tk

from GUI.black_scholes_gui import BlackScholesGUI


class GUI:

    def __init__(self, **kwargs):
        self.principal_window = kwargs.get("main_window")

        self.initial_frame = None
        self.model_frame = None

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

    def _select_model(self, model_name: str):
        """
        Select the model you want
        Args:
            model_name: Name of the model to use
        """
        self.initial_frame.pack_forget()

        if model_name == "Black-Scholes":
            bs_window_obj = BlackScholesGUI(principal_window=self.principal_window,
                                            initial_frame=self.initial_frame)
            bs_window_obj.create_model_window()
        elif model_name == "Binomial":
            self.model_frame = tk.Frame(self.principal_window)
            self.model_frame.pack(fill='both', expand=True)
