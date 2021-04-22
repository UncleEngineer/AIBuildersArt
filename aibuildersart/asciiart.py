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
    |  .-. .- |           
    |  \o| |o (           
    \     ^    \          
     '.  )--'  /          
      '-...-'`      
  -------------------        
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
