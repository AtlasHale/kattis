cards = list(input())
card_count = {'T': 0, 'C': 0, 'G':0}

for x in cards:
    card_count[x]+=1
sets_of_cards = min(card_count['T'], card_count['C'], card_count['G'])
print (card_count['T']**2+card_count['C']**2+card_count['G']**2+7*sets_of_cards)
