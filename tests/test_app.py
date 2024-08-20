from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  # Arrange (Organização do teste)
    # O Client agora é passado como parametro

    response = client.get(
        '/'
    )  # Act (Fase de Ação, que executa algo no código, literalmente o teste.)

    assert (
        response.status_code == HTTPStatus.OK
    )  # Assert = Garantindo, ou seja afirmando que o status é o que esperamos.
    assert response.json() == {
        'message': 'Olá Mundo!'
    }  # Assert = Garantindo que a mensagem é a esperada na saída.


def test_create_user(client):
    # client = TestClient(app)  # Arrange (Organização do teste)
    # O Client agora é passado como parametro

    # Act (Fase de Ação, que executa algo no código, literalmente o teste.)
    response = client.post(
        '/users/',
        json={  # Enviando os dados do model UserShema
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    # Assert = Garantindo, ou seja afirmando que o status é o que esperamos.
    assert response.status_code == HTTPStatus.CREATED
    # Neste ponto valida os dados do model UserPublic, que é o retorno da ação
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):  # Arrange passado como parametro fixture conftest
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_user_invalid(client):
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'teste123987',
            'username': 'testusername2',
            'email': 'testuser2@test.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'testuser2@test.com',
        'id': 1,
    }


def test_update_user_invalid(client):
    response = client.put(
        '/users/0',
        json={
            'password': 'teste123987',
            'username': 'testusername2',
            'email': 'testuser2@test.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User 1 Deleted'}


def test_delete_user_invalid(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
