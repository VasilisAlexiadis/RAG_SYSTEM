try:
    from langchain.prompts import PromptTemplate

    rag_prompt = PromptTemplate(
        template="""
Use ONLY the context below to answer the question.
If the answer is not explicitly in the context, say you don't know.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""",
        input_variables=["context", "question"]
    )
except Exception:
    class _SimplePromptTemplate:
        def __init__(self, template: str, input_variables: list[str]):
            self.template = template
            self.input_variables = input_variables

        def format(self, **kwargs) -> str:
            return self.template.format(**kwargs)

    rag_prompt = _SimplePromptTemplate(
        template="""
Use ONLY the context below to answer the question.
If the answer is not explicitly in the context, say you don't know.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""",
        input_variables=["context", "question"]
    )
