import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)
print(avg)

more_avg = list(filter(lambda x: x > avg, data))
print(more_avg)

less_avg = list(filter(lambda x: x < avg, data))
print(less_avg)

countries = ['', 'Argentina', '', 'Brazil', 'Chile', '',
             'Colombia', '', 'Ecuador', '', '', 'Venezuela']

new_countries1 = list(filter(lambda x: x != '', countries))
new_countries2 = list(filter(None, countries))
print(new_countries1)
print(new_countries2)
