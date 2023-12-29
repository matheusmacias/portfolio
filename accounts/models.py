from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class User(AbstractUser):
    gender_choices = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    )

    avatar = models.ImageField('Imagem principal', upload_to='accounts/avatar', blank=True, null=True, default='accounts/avatar/default-user.png')
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    is_verified = models.BooleanField('Verificado', default=False)
    gender = models.CharField('Gênero', max_length=10, choices=gender_choices, blank=True, null=True)
    birthday = models.DateField('Aniversário', blank=True, null=True)
    is_owner = models.BooleanField('Proprietário', default=False)
    description = CKEditor5Field("Descrição", config_name="extends", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_owner:
            User.objects.filter(is_owner=True).update(is_owner=False)
            User.objects.filter(pk=self.pk).update(is_owner=True)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField('Empresa', max_length=100, blank=True, null=True)
    position = models.CharField('Cargo', max_length=100, blank=True, null=True)
    description = models.TextField('Descrição', blank=True, null=True)
    start_date = models.DateField('Data de início', blank=True, null=True)
    end_date = models.DateField('Data de término', blank=True, null=True)
    is_current = models.BooleanField('Atualmente', default=False)

    def save(self, *args, **kwargs):
        if self.is_current:
            Experience.objects.filter(user=self.user).update(is_current=False)
            Experience.objects.filter(pk=self.pk).update(is_current=True)
        super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.company}'