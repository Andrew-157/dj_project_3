from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models


def validate_file_size(file):
    max_kb_size = 500

    if file.size > max_kb_size * 1024:
        raise ValidationError(f'Files cannot be larger than {max_kb_size}KB')


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(
        upload_to='users/images', validators=[validate_file_size]
    )
