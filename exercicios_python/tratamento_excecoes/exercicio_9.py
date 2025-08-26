"""
Exercício 9: Exceções Personalizadas

Crie sua própria exceção chamada `IdadeInvalidaError`. Escreva uma função que receba uma idade e lance `IdadeInvalidaError` se a idade for negativa ou maior que 120.
"""

class IdadeInvalidaError(Exception):
    """Exceção lançada para idades inválidas."""
    pass

def validar_idade(idade):
    # Escreva seu código aqui
    pass

# Exemplo de uso
try:
    validar_idade(25)
    validar_idade(-5)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")

try:
    validar_idade(150)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")