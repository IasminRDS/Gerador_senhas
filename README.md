# 🔐 Gerador de Senhas

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
[![testes](https://github.com/IasminRDS/Gerador_senhas/actions/workflows/ci.yml/badge.svg)](https://github.com/IasminRDS/Gerador_senhas/actions/workflows/ci.yml)
![License](https://img.shields.io/badge/licença-MIT-blue)

Gera senhas aleatórias e seguras usando o módulo `secrets` (criptograficamente seguro), com **medidor de força** baseado em entropia.

## ✨ Funcionalidades

- 📏 Tamanho personalizável
- 🔤 Escolha de maiúsculas, números e símbolos
- 🚫 Opção de **excluir caracteres ambíguos** (`I`, `l`, `1`, `O`, `0`)
- 🔢 Geração de **várias senhas** de uma vez
- 📊 **Cálculo de entropia** (em bits) e classificação de força
- 🔒 Usa `secrets` em vez de `random` — adequado para segurança

## 🚀 Como executar

```bash
python main.py
```

## 🧪 Testes

```bash
python -m unittest -v
```

## 📁 Estrutura

```
gerador-senhas/
├── main.py             # Interface de linha de comando
├── gerador.py          # Lógica de geração e cálculo de força
└── test_gerador.py     # Testes automatizados
```

## 💡 Conceitos demonstrados

- Geração segura de aleatoriedade (`secrets`)
- Cálculo de entropia: `bits = tamanho × log₂(nº de caracteres possíveis)`
- Funções com argumentos nomeados (`**kwargs`) e testes

## 📄 Licença

MIT — veja [LICENSE](./LICENSE).

---

Feito por **Iasmin Ribeiro de Souza** · [LinkedIn](https://www.linkedin.com/in/iasmin-ribeiro-de-souza-033536401) · [GitHub](https://github.com/IasminRDS)
