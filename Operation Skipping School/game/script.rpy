# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Стас', color="#c8ffc8", image = "stas")
define d = Character('Дима', color="#c8ffc8", image = "dimas")
define var1 = False
define var2 = False
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg garage

    show stas happy

    s "Здарова"

    s angry "В армию идешь?"

    d blya "Здарова..."

    extend d smile " иду!"

    scene run
    with fade

    "И они пошли в армейку. {w}Там их встретил не самый приятный cumбат{w} и они съебались оттуда..."

    menu:
        "пиздец?"

        "Да":
            $ var1 = True
            jump vario


        "пизда":
            $ var2 = True
            jump vario

    return

label vario:

    "Половая ебля"

    if var1:

        menu:
            "согласны?"

            "Нет":
                jump varii

            "Да":
                jump varii
    
    if var2:

        menu:
            "узнали?"

            "Нет":
                jump varii

            "Да":
                jump varii
    
    return

label varii:
    
    "бля"

    return