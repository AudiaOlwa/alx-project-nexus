"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Registers ProductViewSet automatically under /api/products/
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
# Exposes schema and UI documentation for developers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.http import HttpResponse

def home_view(request):
    content = """
    <h1>ALX Ecommerce Project NEXUS</h1>
    <p>Successfully deployed with Render 🎉</p>

    <h2>Available API Endpoints</h2>

    <h3>📦 Products</h3>
    <ul>
        <li><a href="/api/products/">GET /api/products/</a> — List products</li>
        <li>/api/products/&lt;id&gt;/ — Retrieve, update, delete product</li>
        <li>Filtering: /api/products/?category=ID</li>
        <li>Search: /api/products/?search=keyword</li>
        <li>Ordering: /api/products/?ordering=price</li>
    </ul>

    <h3>📁 Categories</h3>
    <ul>
        <li><a href="/api/categories/">GET /api/categories/</a> — List categories</li>
        <li>/api/categories/&lt;id&gt;/ — Retrieve, update, delete category</li>
    </ul>

    <h3>🛠 Admin</h3>
    <ul>
        <li><a href="/admin/">/admin/</a></li>
    </ul>

    <h3>📚 API Documentation</h3>
    <ul>
        <li><a href="/api/schema/">/api/schema/</a> — OpenAPI schema (JSON/YAML)</li>
        <li><a href="/api/docs/">/api/docs/</a> — Swagger UI</li>
        <li><a href="/api/redoc/">/api/redoc/</a> — ReDoc documentation</li>
    </ul>

    <hr>
    <p>Backend Engineering — Project Nexus (ALX)</p>
    """
    return HttpResponse(content)

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    # Include authentication routes under /api/auth/
    path("api/auth/", include("users.urls")),
    path("api/", include(router.urls)),
    path("api/categories/", include("categories.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # raw schema
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # UI
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),  # Alternative UI
]

