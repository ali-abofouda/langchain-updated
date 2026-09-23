import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def check_repository_status():
    load_dotenv()
    print("=" * 60)
    print("LangChain Modern Architecture (v1.x / v0.3+) Status Check")
    print("=" * 60)

    # 1. Environment variables
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        masked_key = groq_key[:6] + "..." + groq_key[-4:] if len(groq_key) > 10 else "***"
        print(f"[OK] GROQ_API_KEY detected: {masked_key}")
    else:
        print("[WARNING] GROQ_API_KEY not found in .env (Groq calls will require it)")

    # 2. Notebooks check
    notebooks = [
        "01-creating-agents.ipynb",
        "02-llm-model-integration.ipynb",
        "03-invoking-batch-streaming.ipynb",
        "04-implementing-tools.ipynb",
        "05-message-types.ipynb",
        "06-structured-output-pydantic.ipynb",
        "07-structured-output-typedict.ipynb",
        "08-structured-output-dataclass.ipynb",
        "09-summarization-middleware.ipynb",
        "10-human-in-the-loop-middleware.ipynb",
    ]

    print("\n--- Jupyter Notebooks (updatedLangchain/) ---")
    all_nb_ok = True
    for nb_name in notebooks:
        nb_path = Path("updatedLangchain") / nb_name
        if nb_path.exists():
            size_kb = nb_path.stat().st_size / 1024
            print(f"  [FOUND] {nb_name:<38} ({size_kb:.1f} KB)")
        else:
            print(f"  [MISSING] {nb_name}")
            all_nb_ok = False

    # 3. Documentation check
    docs = [
        "README.md",
        "01-creating-agents.md",
        "02-llm-model-integration.md",
        "03-invoking-batch-streaming.md",
        "04-implementing-tools.md",
        "05-message-types.md",
        "06-structured-output-pydantic.md",
        "07-structured-output-typedict.md",
        "08-structured-output-dataclass.md",
        "09-summarization-middleware.md",
        "10-human-in-the-loop-middleware.md",
        "interview-questions-guide.md",
    ]

    print("\n--- Documentation & Interview Guides (docs/) ---")
    all_docs_ok = True
    for doc_name in docs:
        doc_path = Path("docs") / doc_name
        if doc_path.exists():
            print(f"  [FOUND] {doc_name}")
        else:
            print(f"  [MISSING] {doc_name}")
            all_docs_ok = False

    print("\n" + "=" * 60)
    if all_nb_ok and all_docs_ok:
        print("Repository is fully structured and verified successfully.")
    else:
        print("Some files are missing. Please inspect the output above.")
    print("=" * 60)


if __name__ == "__main__":
    check_repository_status()
