class nuntakonEngineer:
    '''
    test = nuntakonEngineer()
    test.art()
    '''
    def __init__(self):
        self.name = 'nuntakon Engineer'

    def art(self):
        asciiart = '''
 _____________________       
|  _________________  |
| | JO**nuntakon 0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
        