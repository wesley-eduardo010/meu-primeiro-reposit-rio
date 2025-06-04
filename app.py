def saudacao(nome: str) -> str:
    """
    Retorna uma saudação simples para o nome informado.
    Exemplo: saudacao("Maria") -> "Olá, Maria!"
    """
    return f"Olá, {nome},  bom dia !"

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))