def classify_report(text):
    categories = {
        "Cardiology": ["heart", "cardiac", "myocardial", "ECG", "angina"],
        "Neurology": ["brain", "seizure", "stroke", "neuro", "MRI"],
        "Emergency": ["ER", "emergency", "ICU", "acute", "critical"],
        "Oncology": ["tumor", "cancer", "chemotherapy", "metastasis"],
        "General": []
    }
    for category, keywords in categories.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                return category
    return "General"

