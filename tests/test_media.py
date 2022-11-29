import pytest

from blog.media import MEDIA_RE


@pytest.mark.parametrize('source', [
    '![Alt text](../../../Downloads/leaves_maple_green_14830_1920x1080-2889998535.jpg)',
    '![Alt text](https://www.reactiongifs.com/r/review.gif)',
    '![Alt text](https://en.wikipedia.org/wiki/Scooter_(motorcycle))',
    '![Alt text](https://example/lorem+ipsum)',
    '![Alt text](https://example/lorem%20ipsum)',
])
def test_media_re(source):
    assert MEDIA_RE.search(f'''
        Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. [{source}{{: .right }}](https://example.com) [Proin](#proin)
        finibus ex erat, et rhoncus tortor consectetur sed.
    ''').group(0) == source
