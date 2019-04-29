#HW03_03
name = ['Selena Gomez', 'Cristiano Ronaldo','Ariana Grande', 'Kim Kardashian', 'Beyonce Giselle Knowles', 'Taylor Swift', 'Kylie Jenner', 'Dwayne Johnson', 'Justin Bieber', 'Neymar da Silva SantosJunior']

for i in sorted(name, key=lambda x: x.split(" ")[-1], reverse=False):
    print(i)