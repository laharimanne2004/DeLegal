from transformers import pipeline

# Load summarization model (smaller version)
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_text(text, max_chunk=500):
    text = text.replace('\n', ' ')
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]

    summary = ""
    for chunk in chunks:
        # T5 expects input in a special format
        chunk = "summarize: " + chunk
        summary_piece = summarizer(chunk, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
        summary += summary_piece + " "
    return summary.strip()
