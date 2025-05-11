import os
import time
from tkinter import Tk, filedialog

import pikepdf
from tqdm import tqdm


def comprimir_pdf(entrada, saida):
    with pikepdf.open(entrada) as pdf:
        total_paginas = len(pdf.pages)

        print("\nIniciando a compressão...")

        with tqdm(total=total_paginas, desc="Comprimindo PDF", unit="página") as pbar:
            pbar.update(len(pdf.pages))
            pdf.save(saida, compress_streams=True)


def escolher_arquivo_entrada():
    root = Tk()
    root.withdraw()
    arquivo_entrada = filedialog.askopenfilename(
        title="Escolha o arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")]
    )
    return arquivo_entrada


def gerar_nome_saida(arquivo_entrada):
    pasta_entrada = os.path.dirname(arquivo_entrada)
    nome_arquivo = os.path.splitext(os.path.basename(arquivo_entrada))[0]
    nome_saida = f"{nome_arquivo}_comprimido.pdf"

    return os.path.join(pasta_entrada, nome_saida)


def main():
    print("------------------------------------------------------------")
    print("          Iniciando o processo de compressão do PDF...      ")
    print("------------------------------------------------------------")

    arquivo_entrada = escolher_arquivo_entrada()
    if not arquivo_entrada:
        print("\nNenhum arquivo selecionado. O processo foi cancelado.")
        return

    arquivo_saida = gerar_nome_saida(arquivo_entrada)

    print(f"\nArquivo de entrada selecionado: {arquivo_entrada}")

    comprimir_pdf(arquivo_entrada, arquivo_saida)

    print(f"\nO arquivo foi salvo em: {os.path.abspath(arquivo_saida)}")

    input("\nPressione a tecla enter para fechar o terminal...")


if __name__ == "__main__":
    main()
