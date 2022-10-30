import re

dict_num = {'um': 1,
            'dois': 2,
            'tres': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10,
            'onze': 11,
            'doze': 12,
            'treze': 13,
            'quatorze': 14,
            'catorze': 14,
            'quinze': 15,
            'dezesseis': 16,
            'dezessete': 17,
            'dezoito': 18,
            'dezenove': 19,
            'vinte': 20,
            'trinta': 30,
            'quarenta': 40,
            'cinquenta': 50,
            'sessenta': 60,
            'setenta': 70,
            'oitenta': 80,
            'noventa': 90,
            'cem': 100,
            'cento': 100,
            'duzentos': 200,
            'trezentos': 300,
            'quatrocentos': 400,
            'quinhentos': 500,
            'seiscentos': 600,
            'setecentos': 700,
            'oitocentos': 800,
            'novecentos': 900, }

dict_und = {'mil': 1000,
            'milhao': 1000000,
            'milhoes': 1000000,
            'bilhao': 1000000000,
            'bilhoes': 1000000000,
            'k': 1000,
            'm': 1000000,
            'g': 1000000000}


def standard(text):
    text = text.lower().replace(',', '.')
    text = re.sub(r'[ãâáàä]', 'a', text)
    text = re.sub(r'[ãâáàä]', 'a', text)
    text = re.sub(r'[ẽêéèë]', 'e', text)
    text = re.sub(r'[îiìï]', 'i', text)
    text = re.sub(r'[õôóòö]', 'o', text)

    output = re.findall(r'\S+\d*', text)

    if len(output) == 1:
        try:
            num = re.search(r'[0-9.]+', text).group(0)
            und = re.search(r'[^0-9.]+', text).group(0).rstrip('\n')
            output = [num, und]
        except:
            pass

    return output


def converter(lista):
    soma = 0
    aux = 0

    for pos in range(len(lista)):

        try:
            aux = float(lista[pos])

        except:

            if pos == 0 and lista[pos] == 'mil':
                soma += 1000

            if lista[pos] in dict_num:
                aux += dict_num.get(lista[pos])

            elif lista[pos] in dict_und:

                if lista[pos] == 'mil' or lista[pos] == 'k':
                    aux = aux * dict_und.get(lista[pos])
                    soma += aux
                    aux = 0

                elif lista[pos] == 'milhao' or lista[pos] == 'milhoes' or lista[pos] == 'm':
                    aux = aux * dict_und.get(lista[pos])
                    soma += aux
                    aux = 0

                else:
                    aux = aux * dict_und.get(lista[pos])
                    soma += aux
                    aux = 0

            else:
                continue

    soma += aux

    return f'{soma:.0f}'


def master(path, exit_path):
    with open(exit_path, 'w', encoding='utf-8') as out_file:
        with open(path, 'r', encoding='utf-8') as in_file:
            for line in in_file:
                number = converter(standard(line))
                out_file.write(f'{number}\n')
            in_file.close()
        out_file.close()

    return f'O arquivo {exit_path} foi gravado com SUCESSO'


if __name__ == '__main__':

    url = 'input.txt'
    exit_path = 'output.txt'

    master(url, exit_path)
