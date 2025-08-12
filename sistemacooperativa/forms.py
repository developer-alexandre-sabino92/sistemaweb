from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, optional
from sistemacooperativa.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta', validators=[])

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado. Utilize outro email.')

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg','png', 'jpeg'])])
    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('Vba Impressionador')
    curso_powerbi = BooleanField('Power Bi Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Apresentações Impressionadoras')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição', validators=[])

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse email. Cadastre outro email')



class FormCriarPost(FlaskForm):
    titulo = StringField('Nome do Cliente', validators=[DataRequired(), Length(2, 140)])
    implantacao = DateField('Data da Implantação',validators=[DataRequired()])
    numero_contrato = StringField('Número do Contrato', validators=[DataRequired(), Length(2, 140)])
    cnpj_cpf = StringField('CNPJ ou CPF', validators=[DataRequired(), Length(2, 140)])
    razao_social = StringField('Razão Social', validators=[DataRequired(), Length(2, 140)])
    valor_contrato = DecimalField('Valor do Contrato R$', places=2, rounding=None, validators=[DataRequired(), NumberRange(min=0)])
    bonus_vida = StringField('Bônus por Vida?', validators=[DataRequired(), Length(2, 140)])
    valor_bonus = DecimalField('Valor do Bônus', places=2, rounding=None, validators=[DataRequired(), NumberRange(min=0)])
    corpo = StringField('Operadora', validators=[DataRequired(), Length(2, 140)])
    botao_submit = SubmitField('Cadastrar')
