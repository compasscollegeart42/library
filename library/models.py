import datetime

from django.db import models


class authors(models.Model):
    name = models.CharField("ФИО", max_length=50, help_text='Фамилия Имя Отчество')
    biography = models.TextField("Биография", help_text='Биография')
    description = models.CharField("Описания", max_length=250, help_text='Описания деятельности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class translater(models.Model):
    name = models.CharField("ФИО", max_length=50, help_text='Фамилия Имя Отчество')
    biography = models.TextField("Биография", help_text='Биография')
    description = models.CharField("Описания деятельности", max_length=250, help_text='Описания деятельности')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Переводчик'
        verbose_name_plural = 'Переводчики'


class public(models.Model):
    title = models.CharField("Название", max_length=80, help_text='Название издателя')
    description = models.CharField("Описания", max_length=250, help_text='Описания деятельности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class genre(models.Model):
    title = models.CharField("Название", max_length=80, help_text='Название издателя')
    description = models.CharField("Описания", max_length=250, help_text='Описания деятельности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class books(models.Model):
    title = models.CharField("Название", max_length=120, help_text='Название книги')
    authors = models.ManyToManyField(authors, verbose_name="Автор", related_name='author')
    translater = models.ManyToManyField(translater, verbose_name='Переводчик', related_name='translater')
    public = models.ManyToManyField(public, verbose_name='Издатель', related_name='public')
    num_list = models.PositiveSmallIntegerField("Число страниц", default=5)
    description = models.TextField("Описание")
    date_write = models.PositiveSmallIntegerField("Дата написание", default=2020)
    year_public = models.PositiveSmallIntegerField("Год издания", default=2020)
    admission = models.DateField("Дата поступление", default=datetime.date.today)
    genre = models.ForeignKey(genre, verbose_name='жанры', on_delete=models.SET_NULL, null=True)
    files = models.FileField("Файл книги", upload_to="books/")
    image = models.ImageField("Обложка книги", upload_to="images/")
    url = models.SlugField("Ccылка", max_length=160, unique=True, help_text="Цифры либо текст с латинскими буквами")
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

