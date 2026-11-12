
from abc import ABC, abstractmethod


# STEP 1: Abstract parent class
class Document(ABC):

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def extract_text(self):
        pass


# STEP 2: PDF document
class PDFDocument(Document):

    def extract_text(self):
        return "Extracting text from PDF"


# STEP 3: Text document
class TextDocument(Document):

    def extract_text(self):
        return "Extracting text from TXT"


# STEP 4: Word document
class WordDocument(Document):

    def extract_text(self):
        return "Extracting text from Word"


# STEP 5: Chunker class
class Chunker:

    def __init__(self, chunk_size):

        if (
            not isinstance(chunk_size, int)
            or isinstance(chunk_size, bool)
            or chunk_size <= 0
        ):
            raise ValueError(
                "Chunk size must be a positive integer"
            )

        self.chunk_size = chunk_size

    def create_chunks(self, text):

        chunks = []

        for i in range(0, len(text), self.chunk_size):
            chunks.append(
                text[i:i + self.chunk_size]
            )

        return chunks

    
# Alternative chunker with the same interface
class AdvancedChunker:

    def create_chunks(self, text):

        words = text.split()

        return [
            " ".join(words[i:i + 2])
            for i in range(0, len(words), 2)
        ]



# STEP 6: Document Pipeline using composition
class DocumentPipeline:

    def __init__(self, chunker):
        self.chunker = chunker

    def process(self, document):

        extracted_text = document.extract_text()

        chunks = self.chunker.create_chunks(
            extracted_text
        )

        return chunks


# STEP 7: Execute application
if __name__ == "__main__":

    chunker = Chunker(5)

    pipeline = DocumentPipeline(chunker)

    documents = [
        PDFDocument("report.pdf"),
        TextDocument("notes.txt"),
        WordDocument("report.docx")
    ]

    for document in documents:

        print("\nDocument:", document.filename)

        result = pipeline.process(document)

        print("Chunks:", result)

    

print("\nTesting dependency injection:")

advanced_chunker = AdvancedChunker()

advanced_pipeline = DocumentPipeline(advanced_chunker)

document = PDFDocument("advanced_report.pdf")

result = advanced_pipeline.process(document)

print("Advanced chunks:", result)
