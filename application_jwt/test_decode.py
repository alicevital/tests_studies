import pytest
import jwt
import json
import base64
from main import user_register, users
from main import CHAVE, ALGORITMO

user_register("Alice", "12345")

@pytest.mark.unit
def test_validation_users():
    '''
        Testar se o dict está vazio
    '''
    assert len(users) > 0

@pytest.mark.unit
def test_user_decode_jwt():

    token = user_register("ALICE", "EMILY")

    headers_b64, payload_b64, signature = token.split(".")
    payload_b = base64.urlsafe_b64decode(payload_b64 + '==')
    payload = json.loads(payload_b)

    payload["user"] = "EU"
    payload["password"] = "AQUI"

    new_payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
    print(new_payload_b64)
    print("_______")
    print(token)

    assert new_payload_b64 != token

@pytest.mark.unit
def test_user_register_jwt():
    '''
    testa se houve modificação no payload ou chave do token
    '''
    token = user_register("Alice", "123")

    headers_b64, payload_b64, signature = token.split(".")
 
    payload_b = base64.urlsafe_b64decode(payload_b64 + '==')
    payload = json.loads(payload_b)
 
    payload['user']= "AAAA"
 
    new_payload_b64 = base64.urlsafe_b64encode(
        json.dumps(payload).encode()
    ).decode().rstrip("=")

    with pytest.raises(jwt.InvalidSignatureError):
        '''
            Se cair nessa exceção, o teste passa, pois significa que foi identificada a alteração
        '''
        jwt.decode(f"{headers_b64}.{new_payload_b64}.{signature}", CHAVE, ALGORITMO)