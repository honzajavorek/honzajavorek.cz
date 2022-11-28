from pelican import signals


def register():
    signals.article_generator_context.connect(set_translation_id)


def set_translation_id(article_generator, metadata):
    metadata.setdefault('translation-id', metadata['slug'])
