list_stocks = ["INFY", "HDFC", "ABFRL"]

for count, ticker in enumerate(list_stocks):
    print(count, ticker)

list_stocks = [["INFY", "HDFC", "ABFRL"], 23]
print("Multi dimensional")
for count, ticker in enumerate(list_stocks):
    print(count, ticker)