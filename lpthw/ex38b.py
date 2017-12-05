# create a string called ten_things
ten_things = "Gas Electricity Rent CTax WaterRates Insurance CarTax PhoneBill Maintenance Shopping"

# split it and return the result to a list called 'stuff'
upperstuff = ten_things.upper()
stuff = upperstuff.split(' ')

for item in range(len(stuff)):
    print(stuff[item])