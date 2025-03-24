try:
    valr = 1 / 0
except Exception as e:
    print(e.__class__.__name__)
    valr = 1
print(valr)
