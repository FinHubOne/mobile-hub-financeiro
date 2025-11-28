# main.py
# Importa as bibliotecas necessárias do Firebase
from firebase_admin import initialize_app
from firebase_functions import https_fn
import re

# Inicializa o app do Firebase Admin.
initialize_app()

# --- A "INTELIGÊNCIA" DO BACKEND ---
# Dicionário expandido para maior cobertura de transações.
CATEGORIZATION_RULES = {
    "Transporte": ["uber", "99", "rappi", "lime", "cittamobi", "posto", "gasolina", "estacionamento"],
    "Alimentação": ["ifood", "rappi", "mcdonalds", "bk", "burger king", "restaurante", "padaria", "supermercado", "mercearia"],
    "Compras": ["amazon", "mercado livre", "shopee", "shein", "cea", "renner", "magazine luiza", "americanas"],
    "Saúde": ["farmacia", "drogaria", "unimed", "bradesco saude", "plano de saude", "medico"],
    "Moradia": ["aluguel", "condominio", "enel", "sabesp", "internet", "iptu"],
    "Lazer": ["spotify", "netflix", "hbo", "disney+", "cinema", "show", "ingresso", "bar", "evento"],
    "Educação": ["udemy", "curso", "faculdade", "escola"],
    "Pix": ["pix"], # Regra genérica para PIX, mas será tratada de forma especial abaixo.
}

def get_clean_description(raw_description: str, keyword_found: str) -> str:
    """
    Extrai uma descrição mais limpa e humanizada da string original.
    Ex: "PGTO *UBER DO BRASIL TEC" com keyword "uber" -> "Uber do Brasil Tec"
    """
    try:
        # Tenta encontrar o texto que vem *depois* da palavra-chave ou de um asterisco.
        # Isso geralmente corresponde ao nome do estabelecimento.
        match = re.search(r'[\*\- ]\s*({}[a-zA-Z0-9 .]*)'.format(re.escape(keyword_found)), raw_description, re.IGNORECASE)
        if match and match.group(1):
            # Limpa espaços extras e capitaliza o nome de forma inteligente (Ex: "Ifood" em vez de "ifood")
            return match.group(1).strip().title()
    except Exception:
        # Se a regex falhar, retorna a keyword capitalizada como fallback.
        pass
        
    return keyword_found.capitalize()

# --- A FUNÇÃO PRINCIPAL (PROCESSADORA) ---
@https_fn.on_call(region='southamerica-east1')
def process_transaction_py(req: https_fn.CallableRequest) -> dict:
    """
    Processa uma descrição de transação bruta para extrair categoria e descrição limpa.
    AGORA COM LÓGICA MELHORADA!
    """
    raw_description = req.data.get("raw_description", "") # CORREÇÃO APLICADA AQUI
    
    if not raw_description:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="A função deve ser chamada com um argumento 'raw_description'." # MENSAGEM CORRIGIDA
        )

    lower_description = raw_description.lower()

    # --- LÓGICA ESPECIAL PARA PIX (INOVADOR) ---
    if "pix" in lower_description:
        # Tenta extrair o nome do destinatário/remetente do PIX
        # Ex: "TRANSF PIX RECEBIDA - JOAO SILVA" -> "Joao Silva"
        # Ex: "PAGAMENTO PIX - LOJA DE ROUPAS" -> "Loja de Roupas"
        match = re.search(r'pix[\s\-]*[a-zA-Z]*[\s\-]*([a-zA-Z\s.]+)', lower_description)
        clean_desc = "Transação Pix" # Fallback
        if match and match.group(1):
            name = match.group(1).strip()
            # Remove palavras comuns para limpar o nome
            name = name.replace("recebida", "").replace("enviado", "").strip()
            clean_desc = name.title()

        return {
            "category": "Pix",
            "cleanDescription": clean_desc,
        }

    # --- LÓGICA DE CATEGORIZAÇÃO POR REGRAS (EFICAZ) ---
    for category, keywords in CATEGORIZATION_RULES.items():
        for keyword in keywords:
            if keyword in lower_description:
                # Usa a função auxiliar para limpar a descrição
                clean_desc = get_clean_description(raw_description, keyword)
                
                return {
                    "category": category,
                    "cleanDescription": clean_desc,
                }
    
    # --- FALLBACK INTELIGENTE PARA "OUTROS" ---
    # Se nenhuma regra corresponder, tenta extrair a parte mais relevante.
    # Ex: "COMPRA CARTAO - PADARIA ESTRELA" -> "Padaria Estrela"
    parts = raw_description.split('*')
    if len(parts) > 1:
        clean_description = parts[-1].strip().title()
    else:
        # Se não houver '*', pega a string inteira e capitaliza
        clean_description = raw_description.strip().title()
        
    return {
        "category": "Outros",
        "cleanDescription": clean_description,
    }
