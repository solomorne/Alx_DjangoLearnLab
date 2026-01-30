Authentication:
- Token-based authentication using DRF TokenAuthentication
- Tokens are obtained via POST /api/token/

Permissions:
- All endpoints require authentication
- BookList: accessible to authenticated users
- BookViewSet: restricted to admin users only
