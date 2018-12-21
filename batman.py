import re

text_1 = "Batman and Tina Fey."
text_2 = "Tina Fey and Batman."

hero_regex = re.compile(r"Batman|Tina Fey")
mo_1 = hero_regex.search(text_1)
mo_2 = hero_regex.search(text_2)

print(mo_1.group())
print(mo_2.group())

print()

text_3 = "Batmobile loose a ball. Batman found all."
bat_regax = re.compile(r"Bat(man|mobile|copter|bat)")
mo_3 = bat_regax.search(text_3)

print(mo_3.group())
print(mo_3.group(1))




# ----------------
input("\nDone!..")