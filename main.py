"""
Interface de linha de comando do gerador de senhas.
"""

from gerador import (
    calcular_entropia,
    classificar_forca,
    construir_alfabeto,
    gerar_senha,
)


def perguntar_sim_nao(mensagem, padrao=True):
    sufixo = "(S/n)" if padrao else "(s/N)"
    resposta = input(f"  {mensagem} {sufixo}: ").strip().lower()
    if not resposta:
        return padrao
    return resposta == "s"


def ler_int(mensagem, padrao):
    try:
        return int(input(f"  {mensagem} (padrão {padrao}): ") or padrao)
    except ValueError:
        return padrao


def main():
    print("===== GERADOR DE SENHAS =====")

    tamanho = max(ler_int("Tamanho da senha", 16), 4)
    quantidade = max(ler_int("Quantas senhas gerar", 1), 1)

    opcoes = {
        "maiusculas": perguntar_sim_nao("Incluir letras maiúsculas?"),
        "numeros": perguntar_sim_nao("Incluir números?"),
        "simbolos": perguntar_sim_nao("Incluir símbolos?"),
        "sem_ambiguos": perguntar_sim_nao("Excluir caracteres ambíguos (I, l, 1, O, 0)?", padrao=False),
    }

    try:
        senhas = [gerar_senha(tamanho, **opcoes) for _ in range(quantidade)]
    except ValueError as erro:
        print(f"\n❌ {erro}")
        return

    tamanho_alfabeto = len(construir_alfabeto(**opcoes))
    entropia = calcular_entropia(tamanho, tamanho_alfabeto)

    print("\n----- SENHAS GERADAS -----")
    for senha in senhas:
        print(f"  {senha}")

    print(f"\n  Entropia: {entropia:.0f} bits")
    print(f"  Força:    {classificar_forca(entropia)}")


if __name__ == "__main__":
    main()
