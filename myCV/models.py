from django.db import models

# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )

    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )


    def __str__(self):
        return f'GeneralSetting: {self.name}'

    class Meta:
        verbose_name = 'GeneralSetting'
        verbose_name_plural = 'GeneralSettings'
        ordering = ('name',)

class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.'
    )

    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text=''
    )

    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )

    def __str__(self):
        return f'ImageSetting: {self.name}'

    class Meta:
        verbose_name = 'ImageSetting'
        verbose_name_plural = 'ImageSettings'
        ordering = ('name',)
