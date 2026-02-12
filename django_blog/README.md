Blog Post Management Features
Features Implemented

Full CRUD functionality using class-based views

Authentication-based access control

Author-only edit/delete permissions

Secure form handling with CSRF protection

Automatic author assignment

How to Use

Visit /posts/ to see all blog posts.

Log in to create a new post.

Authors can edit or delete their own posts.

Unauthorized users cannot modify posts.

Security Notes

Passwords handled via Django hashing

CSRF tokens included in all forms

Author validation enforced at view level