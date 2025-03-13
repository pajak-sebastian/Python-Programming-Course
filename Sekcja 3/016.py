capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

capitalReturn = capital * rateOfInterest
print("Zwrot inwestycji: ",capitalReturn)

capitalInflation = capital * inflationRate
print("Spadek wartości z uwagi na inflację: ", capitalInflation)

capitalFinal = capital + capitalReturn - capitalInflation
print("Ostateczny kapitał: ", capitalFinal)
