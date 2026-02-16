from django.contrib import admin
from django.utils.html import format_html
from .models import BannerImages, Clients, Services, Projects


@admin.register(BannerImages)
class BannerImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')
    readonly_fields = ('image_preview',)
    ordering = ('-id',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Preview"



@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'name')
    search_fields = ('name',)
    readonly_fields = ('image_preview',)
    ordering = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;border-radius:50%;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Logo"





@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'short_description')
    search_fields = ('title',)
    list_filter = ('title',)
    readonly_fields = ('image_preview',)
    ordering = ('title',)

    def short_description(self, obj):
        return obj.description[:60] + "..."
    short_description.short_description = "Description"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;border-radius:8px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Image"





@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'short_description')
    search_fields = ('title',)
    list_filter = ('title',)
    readonly_fields = ('image_preview',)
    ordering = ('-id',)

    def short_description(self, obj):
        return obj.description[:60] + "..."
    short_description.short_description = "Description"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:50px;border-radius:8px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Image"



