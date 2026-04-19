import csv

from src.prompts.triage_prompt import build_prompt
from src.models.inference import generate_response
from src.models.inference_finetuned import generate_finetuned_response
from evaluation.test_prompts import test_cases


with open(
    "evaluation/results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as csvfile, open(
    "evaluation/terminal_log.txt",
    "w",
    encoding="utf-8"
) as logfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "symptoms",
        "base_output",
        "finetuned_output"
    ])


    for i, case in enumerate(test_cases, start=1):

        print(f"\nRunning test {i}/{len(test_cases)}...")
        print(f"Symptoms: {case}")

        prompt = build_prompt(case)

        print("Generating BASE model output...")
        base_output = generate_response(prompt)

        print("Generating FINE-TUNED model output...")
        finetuned_output = generate_finetuned_response(prompt)

        print("Saving results...")

        writer.writerow([
            case,
            base_output,
            finetuned_output
        ])

        logfile.write("\n====================\n")
        logfile.write(f"SYMPTOMS:\n{case}\n")
        logfile.write("\nBASE MODEL:\n\n")
        logfile.write(base_output + "\n")
        logfile.write("\nFINE-TUNED MODEL:\n\n")
        logfile.write(finetuned_output + "\n")

        print("Done.")