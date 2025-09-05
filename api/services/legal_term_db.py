LEGAL_TERMS = {
    "affidavit": "A written statement confirmed by oath, used as evidence in court.",
    "plaintiff": "The person who brings a case against another in a court of law.",
    "defendant": "An individual, company, or institution sued or accused in court."
}

def get_term_definition(term: str) -> str:
    return LEGAL_TERMS.get(term.lower(), "Definition not found.")
