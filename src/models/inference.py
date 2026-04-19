from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/gemma-2-2b-it"
)

# huggingface-cli login

def generate_response(prompt):

    output = generator(
        prompt,
        max_new_tokens=200,
        max_length=None,
        do_sample=False,
        return_full_text=False
    )

    return output[0]["generated_text"]