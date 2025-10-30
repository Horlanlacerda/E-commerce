from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    usuario = StringField('Usuário', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite sua senha', [validators.DataRequired(),validators.EqualTo('Confirmar sua senha', message='Sua senha e confirmação não são iguais')])
    confirmacao = PasswordField('Repita sua senha')