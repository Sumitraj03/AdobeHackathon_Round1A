# AdobeHackathon_Round1A – PDF Outline Extractor

This project extracts structured outlines (headings and subheadings) from PDF documents and converts them into a clean JSON format. It identifies headings based on properties like capitalization and font size, making it suitable for navigation, indexing, or pre-processing for further analysis.

---

## Features

1. Extracts headings (H1–H3) from PDFs using text heuristics.  
2. Outputs structured JSON with page references.  
3. Lightweight and works offline (CPU-only).  
4. Docker support for consistent cross-platform execution.

---

## Folder Structure

```
ROUND 1A/
│
├── input/                # Place input PDFs here
├── output/               # Extracted JSON outputs
├── main.py               # Core extraction logic
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build file
└── README.md             # Project documentation
```

---

## Input Format

Place PDF files in the `input/` folder.

---

## Output Format

JSON files will be saved in the `output/` folder, example:

```json
{
  "title": "sample",
  "outline": [
    {
      "level": "H3",
      "text": "EDUCATION",
      "page": 1
    },
    {
      "level": "H2",
      "text": "EXPERIENCE",
      "page": 2
    }
  ]
}
```

---

## Running Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run script:

```bash
python main.py
```

Output JSON will be saved in the `output/` folder.

---

## Running with Docker

1. Build Docker image:

```bash
docker build --platform linux/amd64 -t pdf-outline-extractor .
```

2. Run container:

```bash
docker run --rm -v "${PWD}/input:/app/input" -v "${PWD}/output:/app/output" pdf-outline-extractor
```

---

## Example Use Cases

- Resume heading extraction for recruitment tools  
- Generating navigation trees for academic or legal documents  
- Pre-processing documents for semantic search or NLP pipelines  

---

## Built With

- Python 3  
- PyMuPDF (fitz)  
- Docker  