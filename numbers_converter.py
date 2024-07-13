'''
Jus Mundi Coding Task
author: @rafaelmm82
author name: Rafael Magalhaes

Observation: Description, reasoning, constraints, improvements and solution are described in the README.md file
'''

# Dictionary with numbers between 0 and 20
UNITES =  {'0': '',
           '1': 'un',
           '2': 'deux',
           '3': 'trois',
           '4': 'quatre',
           '5': 'cinq',
           '6': 'six',
           '7': 'sept',
           '8': 'huit',
           '9': 'neuf',
           '10': 'dix',
           '11': 'onze',
           '12': 'douze',
           '13': 'treize',
           '14': 'quatorze',
           '15': 'quinze',
           '16': 'seize',
           '17': 'dix-sept',
           '18': 'dix-huit',
           '19': 'dix-neuf',
           '20': 'vingt'}

# Dictionary with dizaine names
DIZAINES = {'2': 'vingt',
            '3': 'trente',
            '4': 'quarante',
            '5': 'cinquante',
            '6': 'soixante',
            '7': 'soixante-dix',
            '8': 'quatre-vingt',
            '9': 'quatre-vingt-dix'}


# Function that returns the french name for a given number
def number_name(num: int) -> str: 
    """
    Converts a given number into its French cardinal name,
    Exception raises if the number is out of range (1, 999999).

    Args:
        num (int): The number to be converted.

    Returns:
        str: The French name representation.
    """

    # constrain about maximum number and negative ones
    if num < 0 or num > 999999:
        raise Exception('The given number is out of range')
    
    s_num = str(num)    # string version
    l_num = len(s_num)  # number length


    # There are five cases in solution construction
    # ---------------------------------------------

    # 1) number is zero
    if num == 0:
        num_name = 'zéro'


    # 2) MILLE: number is bigger than mille.
    elif l_num > 3:

        num_m = int(s_num[:-3])  # int from mille part
        num_c = int(s_num[-3:])  # int from centaine part

        # specific Jus Mundi Kata Struction to dealing with plurals on 'thousands' position (a divergence is discussed in README.md file)
        if s_num[-3:] == '000':
            if s_num[:-3] == '1':
                num_name = 'mille'
            else:
                num_name = number_name(num_m)
                if num_name.endswith('cents',) or num_name.endswith('vingts'):
                    num_name = num_name[:-1] + '-milles'
                else:
                    num_name += '-milles'
        # general case considering the wikipedia rule (given reference)
        else:
            if s_num[:-3] == '1':
                num_name = 'mille-' + number_name(num_c)
            else:
                num_name =  number_name(num_m) + '-mille-' + number_name(num_c)


    # 3) CENTAINE: number is on centaine base
    elif l_num > 2:

        c, d, u = s_num    # decomposition of centaine, dizaine and unite
        num_du = int(d+u)  # int from dizaine and unite

        if c == '0':
            num_name = 'et-' + number_name(num_du)

        elif c == '1':  # spacial case cent
            num_name = 'cent' if d+u == '00' else 'cent-' + number_name(num_du)

        else:
            num_name = UNITES[c] + '-cents' if d+u == '00' else UNITES[c] + '-cent-' + number_name(num_du)


    # 4) DIZAINE: number is on dizaine base
    elif l_num > 1:
        d, u = s_num

        if str(int(d+u)) in UNITES:
            num_name = UNITES[d+u]

        elif d+u == '71':
            num_name = 'soixante-et-onze'

        elif d+u == '80':
            num_name = 'quatre-vingts'

        elif d+u == '81':
            num_name = 'quatre-vingt-un'
        
        elif d == '7' or d == '9':
            num_name = DIZAINES[str(int(d)-1)] + '-' + UNITES[str(int(u)+10)]

        else:
            if u == '1':
                num_name = DIZAINES[d] + '-et-un'
            else:
                num_name = DIZAINES[d] + '-' + UNITES[u]


    # 5) UNITES: number is on unite base
    else:
        num_name = UNITES[s_num]
    

    # cleaning the number name
    num_name = num_name.replace('--', '-').strip('-')  # remove double hyphen in 'mille-' cases and 'centaines-' cases

    return num_name
        
# the function to be used on vertion list of numbers
def numbers_converter(numbers_list: list) -> list:
    """
    Converts a list of numbers into french cardinal names using the number_name function.

    Args:
        numbers (list): The list of numbers to be converted.

    Returns:
        list: The list of French names representation.
    """
    return [number_name(num) for num in numbers_list]


if __name__ == '__main__':
    """
    The main function of the code. It allows the user to input a number between 0 and 999999 and get its French name representation.
    If no number is provided, it generates a random list of numbers and prints their French names.
    """

    # import for this trial
    from random import randint
    from pprint import pprint
    
    number = input('Enter a number between 0 and 999999 to get it written, or <enter> to random trial: ')

    if number:
        try:
            print(number_name(int(number)))
        except Exception as e:
            print(e)
    else:
        numbers = [randint(0, 999999) for i in range(5)]
        pprint(list(zip(numbers, numbers_converter(numbers))))
