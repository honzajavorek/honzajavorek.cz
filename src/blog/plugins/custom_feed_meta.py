from pelican import signals


def register():
    signals.feed_generated.connect(set_meta)


def set_meta(context, feed):
    feed_meta = context['CUSTOM_FEED_META'](context)
    feed.feed.update(feed_meta)
