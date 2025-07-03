from sistemacooperativa import app, database
from sistemacooperativa.models import Usuario

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     Usuario.query.all()
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.username)
#     print(meus_usuarios.email)
#     print(meus_usuarios.senha)

with app.app_context():
    usuario2 = Usuario.query.filter_by(email='developersabino@gmail.com').first()
    print(usuario2.username)
    print(usuario2.email)
    print(usuario2.senha)
    print(usuario2.cursos)
