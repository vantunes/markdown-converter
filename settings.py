"""
Configurações globais da aplicação
"""


# ==================================================
# INFORMAÇÕES DA APLICAÇÃO
# ==================================================

APP_NOME = "Markdown Converter"

APP_VERSAO = "2.2.0"

APP_AUTOR = "vantunes & Microsoft/guitub Markdown"


# ==================================================
# APARÊNCIA
# ==================================================

APP_TEMA = "dark"

APP_COR = "blue"


# Temas possíveis:
#
# "blue"
# "green"
# "dark-blue"


# ==================================================
# JANELA PRINCIPAL
# ==================================================

JANELA_LARGURA = 1200

JANELA_ALTURA = 750

JANELA_REDIMENSIONAVEL = True


# ==================================================
# LOG
# ==================================================

MAX_LINHAS_LOG = 5000

PASTA_LOGS = "logs"


# ==================================================
# PROGRESSO
# ==================================================

ATUALIZAR_PROGRESSO_MS = 1000


# ==================================================
# PREVIEW MARKDOWN
# ==================================================

MAX_PREVIEW_CARACTERES = 500000


# ==================================================
# EXTENSÕES SUPORTADAS
# ==================================================

EXTENSOES_SUPORTADAS = {

    ".pdf",

    ".docx",

    ".pptx",

    ".xlsx",

    ".html",

    ".htm",

    ".txt",

    ".csv",

    ".xml",

    ".json",

    ".epub"

}


# ==================================================
# DEPENDÊNCIAS A ATUALIZAR
# ==================================================

DEPENDENCIAS = [

    "markitdown",

    "customtkinter",

    "tkinterdnd2"

]


# ==================================================
# BARRA DE PROGRESSO
# ==================================================

COR_PROGRESO_CONCLUIDO = "#2ECC71"

COR_PROGRESO_EM_CURSO = "#3498DB"


# ==================================================
# FUTURAS FUNCIONALIDADES
# ==================================================

ATIVAR_DRAG_DROP = True

ATIVAR_HISTORICO = True

ATIVAR_EXPORTACAO_LOG = True

ATIVAR_MENU_SOBRE = True