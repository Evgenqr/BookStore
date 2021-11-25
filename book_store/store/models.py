from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.utils.safestring import mark_safe

from .utils import upload_function


class BookType(models.Model):
    """Вид книги"""
    name = models.CharField(verbose_name="Вид книги", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид книги"
        verbose_name_plural = "Виды книг"


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
    # url = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField("", upload_to="author/")
    image = models.ImageField(upload_function, null=True, blank=True)

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

    # url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    # cover = models.ImageField("Обложка", upload_to="books/")
    cover = models.ImageField(upload_function)
    year = models.PositiveIntegerField("Год выпуска", default=2019)
    language = models.CharField("Язык издания", max_length=30)
    author = models.ManyToManyField(Author,
                                    verbose_name="автор",
                                    related_name="book_author")
    publisher = models.ManyToManyField(Publisher, verbose_name="Издательство")
    category = models.ManyToManyField(Category,
                                      verbose_name="Категория",
                                      related_name="book_category")
    genre = models.ManyToManyField(Genre, verbose_name="жанр")
    price = models.DecimalField(verbose_name="Цена",
                                max_digits=9,
                                decimal_places=2,
                                default=0,
                                help_text="указывать сумму в рублях")
    # price = models.PositiveIntegerField("Цена",
    #                                     default=0,
    #                                     help_text="указывать сумму в рублях")
    page = models.PositiveIntegerField("Количество страниц", default=0)
    slug = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    offer_of_the_week = models.BooleanField(default=False,
                                            verbose_name="Предложение недели?")

    # book_type = models.ForeignKey(BookType, verbose_name="")

    def __str__(self):
        return f"{self.id} | {self.title}"
        # return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    @property
    def ct_model(self):
        return self._meta.model_name

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


class CartProduct(models.Model):
    """Продукт корзины"""
    user = models.ForeignKey('Customer',
                             verbose_name='Покупатель',
                             on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart',
                             verbose_name='Корзина',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9,
                                      decimal_places=2,
                                      verbose_name='Цена итого')

    def __str__(self):
        return f"Продкут: {self.content_object.name} (для корзины)"

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт корзины'
        verbose_name_plural = 'Продукты корзины'


class Cart(models.Model):
    """Корзина"""
    owner = models.ForeignKey('Customer',
                              verbose_name='Покупатель',
                              on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct,
                                      blank=True,
                                      related_name='related_cart',
                                      verbose_name='Продукты для корзины')
    total_products = models.IntegerField(default=0,
                                         verbose_name='Общее кол-во товара')
    final_price = models.DecimalField(max_digits=9,
                                      decimal_places=2,
                                      verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    """Заказ пользователя"""

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = ((STATUS_NEW, 'Новый заказ'), (STATUS_IN_PROGRESS,
                                                    'Заказ в обработке'),
                      (STATUS_READY, 'Заказ готов'),
                      (STATUS_COMLETED, 'Заказ получен покупателем'))

    BUYING_TYPE_CHOICES = ((BUYING_TYPE_SELF, 'Самовывоз'), (BUYING_TYPE_SELF,
                                                             'Доставка'))

    customer = models.ForeignKey('Customer',
                                 verbose_name='',
                                 related_name='orders',
                                 on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    cart = models.ForeignKey(Cart,
                             verbose_name='Корзина',
                             on_delete=models.CASCADE)
    adress = models.CharField(max_length=1024,
                              verbose_name='Адрес',
                              null=True,
                              blank=True)
    status = models.CharField(max_length=200,
                              verbose_name='Статус заказа',
                              choices=STATUS_CHOICES,
                              default=STATUS_NEW)

    buying_type = models.CharField(max_length=100,
                                   verbose_name='Тип заказа',
                                   choices=BUYING_TYPE_CHOICES)
    comment = models.TextField(verbose_name='Комментарий',
                               null=True,
                               blank=True)
    created_at = models.DateField(verbose_name='Дата создания заказа',
                                  auto_now=True)
    order_date = models.DateField(verbose_name='Дата получения заказа',
                                  default=timezone.now)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    """Покупатель"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активный?')
    customer_orders = models.ManyToManyField(Order,
                                             blank=True,
                                             related_name='related_customer',
                                             verbose_name='Заказы покупателя')
    wishlist = models.ManyToManyField(Book,
                                      blank=True,
                                      verbose_name='Лист ожидания')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return f"{self.user.username}"


class Notification(models.Model):
    """Уведомления"""
    recipient = models.ForeignKey(Customer,
                                  on_delete=models.CASCADE,
                                  verbose_name='')
    test = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Уведомление для {self.recipient.user.username} | id={self.id}"

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомление"


class ImageGalery(models.Model):
    """Галеря изображений"""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to=upload_function)
    use_in_slider = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Изображение для {self.content_object}"

    def image_url(self):
        return mark_safe(f'<img src="{self.image}" width="auto" height="20px"')

    class Meta:
        verbose_name = "Галерея изображений"
        verbose_name_plural = "Галерея изображений"