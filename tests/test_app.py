from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get(
        '/'
    )  # Act (Fase de Ação, que executa algo no código, literalmente o teste.)

    assert (
        response.status_code == HTTPStatus.OK
    )  # Assert = Garantindo, ou seja afirmando que o status é o que esperamos.
    assert response.json() == {
        'message': 'Olá Mundo!'
    }  # Assert = Garantindo que a mensagem é a esperada na saída.
