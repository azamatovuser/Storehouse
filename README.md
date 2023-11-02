# Storehouse
~~~
PATCH 0.0.2
~~~
**API**

- /product/place_list/ --> GET
  - List of all places
- /product/place/place_id/storehouse/ --> GET
  - Filtering all storehouse data by place
~~~
PATCH 0.0.1
~~~
***Models***
- Added Place model
  - To filter stuffs by place
- Added Category model
  - to manage stuffs by category
- Added Product model
  - to add data about product
- Added Storehouse model
  - to manage product and give data about quantity, place and account

***Admin panel***
- Category
  - List of all categories
- Place
  - List of all places
- Product
  - List of all products
  - Filtering by category and Is_active
- Storehouse
  - Filtering by place and account
  - List of all storehouse data


~~~
INITIAL COMMIT
~~~
**Models**
- Custom user

**API**
- All account list
- CRUD account
- JSON Web Token

**Unit tests**

Tests for all account's APIs