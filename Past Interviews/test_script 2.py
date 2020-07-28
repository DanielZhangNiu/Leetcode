import random
import math

LEVEL = 3

util_levels = [.18, .32, .46, .6, .74]
names = ["$first", "$second", "$third", "$fourth", "$fifth"]
U = util_levels[LEVEL]
num_sets = 5
num_tasks = 5
T_base = 1000
print(T_base, "\n")

for i in range(num_sets):
    Us = [0 for x in range(num_tasks)]
    Cs = [0 for x in range(num_tasks)]
    Ts = [0 for x in range(num_tasks)]
    for j in range(num_tasks):
        Us[j] = random.random()+.1

    scale = U / sum(Us)
    Us.sort(reverse=True)

for j in range(num_tasks):
    util = Us[j] * scale
    if (U == 1):
        Ts[j] = T_base * random.randrange(1, 5, 1)
        else:
            Ts[j] = random.randrange(1000, 3000, 10)

    Cs[j] = math.floor(Ts[j] * util)
        if (Cs[j] < 10):
            Cs[j] = Cs[j]*5
            Ts[j] = Ts[j]*5
print("#./reserve set %s %d %d -1" % (names[j], Cs[j], Ts[j]))

# print("C ", Cs, "\n");
# print("T ", Ts, "\n");
    print("\n\n")



