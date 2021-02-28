﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Стас', color="#c8ffc8", image = "stas")
define d = Character('Дима', color="#c8ffc8", image = "dimas")
define gp = Character('Гопник', color="#c8ffc8", image = "gopnik")
define v = Character('Валера', color="#c8ffc8", image = "valera")
define st = Character('Сторож', color="#c8ffc8", image = "storozh")
define m = Character('Мама', color="#c8ffc8", image = "mama")

define var1 = False
define var2 = False
define var3 = False
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    """
    Утро. 

    Прохладная комната, и такая теплая постель. 

    Единственное, что нарушает эту прекрасную атмосферу – будильник. 

    С каждой секундной он начинает еще больше раздражать, ведь звенит он не просто так. 

    Сегодня среда. Отличный день недели, но только не сегодня. 

    Сегодня по Геометрии будут проводить контрольную. 

    Я бы не сказал, что я ничего не понимаю в геометрии и в других предметах, но обычно мои результаты на контрольных не очень высоки, сколько ты ни старайся. 

    Да и Стас вчера совсем был не в духе, всё приговаривал что по контрольной нихрена не подготовился, и что он просто напросто не появлялся бы, если бы было с кем. 

    Зная Стаса, его жалобы можно перевести как вопрос: “Поддержишь ли ты меня в эту трудную минуту?”. 

    Поэтому мной и моим другом Стасяном было решено прогулять сегодня школу. Я крайне редко прогуливаю. 

    В последний раз такое было несколько лет назад, и то случайно. Однако сегодня все иначе. 

    Решение было принято практически сразу. Поэтому… я хорошенько подготовился к предстоящей операции вчера вечером.

    Привычными действиями я собрал сумку и направился к выходу. 

    Обычно мой будильник установлен на самое крайнее время, поэтому мне нужно поторопиться, чтобы не вызвать лишнего подозрения со стороны родных.

    Проверив карманы на наличие денег я выдвигаюсь на улицу. 

    Скорее всего меня уже заждался товарищ по сегодняшним приключениям. Я бы удивился, не окажись его раньше обычного.
    """
    jump utro
    return

label utro:

    scene bg garage
    with fade
    show stas norm

    "Как я и думал, Стасян на месте. Его можно узнать сразу по его любимой спортивной куртке, которую он одевает всегда."

    "Даже в школу, где необходимо быть в костюме." 

    "Все учителя постоянно делают замечания насчет этого, но он лишь отмахивается, говоря, что куртка – часть костюма… {w}спортивного{w}, а значит считается."

    "Так, конечно, думает только он, однако все довольно быстро устают спорить и пропускают его так."

    s angry "Димон, ты долго там стоять будешь, пошли уже!"

    d norm "Да ладно тебе, торопиться нам некуда, у нас весь день впереди."

    s happy "Ну да, ты прав. Я как-то об этом не подумал"

    d smile "Хех, ну ты даешь.{w} Ладно, куда двинем?"

    s smushenie "Я без понятия. Прогуливаю постоянно, но обычно делаю это дома. У тебя есть идеи?"

    d wat "А сегодня к тебе не завалимся?"

    s smushenie "Не, у меня все дома." 
    extend angry" Еле как вырвался сюда через тонны ругани и фраз о том, какой я никудышный сынок, раз приношу только двойки и тройки…"

    d norm "Да уж, звучит вообще невкусно…"
    extend think " Ладно, давай тогда пойдем… {w}чёрт, и куда ж бы сходить… {w}мест вроде много, да везде уже бывали не раз."

    s proud "Ну смотри{w}, мы можем на компы сходить,"
    extend happy " наконец-то постреляемся сколько влезет."
    extend norm " Ну или если компы достали, пройдём вон по тем дворам, как раз по дороге подумаем, чем бы ещё заняться."
    s proud "И… {w}чё ещё… {w}ну, можем в магазин за сухариками сходить…"

    d smile "Слушай, а неплохо. Давай пойдем…"
    jump choise

    return

label choise:
    scene bg school
    if (var1==False and var2==False and var3==False):
        menu:
            "Куда пойдем?"

            "Прогуляемся по дворам":
                $var1 = True
                jump garage

            "Пойдем на компы":
                $var2 = True
                jump kompiki

            "Пошли ко мне":
                $var3 = True
                jump hata
    if (var1==True and var2==False and var3==False):
        menu:
            "Куда пойдем?"

            "Пойдем на компы":
                $var2 = True
                jump kompiki

            "Пошли ко мне":
                $var3 = True
                jump hata
    if (var1==True and var2==True and var3==False):
        menu:
            "Куда пойдем?"

            "Пошли ко мне":
                $var3 = True
                jump hata
    if (var1==True and var2==True and var3==True):
        menu:
            "Куда пойдем?"

            "Ладно, давай уже расходиться":
                jump final

    return

label garage:
    scene bg dvor
    "гараге"
    jump choise
    return

label kompiki:
    scene bg dvor
    "компы"
    jump choise

    return

label hata:
    scene bg dvor
    "хата"
    jump choise
    return

label final:
    "красава!"
    return

label epilog1:

    return

label epilog2:

    return