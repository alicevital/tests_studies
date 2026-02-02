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
def test_token_validation():
    token = user_register("artur", "23456")

    decoded = jwt.decode(
        token,
        CHAVE,
        algorithms=[ALGORITMO]
    )

    assert decoded["user"] == "artur"
    assert decoded["password"] == "23456"


@pytest.mark.unit
def test_user_register_jwt():
    '''
    testa se houve modificação no payload ou chave do token
    '''
    token = user_register("Jose", "123")

    headers_b64, payload_b64, signature = token.split(".") #diivde o token
 
    payload_b = base64.urlsafe_b64decode(payload_b64 + '==') #decodificando o payload
    payload = json.loads(payload_b)
 
    payload['user']= "Lucas" #modifica o payload
 
    new_payload_b64 = base64.urlsafe_b64encode( #remonta o token
        json.dumps(payload).encode()
    ).decode().rstrip("=")


    with pytest.raises(jwt.InvalidSignatureError):
        '''
            Se cair nessa exceção, o teste passa, pois significa que foi identificada a alteração
        '''
        jwt.decode(f"{headers_b64}.{new_payload_b64}.{signature}", CHAVE, ALGORITMO)