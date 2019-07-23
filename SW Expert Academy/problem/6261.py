beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
beer_after = {k: v*(1.05) for k,v in beer.items()}
print(beer)
print(beer_after)