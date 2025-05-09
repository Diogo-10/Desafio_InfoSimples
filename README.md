# Desafio InfoSimples

Este projeto é uma solução para o desafio técnico proposto pela empresa InfoSimples. O objetivo principal é realizar web scraping em uma página de produto, extrair informações estruturadas e salvar os dados em um arquivo JSON conforme especificação.

## ✅ Funcionalidades Implementadas

- Requisição HTTP GET para a página do produto.
- Parseamento do HTML com `BeautifulSoup`.
- Extração dos seguintes dados:
  - `title` (título do produto)
  - `brand` (marca)
  - `categories` (categorias do produto)
  - `description` (descrição do produto)
  - `skus` (preço atual, antigo e disponibilidade)
  - `properties` (tabela de características)
- Salvamento das informações no arquivo `produto_final.json`.

## ⚠️ Funcionalidade Não Implementada

- A extração de dados da seção `reviews` (avaliações dos usuários) e o cálculo de `reviews_average_score`  **não foram desenvolvidos** pois atualmente não tenho experiência ou conhecimento suficiente para realizar essa tarefa. Estes pontos seriam priorizados em uma próxima iteração.

## 🧰 Tecnologias Utilizadas

- **Python 3.x**
- **[requests](https://pypi.org/project/requests/)** — para fazer requisições HTTP
- **[BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)** — para parsear e navegar pelo HTML
- **json** — para manipulação e escrita dos dados no formato estruturado

## 📁 Estrutura do Projeto

```bash
Desafio_InfoSimples/
├── infoSimples.py          # Script principal com a lógica de extração e salvamento
├── produto_final.json      # Arquivo de saída com os dados estruturados
└── README.md               # Documentação do projeto
```

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Instale as dependências necessárias:

   ```bash
   pip install requests beautifulsoup4
   ```

3. Clone este repositório:

   ```bash
   git clone https://github.com/Diogo-10/Desafio_InfoSimples.git
   cd Desafio_InfoSimples
   ```

4. Execute o script:

   ```bash
   python infoSimples.py
   ```

5. O arquivo `produto_final.json` será gerado na pasta do projeto.

## 📌 Observações

- O HTML analisado vem da seguinte URL:  
  `https://infosimples.com/vagas/desafio/commercia/product.html`
- O projeto foi desenvolvido com foco em clareza e aderência aos requisitos da estrutura JSON fornecida.

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
