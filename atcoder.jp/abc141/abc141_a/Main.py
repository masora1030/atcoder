s = input()
weather = ['Sunny', 'Cloudy', 'Rainy']
for i,tmp in enumerate(weather):
    if s == tmp:
        print(weather[i-2])