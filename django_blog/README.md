# Django Blog - Post Management Features

## Features:
1. **Create, Read, Update, Delete (CRUD)** blog posts.
2. **User authentication**: Only authors can modify their posts.
3. **Permissions**:
   - All users can read posts.
   - Only authors can edit or delete their posts.
4. **Navigation**:
   - `/` → List all posts
   - `/posts/new/` → Create a new post
   - `/posts/<id>/` → View a single post
   - `/posts/<id>/edit/` → Edit a post (author only)
   - `/posts/<id>/delete/` → Delete a post (author only)

Run the server:
```bash
python manage.py runserver
