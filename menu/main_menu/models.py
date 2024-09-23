from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    """Модель древовидного меню."""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Название', max_length=64)
    url = models.URLField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'