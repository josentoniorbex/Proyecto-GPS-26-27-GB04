"""Configuración común de las pruebas.

Cada prueba usa una base de datos temporal nueva, así nunca toca la tuya.
"""
import pytest

from app import create_app


@pytest.fixture
def app(tmp_path):
    return create_app({
        "TESTING": True,
        "DATABASE": str(tmp_path / "pruebas.sqlite"),
        # Las pruebas envían formularios sin token; la protección CSRF se prueba en test_csrf.py
        "WTF_CSRF_ENABLED": False,
    })


@pytest.fixture
def client(app):
    """Navegador simulado para hacer peticiones a la web."""
    return app.test_client()
