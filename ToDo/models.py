from django.db import models


class FormsTarefa(models.Model):
    titulo = models.CharField(max_length=25)
    descricao = models.TextField()
    status = models.CharField(max_length=25)
    projeto = models.CharField(max_length=25)

    def __str__(self):
        return self.titulo

    def resposta_json(self):
        return {
            'titulo': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'projeto': self.projeto
        }
