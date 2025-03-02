# Django Permissions and Groups Setup

## Custom Permissions
- Added custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) to the `Book` model.

## Groups and Roles
- Created the following groups:
  - **Viewers:** Can only view books.
  - **Editors:** Can view, create, and edit books.
  - **Admins:** Can perform all actions.

## Views Protection
- Used `@permission_required` decorators to enforce permissions:
  - `book_list` view requires `can_view`.
  - `create_book` view requires `can_create`.
  - `edit_book` view requires `can_edit`.
  - `delete_book` view requires `can_delete`.

## Testing
- Create test users and assign them to different groups via the admin panel.
- Test access for each user based on their group.

