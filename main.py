class TV:
    def __init__(self, tamanho, marca):
        self.marca = marca
        self.tamanho = tamanho
        self.ligada = False
        self.canal_atual = 1
        self.volume = 50

    def ligar_desligar(self):
        self.ligada = not self.ligada
        if self.ligada:
            print("A TV Está Ligada.")
        else:
            print("A TV Está Desligada.")
        
    def alterar_canal(self, canal):
        if self.ligada:
            if 1 <= canal <= 100:
                self.canal_atual = canal
                print(f"Canal Alterado para {canal}.")
            else:
                print(f"Canal Inválido.")
        else:
            print("A TV Está Desligada.")

    def aumentar_volume(self):
        if self.ligada:
            if self.volume < 100:
                self.volume += 1
                print("Volume Aumentado.")
            else:
                print("Volume Já Está No Máximo.")
        else:
            print("A TV Está Desligada.")

    def diminuir_volume(self):
        if self.ligada:
            if self.volume > 0:
                self.volume -= 1
                print("Volume Diminuido.")
            else:
                print("Volume Já Está No Mínimo.")
        else:
            print("A TV Está Desligada.")

    def mudo(self):
        if self.ligada:
            if self.volume != 0:
                self.volume_anterior = self.volume
                self.volume = 0
                print("Modo Mudo Ativado.")
            else:
                self.volume = self.volume_anterior
                self.volume_anterior = None
                print("Modo Mudo Desativado.")
        else:
            print("A TV Está Desligada.")

    def status(self):
        print(f"Status: {'Ligada' if self.ligada else 'Desligada'}")
        

    def informacao_tv(self):
        print(f"Marca: {self.marca}")
        print(f"Tamanho: {self.tamanho} polegadas")
        if self.ligada:
            print(f"Canal Atual: {self.canal_atual}")
            print(f"Volume: {self.volume}")
        else:
            print("A TV Está Desligada.")
class Controle_Remoto:
    def __init__(self, tv):
        self.tv = tv

    def power(self):
        print("Botão Power Pressionado.")
        self.tv.ligar_desligar()

    def volume_mais(self):
        print("Botão Volume Mais Pressionado.")
        self.tv.aumentar_volume()

    def volume_menos(self):
        print("Botão Volume Menos Pressionado.")
        self.tv.diminuir_volume()

    def canal_mais(self):
        print("Botão Canal Mais Pressionado.")
        self.tv.alterar_canal(self.tv.canal_atual + 1)

    def canal_menos(self):
        print("Botão Canal Menos Pressionado.")
        self.tv.alterar_canal(self.tv.canal_atual - 1)

    def mute(self):
        print("Botão Mute Pressionado.")
        self.tv.mudo()

    def informacoes(self):
        print("Botão Informações Pressionado.")
        self.tv.informacao_tv()

    def status_desligado_ligado(self):
        self.tv.status_tv()

    def numero(self, num):
        if 0 <= num <= 9:
            print(f"Digitou o Número {num}.")
        else:
            print("Número Inválido.")


tv_sala = TV(marca="Samsung", tamanho=42)
print("Status Atual")
controle_sala = Controle_Remoto(tv_sala)
controle_sala.informacoes()
print("\n")
tv_sala.status()
print("\n")
tv_sala.ligar_desligar()
tv_sala.alterar_canal(5)
tv_sala.aumentar_volume()
tv_sala.status()
print("\n")
tv_sala.diminuir_volume()
tv_sala.status()
print("\n")


# Controle
controle_sala.power()
controle_sala.power()
controle_sala.volume_mais()
controle_sala.informacoes()
print("\n")
controle_sala.volume_menos()
controle_sala.informacoes()
print("\n")
controle_sala.canal_mais()
controle_sala.numero(5)
controle_sala.informacoes()
print("\n")
controle_sala.power()
controle_sala.informacoes()

