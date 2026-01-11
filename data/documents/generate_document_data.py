# Placeholder: Generate synthetic document metadata for document intelligence
import pandas as pd

def generate_document_metadata(num_docs=20):
    titles = [f"Technical Report {i+1}" for i in range(num_docs)]
    types = ['PDF', 'DOCX', 'TXT'] * (num_docs // 3 + 1)
    types = types[:num_docs]
    pages = [10 + i for i in range(num_docs)]
    df = pd.DataFrame({'title': titles, 'type': types, 'pages': pages})
    df.to_csv('synthetic_document_metadata.csv', index=False)
    print('Synthetic document metadata saved as synthetic_document_metadata.csv')

if __name__ == "__main__":
    generate_document_metadata()
