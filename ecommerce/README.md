# E-Commerce Backend - ProDev BE

## Project Objectives

This project aims to develop a robust backend for an e-commerce product catalog. It simulates a real-world backend development environment and focuses on:

* **Full management of products and categories** (CRUD).
* **Secure user authentication** using JWT.
* **Efficient product discovery** through filtering, sorting, and pagination.
* **Database performance and optimization** with PostgreSQL.
* **API documentation** to facilitate frontend integration.
* **Commit tracking and Git workflow**, documented in `docs/`.

## Technologies Used

* **Django**: Backend web framework for application structure and logic.
* **Django REST Framework (DRF)**: For building RESTful APIs.
* **PostgreSQL**: High-performance relational database.
* **JWT (JSON Web Tokens)**: For secure user authentication.
* **Swagger / OpenAPI**: For documenting and testing APIs.
* **Docker & Docker Compose**: To simplify local and production deployment.
* **GitHub Actions**: For CI/CD and automatic test execution.
* **Render**: Cloud platform for hosting and deploying the backend application.

## Project Structure

```text
ecommerce/
│
├─ ecommerce/             # Django configuration (settings, urls, wsgi)
├─ products/              # Django app for product management
│  ├─ migrations/
│  ├─ models.py
│  ├─ serializers.py
│  └─ views.py
├─ categories/            # Django app for categories
│  ├─ migrations/
│  ├─ models.py
│  ├─ serializers.py
│  └─ views.py
├─ users/                 # Django app for user management
│  ├─ migrations/
│  ├─ models.py
│  ├─ serializers.py
│  └─ views.py
├─ docs/                  # Documentation of important commits and Git workflow
├─ manage.py
└─ README.md
```

## Main Features

1. **CRUD Operations**

   * Full management of products and categories.
   * User management with JWT: registration, login, refresh token.

2. **Advanced API Features**

   * **Filtering**: filter products by category.
   * **Sorting**: sort products by price or creation date.
   * **Pagination**: paginated responses for large sets of products.
   * **Search**: search products by title or description.

3. **Documentation**

   * Swagger/OpenAPI for testing and documenting all API routes.
   * Commit and Git workflow documentation available in `docs/`.

4. **Testing and Quality**

   * Unit and integration tests for product endpoints.
   * Query optimization using PostgreSQL indexes.
   * Detailed Git workflow with descriptive commits (docs/commits.md).

5. **Deployment**

   * Local deployment via Docker and Docker Compose.
   * Production deployment hosted on **Render**.
   * CI/CD using GitHub Actions for automated tests.

## Instructions to Run the Project Locally

1. **Clone the repository**

```bash
git clone https://github.com/AudiaOlwa/alx-project-nexus.git
cd alx-project-nexus/ecommerce
```

2. **Create a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

3. **Configure PostgreSQL database**

* Create a database and update `settings.py` or `.env` with your credentials.

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the server locally**

```bash
python manage.py runserver
```

6. **Access the API and documentation**

* Local API: `http://127.0.0.1:8000/api/`
* Swagger UI: `http://127.0.0.1:8000/api/docs/`
* Redoc UI: `http://127.0.0.1:8000/api/redoc/`
* Production API (Render): `https://alx-project-nexus-h1nh.onrender.com/api/`

7. **Git Workflow and Commits**

* Check the `docs/` folder for detailed instructions on the Git workflow and important commits.

---

This README provides a comprehensive guide for understanding, using, and contributing to your E-Commerce Backend project, with full documentation for developers and evaluators.
