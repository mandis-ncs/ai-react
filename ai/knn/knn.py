import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


dados = pd.read_csv('4/wine.data') #transforma num dataframe

dados.dropna

x = np.array(dados.iloc[:, 0:14])
y = np.array(dados['class'])

scaler = MinMaxScaler()
x = scaler.fit_transform(x)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7, test_size=0.3)

vizinho = 7
knn = KNeighborsClassifier(vizinho)
knn.fit(xtrain, ytrain)
previsao = knn.predict(xtest)

acuracia = accuracy_score(ytest, previsao) * 100
print('Acuracia de %.2f%%' %acuracia)

print(confusion_matrix(ytest, previsao))