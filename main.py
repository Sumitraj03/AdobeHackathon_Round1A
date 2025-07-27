import os
import json
import fitz  # PyMuPDF

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outlines = []

    title = doc.metadata.get("title") or os.path.splitext(os.path.basename(pdf_path))[0]

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    spans = l["spans"]
                    for s in spans:
                        text = s.get("text", "").strip()
                        size = s.get("size", 0)
                        if text and 6 < len(text) < 80:
                            if size >= 16:
                                level = 'H1'
                            elif size >= 13:
                                level = 'H2'
                            elif size >= 11:
                                level = 'H3'
                            else:
                                continue
                            outlines.append({
                                "level": level,
                                "text": text,
                                "page": page_num + 1
                            })

    unique_outlines = []
    seen = set()
    for item in outlines:
        key = (item["level"], item["text"], item["page"])
        if key not in seen:
            unique_outlines.append(item)
            seen.add(key)

    return {
        "title": title,
        "outline": unique_outlines
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdfs = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

    for pdf_file in pdfs:
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        output = extract_outline(pdf_path)
        output_filename = os.path.splitext(pdf_file)[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"Processed {pdf_file} -> {output_filename}")

if __name__ == "__main__":
    main()
