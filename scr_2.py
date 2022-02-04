from sys import argv

script_name, work_hours, money_per_hour, bonus = argv

print(float(work_hours) * float(money_per_hour) + float(bonus))

