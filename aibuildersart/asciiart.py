  
class UncleEngineer:
    '''
    test = UncleEngineer()
    test.art()
    '''
    def __init__(self):
        self.name = 'Uncle Engineer'

    def art(self):
        asciiart = '''
                             Z             
                       Z                   
        .,.,        z           
      (((((())    z             
     ((('_  _`) '               
     ((G   \ |)                 
    (((`   " ,                  
     .((\.:~:          .--------------.    
     __.| `"'.__      | \              |     
  .~~   `---'   ~.    |  .             :     
 /                `   |   `-.__________)     
|             ~       |  :             :   
|                     |  :  |              
|    _                |     |   [ ##   :   
 \    ~~-.            |  ,   oo_______.'   
  `_   ( \) _____/~~~~ `--___              
  | ~`-)  ) `-.   `---   ( - a:f -         
  |   '///`  | `-.                         
  |     | |  |    `-.                      
  |     | |  |       `-.                   
  |     | |\ |                             
  |     | | \|                             
   `-.  | |  |                             
      `-| '
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name

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
