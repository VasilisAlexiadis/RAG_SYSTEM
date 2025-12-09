def semantic_chunk(text: str):
    try:
        from llama_index.core.node_parser import SemanticSplitterNodeParser
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding

        embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

        splitter = SemanticSplitterNodeParser(
            buffer_size=1,          # sliding window
            breakpoint_threshold_type="percentile",
            breakpoint_percentile_threshold=95,
            embed_model=embed_model,
        )

        nodes = splitter.get_nodes_from_documents([
            {"text": text}
        ])

        return [node.get_content() for node in nodes]
    except Exception:
        # Fallback: simple length-based chunking if llama_index isn't installed
        max_chars = 1000
        words = text.split()
        chunks = []
        cur = []
        cur_len = 0
        for w in words:
            if cur_len + len(w) + 1 > max_chars and cur:
                chunks.append(" ".join(cur))
                cur = []
                cur_len = 0
            cur.append(w)
            cur_len += len(w) + 1
        if cur:
            chunks.append(" ".join(cur))
        return chunks


def chunk_text(text: str):
    """Public API expected by the rest of the codebase.

    Prefer the semantic chunking implementation when available, otherwise
    fall back to the simple splitter above.
    """
    return semantic_chunk(text)
