import hashlib

USERS_DB = {
    "admin": {
        "password_hash": hashlib.sha256("secreto123".encode()).hexdigest(),
        "role": "administrator"
    },
    "usuario1": {
        "password_hash": hashlib.sha256("mi_password".encode()).hexdigest(),
        "role": "user"
    }
}

def _hash_password(password: str) -> str:
    """Función auxiliar para generar el hash SHA-256 de una contraseña."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_credentials(username: str, password_input: str) -> bool:
    """
    Valida las credenciales de un usuario comparando el hash de la contraseña ingresada.
    
    Args:
        username (str): El nombre de usuario.
        password_input (str): La contraseña en texto plano ingresada.
        
    Returns:
        bool: True si las credenciales son correctas, False en caso contrario.
    """
    # 1. Verificar si el usuario existe en el sistema
    if username not in USERS_DB:
        return False
    
    # 2. Obtener el hash almacenado
    stored_hash = USERS_DB[username]["password_hash"]
    
    # 3. Hashear la contraseña ingresada para compararla de forma segura
    input_hash = _hash_password(password_input)
    
    # 4. Retornar el resultado de la comparación
    return stored_hash == input_hash


if __name__ == "__main__":
    # Pruebas rápidas para comprobar el funcionamiento
    print("--- Probando auth_service.py ---")
    
    # Prueba 1: Credenciales correctas
    print("Login admin (correcto):", validate_credentials("admin", "secreto123")) 
    # Resultado esperado: True
    
    # Prueba 2: Contraseña incorrecta
    print("Login admin (incorrecto):", validate_credentials("admin", "clave_falsa")) 
    # Resultado esperado: False
    
    # Prueba 3: Usuario que no existe
    print("Login usuario inexistente:", validate_credentials("invitado", "secreto123")) 
    # Resultado esperado: False
