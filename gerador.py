"""
Lógica do gerador de senhas seguras.
Usa o módulo `secrets` (criptograficamente seguro).
"""

import math
import secrets
import string

CARACTERES_AMBIGUOS = "Il1O0"
SIMBOLOS = "!@#$%&*?-_+="


def construir_alfabeto(maiusculas=True, numeros=True, simbolos=True, sem_ambiguos=False):
    alfabeto = string.ascii_lowercase
    if maiusculas:
        alfabeto += string.ascii_uppercase
    if numeros:
        alfabeto += string.digits
    if simbolos:
        alfabeto += SIMBOLOS

    if sem_ambiguos:
        alfabeto = "".join(c for c in alfabeto if c not in CARACTERES_AMBIGUOS)

    return alfabeto


def gerar_senha(tamanho=12, **opcoes):
    alfabeto = construir_alfabeto(**opcoes)
    if not alfabeto:
        raise ValueError("Nenhum conjunto de caracteres selecionado.")
    return "".join(secrets.choice(alfabeto) for _ in range(tamanho))


def calcular_entropia(tamanho, tamanho_alfabeto):
    """Entropia em bits: mede a imprevisibilidade da senha."""
    if tamanho_alfabeto <= 1:
        return 0.0
    return tamanho * math.log2(tamanho_alfabeto)


def classificar_forca(entropia):
    if entropia < 40:
        return "Fraca 🔴"
    if entropia < 60:
        return "Média 🟡"
    if entropia < 80:
        return "Forte 🟢"
    return "Muito forte 🔵"
