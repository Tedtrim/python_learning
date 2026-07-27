import csv

with open('sample.csv') as f:
    reader = csv.DictReader(f)
    transactions = [float(row['amount']) for row in reader]

net_total = sum(transactions)
print(net_total)
