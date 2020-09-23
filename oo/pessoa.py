class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    levy = Pessoa(nome='Levy')
    heber = Pessoa(levy, nome='Heber')
    print(Pessoa.cumprimentar(heber))
    print(id(heber))
    print(heber.cumprimentar())
    print(heber.nome)
    print(heber.idade)
    for filho in heber.filhos:
        print(filho.nome)
    levy.sobrenome = 'Almeida'
    del levy.filhos
    print(levy.__dict__)
    print(heber.__dict__)