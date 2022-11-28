import os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.utils import convert_files_to_docs

# required for corporate SSL proxy
#os.environ['REQUESTS_CA_BUNDLE'] = 'cisco_umbrella_root_ca.cer'

host = os.environ.get("ELASTICSEARCH_HOST", "localhost")
document_store = ElasticsearchDocumentStore(host=host, username="", password="", index="igt-docs")

doc_dir = "haystackdata"
docs = convert_files_to_docs(dir_path=doc_dir, split_paragraphs=True)
document_store.write_documents(docs)