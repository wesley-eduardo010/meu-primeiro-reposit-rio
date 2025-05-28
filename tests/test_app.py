from app import saudacao

def test_saudacao_retorna_string_formatada():
    assert saudacao("João") == "Olá, João!"

def test_saudacao_vazia():
    # Quando o nome é string vazia, retorna "Olá, !"
    assert saudacao("") == "Olá, !"