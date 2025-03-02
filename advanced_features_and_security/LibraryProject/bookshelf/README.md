# Permissions and Groups in Django

## 1. Custom Permissions
- Defined in `Book` model:
  - `can_view`: View books.
  - `can_create`: Create books.
  - `can_edit`: Edit books.
  - `can_delete`: Delete books.

## 2. Groups and Permissions
- Created groups:
  - `Viewers`: Can view books only.
  - `Editors`: Can view, create, and edit books.
  - `Admins`: Full access to all actions.
- Groups and permissions are automatically created in `admin.py`.

## 3. Permission Checks in Views
- Used `@permission_required` decorators:
  - Protects views based on permissions.
- `raise_exception=True` for 403 errors if unauthorized.

## 4. Testing
- Create test users and assign to groups.
- Verify access to various URLs based on permissions.

## 5. Key Files
- `models.py`: Custom permissions.
- `admin.py`: Group setup.
- `views.py`: Permission checks.
