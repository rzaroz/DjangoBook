import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    tag = models.CharField(max_length=100, verbose_name="تگ")

    def __str__(self):
        return f"{self.name} - {self.tag}"

    class Meta:
        verbose_name_plural = 'دسته بندی ها'

class Products(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)
    price = models.IntegerField()
    p_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="Products/")

    # cat = models.OneToOneField(Categories, on_delete=models.CASCADE)
    cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # cat = models.ManyToManyField(Categories)

    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True, default='default-slug',
                            null=True, blank=True)

    def __str__(self):
            return f"{self.name} - {self.price} - {self.pk}"

    class Meta:
        verbose_name_plural = 'محصولات'


@receiver(post_save, sender=Products)
def add_slug(sender, instance, created, **kwargs):
    if created:
       uniq_k = str(uuid.uuid4()).split("-")[0]
       slug = instance.name.replace(" ", "-") + "-" + uniq_k
       instance.slug = slug
       instance.save(update_fields=["slug"])

