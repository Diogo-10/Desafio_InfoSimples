import requests
from bs4 import BeautifulSoup
import json

def extrair_dados_principais(dados_pagina):
    """Extrai os campos mais importantes"""
    produto = {
        "titulo": dados_pagina.find('h2', id='product_title').text.strip(),
        "marca": dados_pagina.find('div', class_='brand').text.strip(),
        "categorias": [link.text.strip() for link in dados_pagina.select('nav.current-category a')[1:-1]],
        "descricao": "\n".join(p.text.strip() for p in dados_pagina.find('div', class_='proddet').find_all('p'))
    }
    return produto

def extrair_precos(dados_pagina):
    """Extrai informações de preço"""
    card = dados_pagina.find('div', class_='card selected')
    return {
        "preco_atual": float(card.find('div', class_='prod-pnow').text.replace('R$','').replace(',','.').strip()),
        "preco_antigo": float(card.find('div', class_='prod-pold').text.replace('R$','').replace(',','.').strip()),
        "disponivel": True
    }

def extrair_propriedades(dados_pagina):
    """Extrai as propriedades do produto no seu estilo"""
    propriedades = []
    
    # Encontra todas as tabelas de propriedades
    tabelas = dados_pagina.find_all('table', class_='pure-table')
    
    for tabela in tabelas:
        # Pega todas as linhas da tabela (ignorando o cabeçalho se existir)
        for linha in tabela.find_all('tr'):
            celulas = linha.find_all('td')
            if len(celulas) == 2:  # Garante que é uma linha válida com 2 colunas
                propriedade = {
                    "nome": celulas[0].text.strip(),
                    "valor": celulas[1].text.strip()
                }
                propriedades.append(propriedade)
    
    return propriedades

# --- Execução principal ---
try:
    # 1° Etapa: Requisição HTTP
    resposta = requests.get('https://infosimples.com/vagas/desafio/commercia/product.html')
    resposta.raise_for_status()
    
    # 2° Etapa: Parsear HTML
    dados_pagina = BeautifulSoup(resposta.text, 'html.parser')
    
    # 3° Etapa: Extrair dados
    dados_produto = extrair_dados_principais(dados_pagina)
    dados_produto.update(extrair_precos(dados_pagina))
    dados_produto["propriedades"] = extrair_propriedades(dados_pagina)  # Adiciona as propriedades
    
    # 4° Etapa: Salvar JSON
    with open('produto_final.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados_produto, arquivo, ensure_ascii=False, indent=2)
    
    print("Dados salvos em 'produto_final.json'!")

except Exception as erro:
    print(f"Erro: {erro}")