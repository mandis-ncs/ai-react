import random

class AlgoritmoGenetico:
    # metodo construtor
    def __init__(self):
        self.tamanho_populacao = 20
        self.populacao = []
        self.numero_geracoes = 10
        self.numero_filhos = 14
        self.filhos = []
        self.mutacao = 1


    def avaliar_individuo(self, x, y, z):
        return (x**2)-(3*y)+(4*z)


    def criar_populacao(self):
        for i in range(ag.tamanho_populacao):
            x = random.randint(-10, 10)
            y = random.randint(0, 12)
            z = random.randint(-20, 20)
            fitness = ag.avaliar_individuo(x, y, z)
            individuo = [x, y, z, fitness]
            ag.populacao.append(individuo)


    def selecionar_pai(self):
        pos_candidato1 = random.randint(0, 19)
        pos_candidato2 = random.randint(0, 19)

        pos_pai = 0

        print(f"pai 1: {ag.populacao[pos_candidato1]}")
        print(f"pai 2: {ag.populacao[pos_candidato2]}")

        if (ag.populacao[pos_candidato1][3] > ag.populacao[pos_candidato2][3]):
            pos_pai = pos_candidato1
        else:
            pos_pai = pos_candidato2
        
        return pos_pai


    def cruzamento(self, pos_pai1, pos_pai2):
        x_f1 = ag.populacao[pos_pai1][0]
        x_f2 = ag.populacao[pos_pai2][0]
        y_f1 = ag.populacao[pos_pai2][1]
        y_f2 = ag.populacao[pos_pai1][1]
        z_f1 = ag.populacao[pos_pai1][2]
        z_f2 = ag.populacao[pos_pai2][2]
        
        fitness_f1 = ag.avaliar_individuo(x_f1, y_f1, z_f1)
        fitness_f2 = ag.avaliar_individuo(x_f2, y_f2, z_f2)
        
        return [x_f1, y_f1, z_f1, fitness_f1], [x_f2, y_f2, z_f2, fitness_f2]


    def realizar_mutacao(self, filho):
        valor_x = random.randint(0, 100)
        valor_y = random.randint(0, 100)
        valor_z = random.randint(0, 100)

        if(valor_x <= ag.mutacao):
            filho[0] = random.randint(-10, 10)
        
        if(valor_y <= ag.mutacao):
            filho[1] = random.randint(0, 12)
        
        if(valor_z <= ag.mutacao):
            filho[2] = random.randint(-20, 20)

        return filho


    def realizar_descarte(self, individuos):
        ag.populacao = sorted(individuos, key=lambda x:x[3])
        ind = 1
        while ind <= ag.numero_filhos:
            del ag.populacao[0]
            ind += 1


    def reproduzir(self):
        f = 1
        while f <= 7:
            pos_pai1 = ag.selecionar_pai()
            pos_pai2 = ag.selecionar_pai()

            filho1, filho2 = ag.cruzamento(pos_pai1, pos_pai2)
                        
            filho1 = ag.realizar_mutacao(filho1)
            filho2 = ag.realizar_mutacao(filho2)

            ag.filhos.append(filho1)
            ag.filhos.append(filho2)

            print(f"filho 1: {filho1}")
            print(f"filho 2: {filho2}")

            f += 1


    def verificar_melhor_individuo(self):
        print("O melhor individuo: ")
        print("x = ", ag.populacao[19][0])
        print("y = ", ag.populacao[19][1])
        print("z = ", ag.populacao[19][2])
        print("fitness = ", ag.populacao[19][3])


    def iniciar_execucao(self):
        ag.criar_populacao()
        contador_geracoes = 1

        while contador_geracoes <= ag.numero_geracoes:
            print("Geracao ", contador_geracoes)
            ag.filhos = []
            ag.reproduzir()
            ag.populacao = ag.populacao + ag.filhos
            ag.realizar_descarte(ag.populacao)
            ag.verificar_melhor_individuo()
            contador_geracoes += 1


ag = AlgoritmoGenetico()
ag.iniciar_execucao()