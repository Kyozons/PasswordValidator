import wizzcoin

purse = wizzcoin.WizCoin(2, 5, 99)  # The ints are passed to __init__().
print(purse)
print('G: ', purse.galleons, 'S: ', purse.sickles, 'K: ', purse.knuts)
print('Total Value: ', purse.value())
print('Weight: ', purse.weight_in_grams(), 'grams')

print()

coin_jar = wizzcoin.WizCoin(13, 0, 0)
print(coin_jar)
print('G: ', coin_jar.galleons, 'S: ', coin_jar.sickles, 'K: ', coin_jar.knuts)
print('Weight: ', coin_jar.weight_in_grams(), 'grams')
