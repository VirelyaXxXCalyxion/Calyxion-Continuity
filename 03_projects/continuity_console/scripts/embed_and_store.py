from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

# Setup paths
ROOT = Path(r"C:\Users\fullm\OneDrive\Desktop\Calyxion_Continuity")
CHUNKS_DIR = ROOT / "04_retrieval" / "chunks"
CHROMA_DIR = ROOT / "04_retrieval" / "chroma_db"

# Initialize model + persistent DB
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=str(CHROMA_DIR))
collection = client.get_or_create_collection(name="calyxion_memory")

def main():
    chunk_files = list(CHUNKS_DIR.glob("*.md"))

    if not chunk_files:
        print("No chunks found.")
        return

    for file in chunk_files:
        content = file.read_text(encoding="utf-8")

        embedding = model.encode(content).tolist()

        collection.add(
            documents=[content],
            embeddings=[embedding],
            ids=[file.stem]
        )

        print(f"Embedded: {file.name}")

    print("\nAll chunks embedded successfully.")

if __name__ == "__main__":
    main()
