import csv

# Arquivos de entrada
softwares_csv = "docs/assets/data/softwares.csv"
conda_csv = "docs/assets/data/conda.csv"

# Arquivo de saída Markdown
md_file = "docs/softwares/index_softwares.md"


def gerar_tabela(caminho_csv, eh_conda=False):
    tabela = []
    
    # Define a chave da coluna e o cabeçalho da tabela dinamicamente
    coluna_nome = "ambiente" if eh_conda else "programa"
    titulo_coluna = "Ambiente" if eh_conda else "Programa"
    
    tabela.append(f"| {titulo_coluna} | Versão | Descrição | Repositório |")
    tabela.append("|----------|:------:|-----------|:-----------:|")

    with open(caminho_csv, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Busca pelo nome da coluna ('ambiente' ou 'programa'), com fallback seguro
            item_nome = row.get(coluna_nome, "").strip() or row.get("programa", "").strip() or row.get("ambiente", "").strip()

            # Ignora linhas vazias ou títulos de seção soltos
            if not item_nome or "###" in item_nome:
                continue

            versao = row.get("versao", "").strip() or "-"
            descricao = row.get("descricao", "").strip() or "-"

            # Formata o repositório como link Markdown com abertura em nova aba
            repo_url = row.get("repositorio", "").strip()
            if repo_url and repo_url.startswith("http"):
                repositorio = f'[:material-github: Link]({repo_url}){{ target="_blank" rel="noopener" }}'
            elif repo_url:
                repositorio = repo_url
            else:
                repositorio = "-"

            tabela.append(
                f"| **{item_nome}** | {versao} | {descricao} | {repositorio} |"
            )

    return "\n".join(tabela)


# Gera o conteúdo de ambas as tabelas
tabela_softwares = gerar_tabela(softwares_csv, eh_conda=False)
tabela_conda = gerar_tabela(conda_csv, eh_conda=True)

# Monta o arquivo Markdown completo
conteudo = f"""# __Softwares__

Nesta página estão listados os softwares atualmente disponíveis globalmente no servidor do LGBio.

!!! note "Solicitação de Softwares"

    Caso necessite de um software que não esteja disponível nesta lista, solicite a instalação através do formulário disponível na página inicial.

{tabela_softwares}

<br>

# __Ambientes Conda__
{tabela_conda}

<p align="right">
    <img src="assets/images/eecbio_menor.png" alt="INCT EECBio" width="150">
</p>

<p style="text-align: center; font-size: 0.8em; color: var(--md-default-fg-color--light);">
© 2026 • LGBio • Universidade Federal de Goiás
</p>
"""

# Salva o arquivo .md final em UTF-8
with open(md_file, "w", encoding="utf-8") as file:
    file.write(conteudo)

print("Página de Softwares e Ambientes Conda atualizada com sucesso!")