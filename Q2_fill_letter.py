name = input("Please enter your name: ")
date = input("Please enter the date: ")

letter =f'''
Dear {name},
You are selected!
{date}'''

print(letter)

#OR

letter = '''
Dear <|name|>,
You are selected!
<|date|>'''

replace = letter.replace("<|name|>", "Meezan").replace("<|date|>", "12/12/2023")
print(replace)