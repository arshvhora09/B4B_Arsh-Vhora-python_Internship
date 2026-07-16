prices = [120, 250, 180, 300, 90, 450, 210, 160, 500, 275]

average = sum(prices) / len(prices)

above_average = [price for price in prices if price > average]

print("Average Price:", average)
print("Prices Above Average:", above_average)