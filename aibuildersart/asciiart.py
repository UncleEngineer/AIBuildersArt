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

class GuitarDev:
    '''
    test = UncleEngineer()
    test.art()
    '''
    def __init__(self):
        self.name = 'GuitarDev'

    def art(self):
        asciiart = '''
                                                                   . ,,                 
                                                         ,(&&/   %/             
                                                       /##%&.    &@%            
                                                       ,%%     *@&%.            
                                                        &,    ,@&(              
                                                       *&.#&&#% ,.              
                                                      %* .&,                    
                                                    *&  .%                      
                                                   &(. #*                       
                                                 *&/ .&.                        
                                               .&#/ *#                          
                                              /##/.%*                           
                                             &,%*.&.                            
                                           /(.#*/#                              
                               ,#@&&&@#, .@..%*%.                               
                             &,         (( .%/%                                 
                            %.        .&. ,#%/       I'm Guitar Dev.                      
                           ,#        #(  .%&.                                   
                          .&    *&#//#&(,%%&,                                   
                       ./&,   #(&*    ,&*%   /&%/,                              
                 ,%&,        ,(%        %/(      ,%                             
              *&.             &#*      ,&(,    *&.                              
            *%                 ##(&%%%#(%.  .&*                                 
           (/                              .%                                   
          .%         .&/                   .%                                   
          ,#         (* .%#.                %.                                  
           &.          .&   ,%%*            (,                                  
           ,#            ,%(,.*, .##        %.                                  
            .&.                 ..         ,#                                   
              ,&.                         ,%                                    
                 ##.                    .%*                                     
                    .%&,              (&.                                       
                          .*(#%&%#(,                                            
        '''
        print(asciiart)
        
    def __str__(self):
        return self.name
