import secrets

jwt_secret_key = secrets.token_hex(32)
print(f"JWT Secret Key: {jwt_secret_key}")