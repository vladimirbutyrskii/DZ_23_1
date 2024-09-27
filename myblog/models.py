from django.db import models

class Myblog(models.Model):
    title = models.CharField(max_length=150,
        verbose_name="Заголовок поста",
        help_text="Введите заголовок",
    )

    slug = models.CharField(max_length=150, verbose_name="Slug", null=True, blank=True)
    body = models.TextField(verbose_name="Содержимое", help_text="Введите текст поста")
    preview = models.ImageField (
        upload_to="myblog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату создания поста",
        blank=True,
        null=True,
    )
    public = models.BooleanField(
        verbose_name="Признак публикации",
        help_text="Введите признак публикации поста",
        default=False
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

