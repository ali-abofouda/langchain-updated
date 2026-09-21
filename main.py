from pathlib import Path


def main():
    notebook = Path("updatedLangchain/01-creating-agents.ipynb")
    print("LangChain Updates")
    print(f"Notebook available: {notebook.exists()} ({notebook})")


if __name__ == "__main__":
    main()
