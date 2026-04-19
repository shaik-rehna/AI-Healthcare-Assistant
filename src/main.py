from gen_ai_healthcare_report_gen.app.prompts.triage_prompt import build_prompt
from gen_ai_healthcare_report_gen.app.models.inference import generate_response
from gen_ai_healthcare_report_gen.app.outputs.parser import parse_output
from gen_ai_healthcare_report_gen.app.outputs.report_generator import generate_pdf

symptoms = "I have fever, cough, and fatigue."

prompt = build_prompt(symptoms)

raw_output = generate_response(prompt)

parsed = parse_output(raw_output)

generate_pdf(parsed)

print("PDF report generated.")