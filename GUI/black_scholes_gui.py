import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

from yahooquery import Ticker

from Configurations.config_gui import CONFIG_GUI
from GUI.model_gui import ModelGUI
from Models.black_scholes import BlackScholes


class BlackScholesGUI(ModelGUI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.principal_window = kwargs.get("principal_window")
        self.initial_frame = kwargs.get("initial_frame")
        self.formula_bs_image = None

    def create_model_window(self):
        """Create the window of the black-scholes model"""
        super().create_model_window()
        self._create_basic_bs_calc()
        self._create_live_bs_calc()

    def _create_basic_bs_calc(self):
        """Function to calculate a basique Black-Scholes according to the variables given by the user"""
        for i, (key, label_text) in enumerate(CONFIG_GUI.LABELS_PRICING.items()):
            self.create_label(row=i, column=0, sticky="e", text=label_text)
            entry = self.create_entry(default_value=str(CONFIG_GUI.DEFAULTS_PRICING[key]), row=i, column=1, sticky="w")
            self.entries[key] = entry

        self.row_index_basic_bs = len(CONFIG_GUI.LABELS_PRICING)

        self.label_call_result = self.create_label(text="Price of call: ", row=self.row_index_basic_bs,
                                                   column=0, sticky="e")
        self.label_put_result = self.create_label(text="Price of put: ", row=self.row_index_basic_bs + 1,
                                                  column=0, sticky="e")
        self.button_calculate = self.create_button(text="Calculate Call/Put", command=self._calculate_cp_button,
                                                   row=self.row_index_basic_bs + 2, column=1, sticky="w")
        self.button_back = self.create_button(text="Back", command=self.show_initial_frame,
                                              row=self.row_index_basic_bs + 2, column=0, sticky="e")
        self.formula_bs_image = self.display_image(image_link="Black-Scholes.png", size_x=339, size_y=220)
        self.formula_bs_label = self.create_label(image=self.formula_bs_image, row=0, column=5,
                                                  rowspan=len(CONFIG_GUI.LABELS_PRICING) + 2, sticky="nsew")

        self.model_frame.columnconfigure("1 2", weight=1)

    def _calculate_cp_button(self):
        """Calculation button command"""
        try:
            black_scholes_obj = BlackScholes(spot=float(self.entries["S"].get()),
                                             strike=float(self.entries["K"].get()),
                                             maturity=float(self.entries["T"].get()),
                                             risk_free=float(self.entries["r"].get()),
                                             sigma=float(self.entries["sigma"].get()))
            self.create_label(text=f"{black_scholes_obj.calculate_call():.2f}", row=self.row_index_basic_bs,
                              column=1, sticky="w")
            self.create_label(text=f"{black_scholes_obj.calculate_put():.2f}", row=self.row_index_basic_bs + 1,
                              column=1, sticky="w")
        except ValueError:
            messagebox.showerror("Error", "Please enter numerical values !")

    def _create_live_bs_calc(self):
        """Function to calculate a live black-scholes according to an underlying given by the user"""
        for i, (key, label_text) in enumerate(CONFIG_GUI.LABELS_LIVE.items()):
            self.create_label(row=i, column=3, sticky="w", text=label_text)
            entry = self.create_entry(default_value=str(CONFIG_GUI.DEFAULTS_LIVE[key]), row=i, column=4, sticky="w")
            self.entries[key] = entry

        self.row_index_live_bs = len(CONFIG_GUI.LABELS_LIVE)

        self.label_spot_result = self.create_label(text="Spot price: ", row=self.row_index_live_bs, column=3, sticky="w")
        self.button_get_spot = self.create_button(text="Get Spot Price", command=self._get_spot_price,
                                                  row=self.row_index_live_bs + 1, column=4, sticky="w")
        self.label_callput = self.create_label(text="Call/Put: ", row=self.row_index_live_bs + 2, column=3, sticky="w")
        self.callput_result = self.create_combobox(values=["Call", "Put"], row=self.row_index_live_bs + 2,
                                                   column=4, sticky="w", default_value="Call")
        self.label_maturity = self.create_label(text="Maturity: ", row=self.row_index_live_bs + 3, column=3, sticky="w")
        self.maturity_result = self.create_combobox(values=[], row=self.row_index_live_bs + 3, column=4, sticky="w")
        self.button_get_maturity = self.create_button(text="Get Live Maturity",
                                                      command=self._get_option_maturity,
                                                      row=self.row_index_live_bs + 4, column=4, sticky="w")
        self.label_strike = self.create_label(text="Strike: ", row=self.row_index_live_bs + 5, column=3, sticky="w")
        self.strike_result = self.create_combobox(values=[], row=self.row_index_live_bs + 5, column=4, sticky="w")
        self.button_get_strike = self.create_button(text="Get Live Strike",
                                                    command=self._get_option_strike,
                                                    row=self.row_index_live_bs + 6, column=4, sticky="w")
        self.label_option_result = self.create_label(text="Option prices: ", row=self.row_index_live_bs + 7,
                                                     column=3, sticky="w")
        self.button_get_option_price = self.create_button(text="Get Price of Option",
                                                          command=self._get_option_prices,
                                                          row=self.row_index_live_bs + 8, column=4, sticky="w")

    def _get_spot_price(self):
        """Get spot price of an underlying specified by the user"""
        symbol = self.entries["symbol"].get()
        if symbol != "":
            spot_data, currency = self._get_spot_data(symbol)
            if spot_data is not None and currency is not None:
                self.label_spot_result.config(text=f"Spot price {symbol}:")
                self.create_label(text=f"{spot_data} {currency}", row=self.row_index_live_bs, column=4, sticky="w")
        else:
            messagebox.showerror("Error", "Please enter a symbol!")

    def _get_spot_data(self, symbol: str):
        """
        Fetch the spot price from Yahoo Finance using yahooquery
        Args:
            symbol: Symbol of the underlying to query
        Return:
            spot: Spot price of the underlying
            currency: Currency type of the underlying
        """
        stock = Ticker(symbol)
        stock_data = stock.financial_data
        if "currentPrice" not in stock_data[symbol]:
            self.label_spot_result.config(text=f"Spot price:")
            messagebox.showerror("Error", "Please enter a valid symbol!")
            return None, None
        else:
            spot = stock_data[symbol]["currentPrice"]
            currency = stock_data[symbol]["financialCurrency"]
        return spot, currency

    def _get_option_maturity(self):
        """Fetch option maturity from Yahoo Finance using yahooquery"""
        symbol = self.entries["symbol"].get()
        if symbol != "":
            stock = Ticker(self.entries["symbol"].get())
            options = stock.option_chain.reset_index()
            options = options.loc[options["optionType"] == ("calls" if self.callput_result.get() == "Call" else "puts")]
            options["expiration"] = options["expiration"].astype(str)
            maturity = options["expiration"].drop_duplicates().tolist()
            self.maturity_result["values"] = maturity
            self.maturity_result.set(maturity[0])
        else:
            messagebox.showerror("Error", "Please enter a symbol!")

    def _get_option_strike(self):
        """Fetch option strike from Yahoo Finance using yahooquery"""
        symbol = self.entries["symbol"].get()
        maturity = self.maturity_result.get()
        if symbol != "" and maturity != "":
            stock = Ticker(self.entries["symbol"].get())
            options = stock.option_chain.reset_index()
            options["expiration"] = options["expiration"].astype(str)
            options = options.loc[(options["optionType"] == ("calls" if self.callput_result.get() == "Call" else "puts"))
                                  & (options["expiration"] == maturity)]
            strike = options["strike"].drop_duplicates().tolist()
            self.strike_result["values"] = strike
            self.strike_result.set(strike[0])
        else:
            messagebox.showerror("Error", "Please enter a symbol or press the button Get Live Maturity !")

    def _get_option_prices(self):
        """Fetch option prices according to the strike, the maturity, call/put and the underlying"""
        symbol = self.entries["symbol"].get()
        maturity = self.maturity_result.get()
        try:
            strike = float(self.strike_result.get())
            if symbol != "" and maturity != "":
                stock = Ticker(self.entries["symbol"].get())
                options = stock.option_chain.reset_index()
                options["expiration"] = options["expiration"].astype(str)
                options = options.loc[
                    (options["optionType"] == ("calls" if self.callput_result.get() == "Call" else "puts"))
                    & (options["expiration"] == maturity) & (options["strike"] == strike)]
                bid_value = options["bid"].values[0]
                ask_value = options["ask"].values[0]
                volatility = options["impliedVolatility"].values[0]
                self.create_label(text=f"Bid : {bid_value}\n"
                                       f"Ask: {ask_value}\n"
                                       f"Implied Volatility: {volatility}",
                                  row=self.row_index_live_bs + 7, column=4, sticky="w")
            else:
                messagebox.showerror("Error", "Please fill the maturity, strike and symbol "
                                              "by pressing the buttons!")
        except ValueError:
            messagebox.showerror("Error", "Please press the button Get Live Strike !")
