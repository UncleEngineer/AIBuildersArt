class DekDork:
    '''
    test = UncleEngineer()
    test.art()
    '''
    def __init__(self):
        self.name = 'Dek ear dek dee'

    def art(self):
        asciiart = '''
      .-""""-.
     / -   -  \           Dek
    |  .-. .- |           D
    |  \o| |o (           O
    \     ^    \          R
     '.  )--'  /          K
      '-...-'`      
  -------------------        
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
