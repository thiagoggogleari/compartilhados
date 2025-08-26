"""
Exercício 8: Lançando Exceções

Escreva uma função que valide uma senha. A função deve receber uma senha como parâmetro e lançar uma exceção `ValueError` se a senha tiver menos de 8 caracteres.
"""

def validar_senha(senha):
    # Escreva seu código aqui
    pass

# Exemplo de uso
try:
    validar_senha("senha123")
    validar_senha("curta")
except ValueError as e:
    print(f"Erro de validação: {e}")