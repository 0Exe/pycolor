# Written by github.com/0Exe

def color(color, text):
    colors = {
        
        # text colors
        'grey': '2',
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        
        # background colors
        'bg-gray': '7',
        'bg-black': '40',
        'bg-red': '41',
        'bg-green': '42',
        'bg-yellow': '43',
        'bg-blue': '44',
        'bg-magenta': '45',
        'bg-cyan': '46',
        'bg-white': '47',

        # light background colors
        'l-bg-gray': '100',
        'l-bg-red': '101',
        'l-bg-green': '102',
        'l-bg-yellow': '103',
        'l-bg-blue': '104',
        'l-bg-magenta': '105',
        'l-bg-cyan': '106',
        'l-bg-white': '107',

        # light text colors
        'l-grey': '90',
        'l-red': '91',
        'l-green': '92',
        'l-yellow': '93',
        'l-blue': '94',
        'l-magenta': '95',
        'l-cyan': '96'
    }

    return u"\u001b[" + colors[color] + u"m" + text + u"\u001b[0m"