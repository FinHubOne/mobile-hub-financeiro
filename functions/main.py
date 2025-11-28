
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
    "Pix": ["pix"], 
}

def get_clean_description(raw_description: str, keyword_found: str) -> str:
    """
    Extrai uma descrição mais limpa e humanizada da string original.
    Ex: "PGTO *UBER DO BRASIL TEC" com keyword "uber" -> "Uber do Brasil Tec"
    """
    try:
        # Tenta encontrar o texto que vem *depois* da palavra-chave ou de um asterisco.
        match = re.search(r'[\*\- ]\s*({}[a-zA-Z0-9 .]*)'.format(re.escape(keyword_found)), raw_description, re.IGNORECASE)
        if match and match.group(1) and len(match.group(1).strip()) > 3:
            return match.group(1).strip().title()
    except Exception:
        pass
        
    # Fallback: Se a regex falhar ou não encontrar um nome válido, usa a própria keyword capitalizada.
    return keyword_found.capitalize()

# --- A FUNÇÃO PRINCIPAL (PROCESSADORA) ---
@https_fn.on_call(region='southamerica-east1')
def process_transaction_py(req: https_fn.CallableRequest) -> dict:
    """
    Processa uma descrição de transação bruta para extrair categoria e descrição limpa.
    AGORA COM LÓGICA MELHORADA!
    """
    raw_description = req.data.get("raw_description", "")
    
    if not raw_description:
        raise https_fn.HttpsError(
            code=https_fn.FunctionsErrorCode.INVALID_ARGUMENT,
            message="A função deve ser chamada com um argumento 'raw_description'."
        )

    lower_description = raw_description.lower()

    # --- LÓGICA ESPECIAL PARA PIX ---
    if "pix" in lower_description:
        match = re.search(r'pix[\s\-]*[a-zA-Z]*[\s\-]*([a-zA-Z\s.]+)', lower_description)
        clean_desc = "Transação Pix"
        if match and match.group(1):
            name = match.group(1).strip()
            name = name.replace("recebida", "").replace("enviado", "").strip()
            if len(name) > 3:
              clean_desc = name.title()

        return {
            "category": "Pix",
            "clean_description": clean_desc,
        }

    # --- LÓGICA DE CATEGORIZAÇÃO POR REGRAS (MAIS ROBUSTA) ---
    for category, keywords in CATEGORIZATION_RULES.items():
        for keyword in keywords:
            if keyword in lower_description:
                # A função auxiliar agora é mais simples e confiável.
                clean_desc = get_clean_description(raw_description, keyword)
                
                return {
                    "category": category,
                    "clean_description": clean_desc,
                }
    
    # --- FALLBACK INTELIGENTE PARA "OUTROS" ---
    # Se nenhuma regra corresponder, tenta extrair a parte mais relevante do final.
    parts = re.split(r'[\*\- ]', raw_description)
    # Pega a última parte da string que tenha pelo menos 4 caracteres.
    relevant_part = next((part.strip().title() for part in reversed(parts) if len(part.strip()) >= 4), None)
    
    if relevant_part:
        clean_description = relevant_part
    else:
        # Se não encontrar nada, usa a string inteira capitalizada.
        clean_description = raw_description.strip().title()
        
    return {
        "category": "Outros",
        "clean_description": clean_description,
    }
