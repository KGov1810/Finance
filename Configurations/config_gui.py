class CONFIG_GUI:
    LABELS_PRICING = {"S": "Spot price (S):",
                      "K": "Strike Price (K):",
                      "T": "Maturity (T):",
                      "r": "Risk Free Rate (r):",
                      "sigma": "Volatility (sigma):"}

    DEFAULTS_PRICING = {"S": 100,
                        "K": 100,
                        "T": 1,
                        "r": 0.05,
                        "sigma": 0.2}

    LABELS_LIVE = {"symbol": "Stock symbols",
                   "maturity": "Maturity (YYYY-MM-DD)"}

    DEFAULTS_LIVE = {"symbol": "AAPL",
                     "maturity": "2025-12-31"}
