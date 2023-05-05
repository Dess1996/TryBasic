import re

cardValuesInf = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}

cardValues = '6S 10S'  # 6S 10S AH JH
trump = 'S'

value = re.findall('A|K|Q|J|[0-9]+', cardValues)
colors = re.findall('[CDHS]', cardValues)

# Перевод в веса
weight1 = cardValuesInf.get(value[0])
weight2 = cardValuesInf.get(value[1])

if len(colors) == 2:
    if trump in colors:
        if trump == colors[1] and trump != colors[0]:
            print('Second')
        elif trump != colors[1] and trump == colors[0]:
            print('First')
        elif weight1>weight2:
            print('First')
        else:
            print('Second')
    elif colors[0] != colors[1]:
        print('Error')
    else:
        if weight1 > weight2:
            print('First')
        else:
            print('Second')
