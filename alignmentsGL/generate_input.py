#Arquivo para entrar com o txt das entradas para o alinhamento e utilizar o arquivo dentro do for
from random import choice, randint

NUM_SEQUENCES = 100
MIN_SIZE = 200 #minimo de cada sequencia
MAX_SIZE = 300 #maximo de cada sequencia
ALPHABET = 'ACGTU' #alfabeto

input_file = open('input.txt', 'w')

#preenche o arquivo com as sequencias
for i in range(NUM_SEQUENCES):
    size = randint(MIN_SIZE, MAX_SIZE)
    seq = ''
    for j in range(size):
        seq += choice(ALPHABET)
    if i + 1 == NUM_SEQUENCES:
        input_file.write(seq)
    else:
        input_file.write(seq + '\n')

input_file.close()
