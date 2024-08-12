class BombaDeCombustivel:
    def __init__(self):
        self._valor_litro = 1.1
        self._qtd_disponivel = 10000

    @property
    def valor_litro(self):
        return self._valor_litro
    
    @valor_litro.setter
    def valor_litro(self, valor):
        self._valor_litro = valor

    @property
    def qtd_disponivel(self):
        return self._qtd_disponivel
    
    @qtd_disponivel.setter
    def qtd_disponivel(self, valor):
        self._qtd_disponivel = valor

    def abastecer_por_valor(self, valor):
        if valor < 0:
            print('Este não é um valor válido')
            return

        abastecido = valor / self.valor_litro

        if self.qtd_disponivel < abastecido:
            print('A bomba não possui combustível suficiente')
            return

        self.qtd_disponivel -= abastecido
        print(f'Você abasteceu {round(abastecido, 2)}L de combustível')
    
    def abastecer_por_litro(self, qtd_litro):
        if qtd_litro < 0:
            print('Este não é um valor válido')
            return

        if self.qtd_disponivel < qtd_litro:
            print('A bomba não possui combustível suficiente')
            return

        self.qtd_disponivel -= qtd_litro
        abastecido = qtd_litro * self.valor_litro
        print(f'Você irá pagar {round(abastecido, 2)} reais')

class Etanol(BombaDeCombustivel):
    _tipo_combustivel = 'Etanol'
    def __init__(self):
        super().__init__()
        self.valor_litro = 4.5
    
    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

class Gasolina(BombaDeCombustivel):
    _tipo_combustivel = 'Gasolina'
    def __init__(self):
        super().__init__()
        self.valor_litro = 5.4
    
    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel


b1 = Gasolina()
b1.abastecer_por_litro(53)
b1.abastecer_por_litro(53)
b1.abastecer_por_litro(53)
print(b1.qtd_disponivel)