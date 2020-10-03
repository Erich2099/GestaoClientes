import uuid

from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    age = models.IntegerField('Idade')
    endereco = models.CharField('Endereço', max_length=200)
    salario = models.DecimalField('Salário', max_digits=8, decimal_places=2)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Foto', upload_to=get_file_path,
                           variations={'thumb': {'width': 225, 'height': 225, 'crop': True}},  null=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome