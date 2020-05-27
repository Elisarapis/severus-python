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
european_option = ql.VanillaOption(payoff, exercise)

v0 = volatility*volatility
kappa = 0.1
theta = v0
sigma = 0.1
rho = -0.75

spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, risk_free_rate, day_count))
dividend_yield = ql.YieldTermStructureHandle(ql.FlatForward(calculation_date, dividend_rate, day_count))
heston_process = ql.HestonProcess(flat_ts, dividend_yield, spot_handle, v0, kappa, theta, sigma, rho)
engine = ql.AnalyticHestonEngine(ql.HestonModel(heston_process))
european_option.setPricingEngine(engine)
h_price = european_option.NPV()
print(h_price)

flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(calculation_date, calendar, volatility, day_count))
bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_yield, flat_ts, flat_vol_ts)
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()
print(bs_price)
