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


class takatbprint:
    '''
    test = takatbprint()
    test.art()
    '''
    def __init__(self):
        self.name = 'Tang'

    def art(self):
        asciiart = '''


__________________|      |____________________________________________
     ,--.    ,--.          ,--.   ,--.
    |oo  | _  \  `.       | oo | |  oo|
o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
    |/\/\|   '._,'        |/\/\| |/\/\|
__________________        ____________________________________________
                  |      |dwb                         
                         
                    
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
