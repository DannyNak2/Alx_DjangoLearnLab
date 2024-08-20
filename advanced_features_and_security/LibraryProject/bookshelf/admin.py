from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


# Create groups and assign permissions
def setup_groups():
    # Create groups
    editors_group, created = Group.objects.get_or_create(name='Editors')
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    admins_group, created = Group.objects.get_or_create(name='Admins')

    # Get permissions for the Book model
    content_type = ContentType.objects.get_for_model(Book)
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

    # Assign permissions to groups
    editors_group.permissions.set([can_create, can_edit])
    viewers_group.permissions.set([can_view])
    admins_group.permissions.set([can_view, can_create, can_edit, can_delete])

    # Optional: Register function to run on application start
    # setup_groups()

admin.site.register(Book)