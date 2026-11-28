"""Protección CSRF: un formulario enviado sin token se rechaza."""
import pytest

from app import create_app


@pytest.fixture
def app_con_csrf(tmp_path):
    return create_app({
        "TESTING": True,
        "DATABASE": str(tmp_path / "pruebas.sqlite"),
        "WTF_CSRF_ENABLED": True,
    })


def test_un_post_sin_token_csrf_se_rechaza(app_con_csrf):
    respuesta = app_con_csrf.test_client().post("/contacto", data={"nombre": "Frodo"})
    assert respuesta.status_code == 400


def test_los_formularios_incluyen_el_token_csrf(app_con_csrf):
    respuesta = app_con_csrf.test_client().get("/contacto")
    assert b'name="csrf_token"' in respuesta.data
