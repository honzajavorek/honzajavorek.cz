from pelican import signals


def register():
    signals.feed_generated.connect(set_meta)


def set_meta(context, feed):
    feed.feed.update(context['CUSTOM_FEED_META'])
