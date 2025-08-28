"""
Exercício 8: Lançando Exceções

Escreva uma função que valide uma senha.
A função deve receber uma senha como parâmetro e lançar uma exceção `ValueError` se a senha tiver menos de 8 caracteres.
"""

def validar_senha(senha):
    if len(senha) < 8:
        raise ValueError ("\nSenha deve ter no mínimo 8 caracteres")
    else:
        print("Senha validada.")
# Exemplo de uso
try:
    validar_senha("senha123")
    validar_senha("curta")
except ValueError as e:
    print(f"Erro de validação: {e}")