
import csv

# Arquivos de entrada
bd_csv = "docs/assets/data/bd.csv"

# Arquivo de saída Markdown
md_file = "docs/index_bancos_de_dados.md"


def gerar_tabela(caminho_csv):
    tabela = []

    # Define as colunas e seus títulos
    coluna_nome = "banco"
    titulo_coluna = "Banco de Dados"

    coluna_data = "data"
    titulo_data = "Última atualização"

    tabela.append(
        f"| {titulo_coluna} | {titulo_data} | Descrição | Repositório |"
    )
    tabela.append("|:---|:---:|:---|:---:|")

    with open(caminho_csv, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Busca os valores nas respectivas colunas
            item_nome = row.get(coluna_nome, "").strip()
            item_data = row.get(coluna_data, "").strip()

            # Ignora linhas vazias ou títulos de seção
            if not item_nome or "###" in item_nome:
                continue

            descricao = row.get("descricao", "").strip() or "-"

            # Formata o repositório como link Markdown
            repo_url = row.get("repositorio", "").strip()

            if repo_url.startswith("http"):
                repositorio = (
                    f'[:material-github: Link]({repo_url})'
                    '{ target="_blank" rel="noopener" }'
                )
            elif repo_url:
                repositorio = repo_url
            else:
                repositorio = "-"

            tabela.append(
                f"| **{item_nome}** | {item_data or '-'} | "
                f"{descricao} | {repositorio} |"
            )

    return "\n".join(tabela)


# Gera a tabela
tabela_bd = gerar_tabela(bd_csv)


# Monta o arquivo Markdown completo
conteudo = f"""# __Bancos de Dados__

Nesta página estão listados os bancos de dados atualmente disponíveis globalmente no servidor do LGBio.

!!! note "Solicitação de novos bancos de dados"

    Caso necessite de um banco de dados padrão que não esteja disponível nesta lista, solicite sua instalação por meio do formulário disponível na página inicial. Se desejar disponibilizar um banco de dados customizado para todos os usuários do servidor, entre em contato com os administradores pela aba "Contato".

{tabela_bd}

<br>

<p align="right">
    <img src="assets/images/eecbio_menor.png" alt="INCT EECBio" width="150">
</p>

<p style="text-align: center; font-size: 0.8em; color: var(--md-default-fg-color--light);">
© 2026 • LGBio • Universidade Federal de Goiás
</p>
"""


# Salva o arquivo Markdown em UTF-8
with open(md_file, "w", encoding="utf-8") as file:
    file.write(conteudo)

print("Página de Bancos de Dados atualizada com sucesso!")
