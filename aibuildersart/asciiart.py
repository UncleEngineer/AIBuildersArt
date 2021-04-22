class Hana_Harper:
    '''
    test = Hana_Harper()
    test.art()
    '''
    def __init__(self):
        self.name = 'Hana_Harper'

    def art(self):
        asciiart = '''

   |\---/|
   | ,_, |
    \_`_/-..----.
 ___/ `   ' ,""+ \  sk          Hana & Harper
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
---------------------------------                                                                                                                                                                                                                
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
