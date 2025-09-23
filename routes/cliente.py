from flask import Blueprint,render_template,request
from database.models.cliente import Cliente

cliente_route=Blueprint('cliente',__name__)

@cliente_route.route('/')
def lista_cliente():
    """
    LISTAR CLIENTES
    """
    clientes = Cliente.select()
    return render_template('lista_clientes.html',clientes=clientes)

@cliente_route.route('/',methods= ['POST'])
def inserir_clientes():
    """
    INSERIR OS DADOS DO CLIENTE
    """
    data = request.json
    
    novo_usuario = Cliente.create(
        nome= data['nome'],
        email= data['Email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_clientes():
    """
    FORMULARIO PARA CRIAR UM CLIENTE
    """
    return render_template('form_clientes.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    """EXIBIR DETALHES CLIENTES"""
    
    cliente = Cliente.get(Cliente.id == cliente_id )
    return render_template('detalhe_clientes.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_clientes(cliente_id):
    """
    FORMULARIO PARA EDITAR UM CLIENTE
    """
    cliente = Cliente.get(Cliente.id == cliente_id )

    return render_template('form_clientes.html', cliente= cliente)

@cliente_route.route('/<int:cliente_id>/update', methods= ['PUT'])
def atualizar_clientes(cliente_id):
    """ ATUALIZAR INFORMAÇÕES DO CLIENTE """
    #Obter dados do formulario de edicao
    data=request.json
    cliente_editado = Cliente.get(Cliente.id == cliente_id )
    cliente_editado.nome =data['nome']
    cliente_editado.email =data['Email']
    cliente_editado.save()


    #editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)
    

@cliente_route.route('/<int:cliente_id>/delete', methods= ['DELETE'])
def deletar_clientes(cliente_id):
    cliente = Cliente.get(Cliente.id == cliente_id )
    cliente.delete_instance()
    return {'Deleted': 'ok'}