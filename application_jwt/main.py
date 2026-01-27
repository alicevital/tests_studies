import jwt

CHAVE = "SECRETA"
ALGORITMO = "HS256"

users = {}

def user_register(username, password):
    '''
        Registra user e gera token jwt
    '''
    token_jwt = jwt.encode({"user": username, "password": password}, CHAVE, algorithm=ALGORITMO)

    users[username] = token_jwt

    return token_jwt

print(user_register("ALICE", "123@a"))