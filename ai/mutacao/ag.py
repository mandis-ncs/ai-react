import random

# Maximizar X^2-3Y+4Z
class AlgoritmoGenetico:
    # Seria o Constructor do Java - Permite com que possamos inicializar o nosso atributo
    def iniciar_execucao(self):
        # Declaração dos atributos necessários de cada classe
        # Primeiro tamanho deve ser o tamanho da população
        self.tamanho_populacao = 20
        # Permite com que eu armazene a minha população
        self.populacao = []
        # Definição de um critério de parada (Somente uma observação minha)
        self.num_geracoes = 10
        # Seleção dos pais e escolher qual é o tipo de seleção
        # Pra iniciar a fase de reprodução, eu preciso saber quantos filhos devem ser gerados
        self.num_filhos = 14
        self.filhos = []
        # Os filhos entram na sociedade, mas antes de integrarem a sociedade, eles devem passar por mutação
        self.mutacao = 1

    #funcao fitness, pontua cada membro da populacao
    def avaliar_individuo(self,x,y,z):
        return (x*x)-(3*y)+(4*z)

    def criar_populacao(self):
        for i in range (ag.tamanho_populacao):
            x = random.randint(-10,10)
            y = random.randint(0,12)
            z = random.randint(-20,20)
            fitness = ag.avaliar_individuo(x,y,z)
            individuo = [x,y,z,fitness]
            ag.populacao.append(individuo)
            
    def selecionar_pai(self):
        #precisa de dois candidatos para competir
        #selecao por torneio para escolher o pai
        #nao tem problema os dois candidatos tem o mesmo numero
        pos_cand1 = random.randint(0,19)
        pos_cand2 = random.randint(0,19)

        #descobrir a posicao do pai
        pos_pai = 0

        #para descobrir posicao do pai precisa comparar o fitness (parametro 3 do array populacao)
        #se torna o pai quem tem maior fitness
        if (ag.populacao[pos_cand1][3] > ag.populacao[pos_cand2]):
            pos_pai = pos_cand1
        else:
            pos_pai=pos_cand2
        return pos_pai
    
    def realizar_mutacao(self, filho):
        #pega valor aleatorio entre 0 e 100 
        valorx = random.randint(0,100)
        valory = random.randint(0,100)
        valorz = random.randint(0,100)

        if (valorx <= ag.mutacao):
            filho[0] = random.randint(10,-10)
        if (valory <= ag.mutacao):
            filho[0] = random.randint(0,12)
        if (valorz <= ag.mutacao):
            filho[0] = random.randint(-20,20)

        return filho
    
    def realizar_descarte(self, individuos):
        #vai fazer o SORT dos individuos, e vai descartar o de MENORES NOTAS
        #se fizer SORT crescente, a menor nota está no topo, eliminamos os individuos do topo entao
        #se fizer SORT decrescente, eliminamos os ultimos individuos
        ag.populacao = sorted(individuos, key=lambda x:x[3])
        ind = 1
        while ind <= ag.num_filhos:
            del ag.populacao[0]
            ind +=1

    def reproduzir(self):
        
        # f é uma variavel que vai contar quantos crossovers precisamos fazer para ter as 14 geracoes de filhos
        f=1
        while f <= 7:
            pos_pai1 = ag.selecionar_pai()
            pos_pai2 = ag.selecionar_pai()

            xf1 = ag.populacao[pos_pai1][0]
            xf2 = ag.populacao[pos_pai2][0]
            yf1 = ag.populacao[pos_pai2][1]
            yf2 = ag.populacao[pos_pai1][1]
            zf1 = ag.populacao[pos_pai1][2]
            zf2 = ag.populacao[pos_pai2][2]
            fitnessf1 = ag.avaliar_individuo(xf1,yf1,zf1)
            fitnessf2 = ag.avaliar_individuo(xf2,yf2,zf2)

            #filho1 vai pegar o valor de pos_pai1 para parametro X
                    # X                          Y                          Z 
            filho1 = [xf1, yf1, zf1, fitnessf1]
            filho2 = [xf2, yf2, zf2, fitnessf2]

            #terminou o crossover dos genes dos filhos
            #vai fazer mutacao ANTES de colocar os filhos na populacao

            filho1 = ag.realizar_mutacao(filho1)
            filho2 = ag.realizar_mutacao(filho2)

            #depois da mutacao, adicionamos a geracao nova a populacao de filhos
            ag.filhos.append(filho1)
            ag.filhos.append(filho2)
            f+=1

    def verificar_melhor_individuo(self):
        print("O melhor individuo: ")
        print("x = ", ag.populacao[19][0])
        print("y = ", ag.populacao[19][1])
        print("z = ", ag.populacao[19][2])
        print("fitness = ", ag.populacao[19][3])

    def iniciar_execucao(self):
        ag.criar_populacao()
        contador_geracoes = 1

        while contador_geracoes <= ag.num_geracoes:
            print("Geracao: ", contador_geracoes)
            ag.filhos=[]
            ag.reproduzir()
            ag.populacao=ag.populacao+ag.filhos
            ag.realizar_descarte()
            ag.verificar_melhor_individuo()
            contador_geracoes +=1

        
# A partir dela conseguiremos acessar todos os atributos e métodos pertencentes à classe
ag = AlgoritmoGenetico()
ag.iniciar_execucao()

# 1º Passo - Criação da população inicial
# 2º Passo - Roda a condição de parada

#selecionar pais iguais diminui a variabilidade