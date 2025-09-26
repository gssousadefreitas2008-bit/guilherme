#SISTEMA DE BIBLIOTECA
print('--- SISTEMA DE BIBLIOTECA ---')

livros = []
usuarios = []

def visualizar_livro():
    for i, livro in enumerate(livros):
        print(f'{i+1}. {livro['titulo']} - {livro['autor']} - {livro['gênero']} - Editora {livro['editora']}')

def adicionar_livro():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    gênero = input('Digite o gênero do livro: ')
    editora = input('Digite a editora do livro: ')

    livro = {
        'titulo': titulo,
        'autor': autor,
        'gênero': gênero,
        'editora': editora,
        'alugado': False,
        'usuario': None,
        'alugueis': 0,
    }

    livros.append(livro)
    print('Livro adicionado na sua biblioteca')

def adicionar_usuario():
    identidade = input('Identidade: ')
    cpf = input("CPF: ")
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    cep = input('CEP: ')
    bairro = input('Bairro: ')
    estado = input('Estado: ')
    capital = input('Capital:')
    idade = int(input('Idade: '))

    usuario = {
        'identidade': identidade,
        'cpf': cpf,
        'nome': nome,
        'endereco': endereco,
        'cep': cep,
        'bairro': bairro,
        'estado': estado,
        'capital': capital,
        'idade': idade,
    }

    usuarios.append(usuario)
    print('Usuário adicionado na sua biblioteca')

adicionar_usuario()


def alugar_livro():
    visualizar_livro()
    indice = int(input('Digite o número do livro que deseja alugar: ')) - 1

    if livros[indice]['alugado']:
        print('Livro já está alugado.')
    else:
        for i, usuario in enumerate(usuarios):
            print(f"(i+1). {usuario['nome']} - Registro: {usuario['identidade']}")
            usuario_indice = int(input('Escolha o usário pelo número: ')) - 1


            livros[indice]['alugado'] = True
            livros[indice]['usuario'] = usuarios[usuario_indice]['nome']
            livros[indice]['alugueis'] += 1
            print(f'Livro {livros[indice]["titulo"]} alugado para {usuarios[usuario_indice]["nome"]}'
    )
