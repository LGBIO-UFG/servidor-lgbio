import csv

# Arquivos de entrada
softwares_csv = "docs/assets/data/softwares.csv"
conda_csv = "docs/assets/data/conda.csv"

# Arquivo de saída Markdown
md_file = "docs/softwares/index_softwares.md"


def gerar_tabela(caminho_csv):
    tabela = []
    tabela.append("| Programa | Versão | Descrição | Repositório |")
    tabela.append("|----------|:------:|-----------|:-----------:|")

    with open(caminho_csv, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            programa = row.get("programa", "").strip()

            # Ignora linhas vazias ou títulos de seção soltos
            if not programa or "###" in programa:
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
                f"| **{programa}** | {versao} | {descricao} | {repositorio} |"
            )

    return "\n".join(tabela)


# Gera o conteúdo de ambas as tabelas
tabela_softwares = gerar_tabela(softwares_csv)
tabela_conda = gerar_tabela(conda_csv)

# Monta o arquivo Markdown completo
conteudo = f"""# __Softwares__

Nesta página estão listados os softwares atualmente disponíveis globalmente no servidor do LGBio.

!!! note "Solicitação de Softwares"

    Caso necessite de um software que não esteja disponível nesta lista, solicite a instalação através do formulário disponível na página inicial.

{tabela_softwares}

<br>

# __Ambientes Conda__
{tabela_conda}
"""

# Salva o arquivo .md final em UTF-8
with open(md_file, "w", encoding="utf-8") as file:
    file.write(conteudo)

print("Página de Softwares e Ambientes Conda atualizada com sucesso!")