from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators, DecimalField


# StringField x TextAreaField --> O StringField é usado apenas para texto simples de linha única, enquanto o TextAreaField
# é usado para área de texto de múltiplas linhas.

class Addprodutos(Form):
    name = StringField('Nome:', [validators.data_required()])
    price = DecimalField('Preço:', [validators.data_required()])
    discount = IntegerField('Disconto:', [validators.data_required()])
    stock = IntegerField('Estoque:', [validators.data_required()])
    description = TextAreaField('Descrição:', [validators.data_required()])
    colors = TextAreaField('Cor:', [validators.data_required()])

    image_1 = FileField('Image 1:', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2:', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3:', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])