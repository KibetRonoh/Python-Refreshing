friends = ['Rolf', 'Bob', 'Jen']
time_since_seen = [3, 7, 90]

long_timers_dict = dict(zip(friends, time_since_seen))
long_timers_list = list(zip(friends, time_since_seen))

print(long_timers_list)
print(long_timers_dict)