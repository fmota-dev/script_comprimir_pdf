# Compressor de PDF para Documentos Digitalizados

Este script foi desenvolvido a pedido do **setor de estoque**, que está digitalizando todos os documentos internos para reduzir o uso de papel. Durante esse processo, surgiu a necessidade de **importar arquivos PDF para o sistema**, que aceita apenas arquivos com até **100 MB**. Anteriormente, a redução de tamanho dos arquivos era feita de forma manual, o que tomava tempo e era pouco eficiente.

Este utilitário automatiza esse processo, **comprimindo arquivos PDF** rapidamente e com facilidade, garantindo que estejam dentro do limite exigido.

## ⚙️ Funcionalidade

- Seleciona um arquivo PDF usando uma interface gráfica.
- Comprime o conteúdo do PDF mantendo as páginas intactas.
- Exibe uma barra de progresso com o total de paginas durante o processo.
- Salva o arquivo comprimido com sufixo `_comprimido.pdf` na mesma pasta do original.

## 🖥️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências com o comando:

```bash
pip install pikepdf tqdm
```

3. Execute o script com:

```bash
python main.py
```

4. Escolha o arquivo PDF desejado quando a janela for aberta.

## 📦 Exemplo de Saída

Se você escolher o arquivo:

```
documento_original.pdf
```

Será gerado:

```
documento_original_comprimido.pdf
```

na mesma pasta.

## ✅ Requisitos

- Python 3.7+
- Biblioteca `pikepdf` para manipulação de PDFs
- Biblioteca `tqdm` para exibir progresso no terminal

## 💡 Observações

- O processo de compressão utiliza `compress_streams=True` do `pikepdf`, o que reduz significativamente o tamanho do PDF sem comprometer as páginas.
- Ideal para lotes de digitalização que excedem 100 MB.

---

🚀 Feito por fmota.dev
