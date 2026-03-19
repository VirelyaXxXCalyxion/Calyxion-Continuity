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

def main() -> None:
    query = "voice recognition and continuity threshold"

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print(f"\nQuery: {query}\n")
    ids = results.get("ids", [[]])[0]
    docs = results.get("documents", [[]])[0]

    if not ids:
        print("No results found.")
        return

    for i, (doc_id, doc) in enumerate(zip(ids, docs), start=1):
        preview = doc[:400].replace("\n", " ")
        print(f"Result {i}: {doc_id}")
        print(f"Preview: {preview}...\n")

if __name__ == "__main__":
    main()
