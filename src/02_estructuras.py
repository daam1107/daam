"""
Tupla: 
    - inmutables
    - mentienen el orden
"""

punto1 = (0,1)
print(type(punto1))

# unpacking
x, y = punto1 
print(f'X: {x}, Y: {y}')

largo = len(punto1)
print('El largo del punto1 es {}'.format(largo))

"""
Listas: 
    - Son mutables
    - Son dinámicas en tamaño
    - Reciben cualquier tipo de dato
"""

lista_ml = ['SVM', 'RF', 'XGBoost']
lista_accuracy = [90, 88.5, 63.4, 70]

print(lista_ml)
print(type(lista_ml))


lista_ml.append('Decision Tree')
print(lista_ml)

"""
Diccionario:
    - Colección Key:Value
    - Las key son únicas
    - No tienen orden en partícular
    - Array asociativos
"""

supervisado = {
    'svm':'support vector machine',
    'lr': ' logistic regression',
    'xgb': 'XGBoost'
}



#hyperopt = {
    # learning rate
#    'lr': [0.005, 0.05, 0.2]
#}

print(supervisado)
print(type(supervisado))

print(supervisado['svm'])