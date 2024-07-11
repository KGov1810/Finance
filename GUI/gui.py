import tkinter as tk

from Models.black_scholes import BlackScholes


class GUI:

    def __init__(self):
        None

    def _select_model(self, model_name: str, old_window: tk.Tk):
        """Select the model you want"""
        old_window.destroy()
        model_window = tk.Tk()
        model_window.title(f"{model_name} Model")
        model_window.minsize(400, 300)

        if model_name == "Black-Scholes":
            self._create_black_scholes_window(model_window)
        else:
            label = tk.Label(model_window, text="NOT IMPLEMENTED !")
            label.grid(row=0, column=0, padx=10, pady=4)

    def create_principal_window(self):
        """Create the principal window"""
        principal_window = tk.Tk()
        principal_window.title("Select your model")
        principal_window.minsize(300, 200)

        button_bs = tk.Button(principal_window, text="Black Scholes Model", command=lambda: self._select_model("Black-Scholes", old_window=principal_window))
        button_bs.pack(padx=20, pady=10)

        button_binomial = tk.Button(principal_window, text="Test Model", command=lambda: self._select_model("Binomial"))
        button_binomial.pack(padx=20, pady=10)

        return principal_window.mainloop()

    def _create_black_scholes_window(self, window: tk.Tk):
        """Create specific window for the black-scholes model"""

        # Parameters to calculate the black_scholes model
        labels = ["Actual price of the underlying (S):", "Strike Price (K):", "Maturity (T):",
                  "Risk Free Rate (r):", "Volatility (sigma):"]
        defaults = [100, 100, 1, 0.05, 0.2]
        entries = []

        for i, (label_text, default_value) in enumerate(zip(labels, defaults)):
            label = tk.Label(window, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(window)
            entry.insert(0, str(default_value))
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            entries.append(float(entry.get()))

        entry_S, entry_K, entry_T, entry_r, entry_sigma = entries

        black_scholes_obj = BlackScholes(strike=entry_K,
                                         spot=entry_S,
                                         maturity=entry_T,
                                         risk_free=entry_r,
                                         sigma=entry_sigma)

        # Button to calculate the price
        button_calculate = tk.Button(window, text="Calculate price", command=black_scholes_obj.calculate_call_and_put())
        button_calculate.grid(row=5, columnspan=2, pady=10)

        # Display prices
        label_call_result = tk.Label(window, text="Price of call: ")
        label_call_result.grid(row=6, columnspan=2, pady=5)

        label_put_result = tk.Label(window, text="Price of put: ")
        label_put_result.grid(row=7, columnspan=2, pady=5)

        label_call_result.config(text=f"Price of call: {black_scholes_obj.calculate_call():.2f}")
        label_put_result.config(text=f"Price of put: {black_scholes_obj.calculate_put():.2f}")

        # Responsive behavior
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)
