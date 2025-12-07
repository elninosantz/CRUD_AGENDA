def limpar_texto(texto:str) -> str:
    """
    - Padroniza texto do tipo string.
    - Remove espaços em branco causados por erros de digitação.
    - Converte o texto para minúsculas usando o método lower. Para evitar futuros erros de variação de digitação.


    Args:
         texto (str): Texto informado pelo usuário.

    Returns:
         str: Texto padronizado.
    """

    texto = texto.strip()
    texto_limpo = texto.lower()
    return texto_limpo


