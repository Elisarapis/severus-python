import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
import math

maturity_date = ql.Date(29, 5, 2020)
spot_price = 125
strike_price = 130
volatility = 0.20
dividend_rate = 0.0163
option_type = ql.Option.Call

risk_free_rate = 0.0001
day_count = ql.Actual365Fixed()
calendar = ql.Italy()

calculation_date = ql.Date(24, 4, 2020)
ql.Settings.instance().evaluationDate = calculation_date

payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(maturity_date)
