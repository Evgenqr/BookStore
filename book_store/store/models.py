from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    """Авторы"""
    name = models.CharField("Автор", max_length=150)
    age = models.IntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("", upload_to="author/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    """Жанр"""
    name = models.CharField("Жанр", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Publisher(models.Model):
    """Издательство"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    cover = models.ImageField("Обложка", upload_to="books/")
    year = models.PositiveIntegerField("Год выпуска", default=2019)
    language = models.CharField("Язык издания", max_length=30)
    authors = models.ManyToManyField(Author,
                                     verbose_name="автор",
                                     related_name="book_author")
    publishers = models.ManyToManyField(Publisher, verbose_name="Издательство")
    categories = models.ManyToManyField(Category, 
                                        verbose_name="Категория", 
                                        related_name="book_category")
    genres = models.ManyToManyField(Genre, verbose_name="жанр")
    price = models.PositiveIntegerField("Цена",
                                        default=0,
                                        help_text="указывать сумму в рублях")
    page = models.PositiveIntegerField("Количество страниц", default=0)
    
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self',
                               verbose_name="Родитель",
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True)
    book = models.ForeignKey(Book,
                             verbose_name="книга",
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
