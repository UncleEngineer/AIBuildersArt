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


class MCCHAKKRAPONG:
    '''
    test = MCCHAKKRAPONG()
    test.art()
    '''
    def __init__(self):
        self.name = 'chakkrapong mc'

    def art(self):
        asciiart = '''
-----------------------------------------------
    a'!   _,,_ a'!   _,,_     a'!   _,,_
  \\_/    \  \\_/    \      \\_/    \.-,
   \, /-( /'-,\, /-( /'-,    \, /-( /
   //\ //\\   //\ //\\       //\ //\\jrei
-----------------------------------------------
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name