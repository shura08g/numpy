gender = {
    'm': "Дорогой",
    'f': "Дорогая"
}

people = [
    ["Семен", "Семенович", 32.56, 'm'],
    ["Тамара", "Ивановна", 13.12, 'f'],
    ["Михаил", "Анатольевич", 238.12, 'm']
]

for name, midlname, balance, g in people:
    text = f"""\t{gender.get(g)} {name} {midlname},
баланс Вашего лицевого счета составляет: {balance}$"""
    print(text)
