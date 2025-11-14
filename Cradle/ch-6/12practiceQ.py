#WAF to calculate USD-INR
# def usd_inr(a, b=83):
#     # a = 80
#     print("inr:", a*b)

# usd_inr(100)
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)