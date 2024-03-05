class Radio:    #Define a classe "Radio"
    def __init__(self):
        self.estado = 'desligado'
        self.volume = 'on'

    #Métodos
    def ligar(self):
        if self.estado == 'ligado':
            print(f'O rádio está ligado.')
        else:
            self.estado = 'ligado'
            print(f'O rádio está {self.estado}.')


    def desligar(self):
        if self.estado == 'desligado':
            print(f'O rádio está desligado.')
        else:
            self.estado = 'desligado'
            print(f'O rádio está {self.estado}.')
            

    def aum_vol(self):
        if self.estado == 'ligado':
            if self.volume == 'off':
                print(f'O áudio não pode ser escutado.')
                self.volume = 'on'
            elif self.volume == 'on':
                print(f'O som está audível agora.')


    def mudo(self):
        if self.estado == 'ligado':
            if self.volume == 'on':
                print('O rádio está audível.')
                self.volume = 'off'
                print('Abaixando o volume agora.')


radio = Radio()
