import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = " ".join(text.split())
    return text

def jd(job_d):
    stopwords = {
        "the", "is", "and", "for", "with", "a", "to", "in", "of",
        "on", "at", "by", "an", "be", "are", "as", "from"
    }

    job = clean_text(job_d)
    words = job.split()
    keywords = set()

    for word in words:
        if word not in stopwords and len(word) > 2:
            keywords.add(word)

    return list(keywords)
