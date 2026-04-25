import re

COMPANY_INDUSTRY = {
    "vodafone": "telecom",
    "orange": "telecom",
    "etisalat": "telecom",
    "we": "telecom",

    "nike": "fashion",
    "adidas": "fashion",

    "loreal": "beauty",
    "nivea": "beauty",
}

INVALID_INPUTS = {
    "egypt", "saudi", "ksa", "cairo", "alexandria"
}

INDUSTRY_PRODUCTS = {
    "telecom": ["data bundle", "voice calls", "sms", "roaming", "sim card"],
    "fashion": ["t-shirt", "shoes", "jacket", "jeans"],
    "beauty": ["skincare", "makeup", "serum", "cleanser"],
    "retail": ["product a", "product b", "product c"]
}


def normalize(name: str) -> str:
    return re.sub(r"\s+", " ", name.strip().lower())


def classify_company(name: str) -> str:
    name = normalize(name)

    if name in INVALID_INPUTS:
        return "retail"

    if name in COMPANY_INDUSTRY:
        return COMPANY_INDUSTRY[name]

    if any(k in name for k in ["vodafone", "orange", "etisalat", "mobile", "telecom"]):
        return "telecom"

    if any(k in name for k in ["nike", "adidas", "fashion", "wear"]):
        return "fashion"

    if any(k in name for k in ["loreal", "nivea", "beauty", "skin"]):
        return "beauty"

    return "retail"


def filter_products(products: list, industry: str) -> list:
    allowed = INDUSTRY_PRODUCTS.get(industry, INDUSTRY_PRODUCTS["retail"])
    cleaned = [p for p in products if p in allowed]

    return cleaned if cleaned else allowed[:3]
