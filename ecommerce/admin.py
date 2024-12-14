


from django.contrib import admin
from django.utils.html import mark_safe
from .models import Product
from .models import Product, TipResource, TeamMember

# Customizing ProductAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_active', 'image_thumbnail')  # Display image thumbnail in list view
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'is_active')

    # Method to show a small thumbnail of the product image in the list view
    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return 'No image'
    image_thumbnail.short_description = 'Image'  # Set the column name for the thumbnail

    # Optional: Display image preview in the form view (useful if you're editing a product)
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Add a thumbnail preview for the image field in the form
        form.base_fields['image'].widget.attrs.update({'style': 'max-width: 200px;'})
        return form



@admin.register(TipResource)
class TipResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('title', 'content')  # Allow search by title and content
    list_filter = ('created_at',)  # Filter by creation date

    # Customize the form fields and display in the admin
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'health_benefits', 'image')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')  # Make created_at and updated_at readonly in admin


# Customizing TeamMemberAdmin
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'photo_thumbnail')  # Display name, role, and photo thumbnail in list view
    search_fields = ('name', 'role')  # Allow search by name and role

    # Method to show a small thumbnail of the team member photo in the list view
    def photo_thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />')
        return 'No photo'
    photo_thumbnail.short_description = 'Photo'  # Set the column name for the photo thumbnail



