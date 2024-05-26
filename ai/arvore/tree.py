import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Carregar o conjunto de dados a partir do CSV
df = pd.read_csv('wine.data')

# Separar as características (features) e o rótulo (label)
X = df.drop('class', axis=1)  # Supondo que a coluna 'class' é o alvo
y = df['class']

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar o classificador de árvore de decisão
clf = DecisionTreeClassifier(random_state=42)

# Treinar o modelo
clf.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = clf.predict(X_test)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")

# Extraindo os nomes das classes
class_names = [str(c) for c in clf.classes_]

# Plotar a árvore de decisão
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=class_names, filled=True)
plt.show()
