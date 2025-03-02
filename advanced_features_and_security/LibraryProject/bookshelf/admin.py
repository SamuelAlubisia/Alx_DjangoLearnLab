from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)

def create_groups_and_permissions():
    permission_names = ['can_view', 'can_create', 'can_edit', 'can_delete']
    book_content_type = ContentType.objects.get_for_model(Book)

    for perm_name in permission_names:
        Permission.objects.get_or_create(
            codename=perm_name,
            name=f'Can {perm_name.split("_")[1]} book',
            content_type=book_content_type
        )

    editors_group, _ = Group.objects.get_or_create(name='Editors')
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    viewers_group.permissions.set([can_view])
    editors_group.permissions.set([can_view, can_create, can_edit])
    admins_group.permissions.set([can_view, can_create, can_edit, can_delete])

create_groups_and_permissions()
