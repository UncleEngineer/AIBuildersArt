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


class MeenAnusak:
    '''
    test = MeenAnusak()
    test.art()
    '''

    def __init__(self):
        self.name = 'Meen Anusak'

    def art(self):
        asciiart = '''
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm

        '''
        print(asciiart)

    def __str__(self):
        return self.name


test = MeenAnusak()
test.art()
