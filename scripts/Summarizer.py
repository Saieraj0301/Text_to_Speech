from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import textwrap

model_name = "sshleifer/distilbart-cnn-12-6"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def chunk_text(text, max_tokens=800):
    sentences = text.split(". ")
    chunks, current_chunk = [], ""

    for sentence in sentences:
        test_chunk = f"{current_chunk} {sentence}".strip()
        token_count = len(tokenizer.encode(test_chunk, truncation=False))

        if token_count <= max_tokens:
            current_chunk = test_chunk
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_text(text, strength=50):
    """
    Summarizes text with chunking and summarization strength control.
    Strength: 1 (least summarization) to 100 (most aggressive summarization)
    """
    chunks = chunk_text(text)
    summaries = []

    # Lower strength → longer summary → higher max_length
    strength_ratio = max(1, min(strength, 100)) / 100.0
    max_len = int(120 - (strength_ratio * 80))     # range: 40 to 120
    min_len = int(max_len * 0.6)                   # ensure it's always < max_len

    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", max_length=1024, truncation=True)

        summary_ids = model.generate(
            inputs["input_ids"],
            num_beams=4,
            max_length=max_len,
            min_length=min_len,
            early_stopping=True
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary.strip())

    return " ".join(summaries)
