# Markdown Converter

Aplicação desktop para Windows desenvolvida em Python para converter documentos para Markdown utilizando a biblioteca MarkItDown.

O objetivo do projeto é disponibilizar uma interface simples e intuitiva para converter documentos individuais ou coleções de documentos para Markdown, permitindo a sua utilização em sistemas de documentação, gestão do conhecimento, websites, blogs e projetos de Inteligência Artificial.

---

## Principais Funcionalidades

### Conversão Individual

Permite converter rapidamente um único documento para Markdown.

Formatos suportados pelo MarkItDown:

- PDF
- DOCX
- PPTX
- XLSX
- HTML
- TXT
- Outros formatos suportados pela biblioteca

---

### Conversão em Lote

Converte automaticamente todos os documentos compatíveis existentes numa pasta.

Ideal para:

- Arquivos documentais
- Bases de conhecimento
- Migração de documentação
- Preparação de dados para sistemas de IA

---

### Preview Markdown

Visualização imediata do conteúdo Markdown gerado diretamente na aplicação.

---

### Sistema de Log

Registo detalhado das operações executadas:

- Conversões efetuadas
- Erros encontrados
- Estado das operações
- Atualizações realizadas

---

### Atualização de Dependências

Permite verificar e atualizar automaticamente as bibliotecas necessárias ao funcionamento da aplicação.

---

## Interface da Aplicação

A interface gráfica foi desenvolvida com CustomTkinter e inclui:

- Barra de ferramentas
- Painel de progresso
- Painel de log
- Visualizador Markdown
- Janela de informações da aplicação

---

## Tecnologias Utilizadas

Este projeto utiliza diversas bibliotecas open source:

- Python 3.13
- MarkItDown
- CustomTkinter
- TkinterDnD2
- Magika
- PDFMiner.six
- OpenPyXL
- PyInstaller

---

## Download

A versão mais recente pode ser obtida em:

👉 https://github.com/vantunes/markdown-converter/releases

---

## Instalação Manual

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Execução

```bash
python main.py
```

---

## Construção do Executável

O projeto inclui uma configuração de compilação baseada em:

- Python 3.13
- PyInstaller
- Magika
- MarkItDown

Após a configuração do ambiente de compilação:

```bash
build_exe.bat
```

Será gerado um executável funcional em:

```text
dist\main\
```

---

## Estrutura do Projeto

```text
MarkdownConverter
│
├── main.py
├── settings.py
├── converter.py
├── file_scanner.py
├── updater.py
│
├── services
│   ├── conversion_service.py
│   ├── timer_service.py
│   └── update_service.py
│
├── ui
│   ├── main_window.py
│   ├── toolbar.py
│   ├── log_panel.py
│   ├── preview_panel.py
│   ├── progress_panel.py
│   └── about_dialog.py
│
├── installer
│
├── requirements.txt
├── build_exe.bat
└── README.md
```

---

## Roadmap

### Versão 2.4

- Drag & Drop
- Melhorias do cronómetro
- Otimização da interface

### Versão 2.5

- Exportação de logs
- Configurações persistentes
- Melhorias de desempenho

### Versão 3.0

- Sistema de atualização automática
- Instalador otimizado
- Novos formatos suportados

---

## Autor

vantunes

---

## Agradecimentos

Este projeto utiliza bibliotecas open source desenvolvidas por diversas comunidades e organizações.

Agradecimento especial aos autores dos projetos:

- MarkItDown (Microsoft)
- CustomTkinter
- TkinterDnD2
- Magika (Google)
- PDFMiner.six
- PyInstaller

Sem estas bibliotecas o desenvolvimento desta aplicação não seria possível.

---

## Licença

Projeto de uso pessoal e educativo.

---

## Apoiar o Projeto

O Markdown Converter é desenvolvido de forma independente.

Se esta ferramenta lhe foi útil e desejar apoiar futuras melhorias, pode considerar um donativo voluntário.

### 💙 PayPal

https://paypal.me/rootiv

### 💜 Revolut

https://revolut.me/vitor0as

Obrigado pelo apoio!