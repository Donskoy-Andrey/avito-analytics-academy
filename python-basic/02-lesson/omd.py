from random import randint


def is_rain() -> bool:
    if randint(1, 10) <= 5:
        return True
    return False


def step2_umbrella() -> None:
    if is_rain():
        print("Вы спаслись от дождя и благополучно добрались в бар! 🥳")
    else:
        print("Дождя не было. Вы благополучно добрались в бар! 🤩")


def step2_no_umbrella() -> None:
    if is_rain():
        print("Вы промокли. Вечер испорчен. 🥲")
    else:
        print("Дождя не было. Вы благополучно добрались в бар! 🤩")


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. Взять ей зонтик? ☂️")
    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    step1()
