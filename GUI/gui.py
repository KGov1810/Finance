import tkinter as tk


class GUI:

    def __init__(self):
        None

    def _select_model(self, model_name: str):
        """Select the model you want"""
        model_window = tk.Tk()
        model_window.title(f"{model_name} Model")
        model_window.minsize(400, 300)

        if model_name == "Black-Scholes":
            self._create_black_scholes_window(window=model_window)
        else:
            label = tk.Label(model_window, text="NOT IMPLEMENTED !")
            label.grid(row=0, column=0, padx=10, pady=4)

    def create_principal_window(self):
        """Create the principal window"""
        principal_window = tk.Tk()
        principal_window.title("Select your model")
        principal_window.minsize(300,200)

        button_bs = tk.Button(principal_window, text="Black Scholes Model", command=lambda: self._select_model("Black-Scholes"))
        button_bs.pack(padx=20, pady=10)

        button_binomial = tk.Button(principal_window, text="Test Model", command=lambda: self._select_model("Binomial"))
        button_binomial.pack(padx=20, pady=10)

        return principal_window.mainloop()

    def _create_black_scholes_window(self, window: tk.Tk):
        """Create specific window for the black-scholes model"""

        # Parameters to calculate the black_scholes model
        labels = ["Actual price of the underlying (S):", "Strike Price (K):", "Maturity (T):",
                  "Risk Free Rate (r):", "Volatility (sigma):"]
        entries = [tk.Entry(window) for _ in labels]

        for i, (label_text, entry) in enumerate(zip(labels, entries)):
            label = tk.Label(window, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

        entry_S, entry_K, entry_T, entry_r, entry_sigma = entries

        # Button to calculate the price
        button_calculate = tk.Button(window, text="Calculate price",)
        button_calculate.grid(row=5, columnspan=2, pady=10)

        # Display prices
        label_call_result = tk.Label(window, text="Price of call: ")
        label_call_result.grid(row=6, columnspan=2, pady=5)

        label_put_result = tk.Label(window, text="Price of put: ")
        label_put_result.grid(row=7, columnspan=2, pady=5)

        # Responsive behavior
        window.grid_columnconfigure(0, weight=1)
        window.grid_columnconfigure(1, weight=1)

