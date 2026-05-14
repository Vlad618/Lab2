from django.contrib import admin
from .models import Game, Mod, ModAuthor


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "genre", "created_at", "updated_at")


@admin.register(ModAuthor)
class ModAuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "experience", "created_at", "updated_at")


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    list_display = ("name", "game", "author", "created_at", "updated_at")