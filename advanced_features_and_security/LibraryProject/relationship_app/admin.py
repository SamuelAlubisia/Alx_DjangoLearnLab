from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Author, Book, Library, Librarian  # Removed CustomUser import

# Removed CustomUserAdmin class and CustomUser registration
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# Keep the group and permission setup if needed
def setup_groups_and_permissions():
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    book_content_type = ContentType.objects.get_for_model(Book)

    permissions = [
        ('can_add_book', 'Can add a new book'),
        ('can_change_book', 'Can edit book details'),
        ('can_delete_book', 'Can delete a book'),
        ('can_view_book', 'Can view book details'),
    ]

    for codename, name in permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            name=name,
            content_type=book_content_type
        )

        if codename in ['can_add_book', 'can_change_book']:
            editors_group.permissions.add(permission)
        if codename in ['can_view_book']:
            viewers_group.permissions.add(permission)
        if codename in ['can_add_book', 'can_change_book', 'can_delete_book', 'can_view_book']:
            admins_group.permissions.add(permission)

setup_groups_and_permissions()

