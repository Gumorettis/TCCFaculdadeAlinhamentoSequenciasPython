from multiprocessing import Pool, cpu_count
from time import time
from global_alignment import GlobalAlignment
from local_alignment import LocalAlignment
from score import Score

score = Score(
    match=10,
    mismatch=-5,
    gap=-7
)

#rodar com a sequencia na mão, sem precisar do txt
def run_hardcode():
    """
    Exemplo rodando alinhamentos local e global, passando a entrada pelo código
    """
    local_alignment = LocalAlignment(
        s='AGCGTAG',
        t='CTCGTC',
        score=score
    )

    local_alignment.run()

    print(local_alignment, '\n')

    global_alignment = GlobalAlignment(
        s='AGCGTAG',
        t='CTCGTC',
        score=score
    )

    global_alignment.run()

    print(global_alignment)


def generate_sequences(filename):
    """
    Esta função gera duas sequências s e t de entrada a cada linha lida do arquivo.
    Também conhecido como generator:

    LER MAIS EM ===> http://pythonclub.com.br/python-generators.html

    Args:
        filename (str): Nome do arquivo de entrada

    """
    with open(filename, 'r') as f:
        s = f.readline()
        t = f.readline()

        yield [s.rstrip(), t.rstrip()]

        for line in f:
            s = t
            t = line.rstrip()

            yield [s, t]


def run(sequences):
    """
    Executa o alinhamento global de duas sequências passadas por parâmetro.

    Args:
        sequences[0]: sequência s
        sequences[1]: sequência t

    Returns: Similaridade entre as sequências s e t.
    """
    s = sequences[0]
    t = sequences[1]

    local_alignment = LocalAlignment(
        s=s,
        t=t,
        score = score
    )
    local_alignment.run()

    # global_alignment = GlobalAlignment(
    #     s=s,
    #     t=t,
    #     score=score
    # )
    # global_alignment.run()

    #mostra as sequencias e a similaridade, retorno multiplo alinhamento global
    # similarity = global_alignment.get_similarity()
    # sequences = global_alignment.get_alignments()

    #as duas linhas abaixo imprimi o alinhamento local
    similarity = local_alignment.get_similarity()
    sequences = local_alignment.get_alignments()

    return similarity,sequences

def print_sequencies(similarity, sequences):
    print('Similaridade: ', similarity)
    [s, t] = sequences
    print('S = %s' % s)
    print('T = %s' % t)
    print("\n")

def run_file_serial(filename):
    for sequences in generate_sequences(filename):
        run(sequences)

def run_file_thread(filename):
    #define usar o numero de nucleos de cpu existentes para processar, inves de determinar numero fixo de processos
    pool = Pool(cpu_count())
    results = pool.map_async(run, generate_sequences(filename))
    pool.close()
    pool.join()
    sequences_results = results.get()

    for similarity, sequences in sequences_results:
        print_sequencies(similarity, sequences)

    return sequences_results # retorna um array com os valores de similaridade (SAIDA DO PROGRAMA)


#metodo de start do programa, definindo os main
if __name__ == '__main__':
    start_time = time()
    run_file_serial('input.txt')
    end_time = time()


    start_time_paralelo = time()
    run_file_thread('input.txt')
    end_time_paralelo = time()
    print('==== Tempo de execução serial {0} seconds ===='.format(end_time - start_time))
    print('==== Tempo de execução paralela {0} seconds ===='.format(end_time_paralelo - start_time_paralelo))

