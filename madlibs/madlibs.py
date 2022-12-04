from Sample_Madlibs import hp, code, zombies , hungergames
import random

if __name__ == '__main__':
 m = random.choice([hp,code,zombies,hungergames])
 m.madlib()