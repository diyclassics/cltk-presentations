from cltk.corpus.utils.importer import CorpusImporter

# Latin
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_text_latin_library')
corpus_importer.import_corpus('latin_models_cltk')

# Greek
corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_models_cltk')

# Akkadian
corpus_importer = CorpusImporter('akkadian')
corpus_importer.import_corpus('cdli_corpus')
