#HW02_1
monster_list = ['地精','狼人','熊貓人']
attack_list = [80,90,20]
defense_list = [70,92,75]

monster = dict(zip(monster_list, zip(attack_list,defense_list)))
print(monster)
