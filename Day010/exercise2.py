def e_ano_bissexto(ano):
    bissexto = False

    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                bissexto = True
        else:
            bissexto = True
    return bissexto

print(e_ano_bissexto(1700))

