import random

def daniel(world):
    emojis = "¯\_(ツ)_/¯", " ´• ل •`"," (◉ω◉)", "(｡>﹏<｡)" , "-ㅅ-","¯\(°_o)/¯"
    generador = ""

    for i in range(world):
        generador += random.choice(emojis)

    return generador


