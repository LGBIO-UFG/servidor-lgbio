import csv


csv_file = "docs/assets/data/softwares.csv"
md_file = "docs/softwares/index_softwares.md"


with open(csv_file) as file:
    reader = csv.DictReader(file)
    softwares = list(reader)


tabela = []

tabela.append("| Programa | Versão | Descrição |")
tabela.append("|----------|:------:|-----------|")


for software in softwares:
    tabela.append(
        f"| {software['programa']} | "
        f"{software['versao']} | "
        f"{software['descricao']} |"
    )


conteudo = f"""# __Softwares__

Nesta página estão listados os softwares atualmente disponíveis no servidor.

---

{"\n".join(tabela)}

!!! note

    Caso necessite de um software que não esteja disponível, solicite sua instalação pela Central de Recursos.
"""


with open(md_file, "w", encoding="utf-8") as file:
    file.write(conteudo)


print("Tabela de softwares atualizada!")