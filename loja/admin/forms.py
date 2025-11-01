from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome: ', [validators.Length(min=4, max=25)])
    username = StringField('Usuário: ', [validators.Length(min=4, max=25)])
    email = StringField('Email: ', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite sua senha: ', [validators.DataRequired(),validators.EqualTo('Confirmar sua senha: ', message='Sua senha e confirmação não são iguais')])
    confirm = PasswordField('Repita sua senha: ')