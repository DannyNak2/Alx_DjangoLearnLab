# Permissions and Groups Setup

## Permissions
Custom permissions have been added to the `Book` model:
- can_view: Allows viewing book entries.
- can_create: Allows creating new book entries.
- can_edit: Allows editing existing book entries.
- can_delete: Allows deleting book entries.

## Groups
The following groups have been created:
- Editors: Can create and edit books.
- Viewers: Can view books.
- Admins: Can view, create, edit, and delete books.

## Usage
The views in `relationship_app/views.py` enforce these permissions using the `@permission_required` decorator.
