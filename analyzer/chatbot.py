import random

def generate_response(user_input, context_text):
    user_input = user_input.lower()

    if "diagnosis" in user_input:
        return "The diagnosis refers to the medical condition identified in the report."
    elif "treatment" in user_input or "medication" in user_input:
        return "Treatment involves the medical interventions listed in the report, such as drugs or procedures."
    elif "symptom" in user_input:
        return "Symptoms are the patient’s reported issues, like pain or discomfort."
    elif "summary" in user_input:
        return "This report discusses the patient's condition, relevant symptoms, and ongoing treatments."
    else:
        return random.choice([
            "Can you ask more specifically about diagnosis, symptoms, or treatment?",
            "I'm here to help you understand the report. Try asking about a symptom or diagnosis.",
        ])
