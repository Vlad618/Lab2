from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ModAuthor(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # 🔗 зв’язок між таблицями (ОБОВ’ЯЗКОВО)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(ModAuthor, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name