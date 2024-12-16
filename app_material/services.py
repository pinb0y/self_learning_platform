from django.utils.text import slugify
from unidecode import unidecode


def generate_unique_slug(obj, title):
    """Преобразует название в слаг и делает его уникальным"""

    origin_slug = slugify(unidecode(title))
    unique_slug = origin_slug
    numb = 1
    while obj.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{origin_slug}-{numb}"
        numb += 1
    return unique_slug
