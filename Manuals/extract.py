import fitz
doc = fitz.open('synthesis_school_manual.pdf')
for i in range(min(5, len(doc))):
    page = doc[i]
    text = page.get_text()
    print(f'=== PAGE {i+1} ===')
    print(text[:5000])
