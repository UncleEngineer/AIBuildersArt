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


class Argirozeal:
    '''
    test = Argirozeal()
    test.art()
    '''
    def __init__(self):
        self.name = 'Argirozeal'

    def art(self):
        asciiart = '''
                 __/___
           _____/______|              Ar
   _______/_____\_______\_____          gi
   \              < < <       |           ro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          zeal

        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
