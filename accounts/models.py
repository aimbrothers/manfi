from django.contrib.auth.models import AbstractUser


class ManfiUser(AbstractUser):
    pass


    def __str__(self):
        return self.username