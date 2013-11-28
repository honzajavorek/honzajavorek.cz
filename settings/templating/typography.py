# -*- coding: utf-8 -*- #

import re

import lxml.html


# sources:
# - texy-2.1/texy/modules/TexyTypographyModule.php
# - https://gist.github.com/msgre/3805872


tag_blacklist = ('area', 'base', 'br', 'canvas', 'code', 'col', 'colgroup',
                 'embed', 'head', 'html', 'hr', 'iframe', 'input', 'link',
                 'map', 'meta', 'noscript', 'object', 'optgroup', 'param',
                 'pre', 'samp', 'script', 'select', 'source', 'style',
                 'table', 'tbody', 'tfoot', 'thead', 'title', 'tr', 'track',
                 'var', 'video', 'xmp')

chars = ur'A-Za-z\u00C0-\u02FF\u0370-\u1EFF'

typo_patterns = (
    # ellipsis ...
    (re.compile(ur'(?<![.\u2026])\.{3,4}(?![.\u2026])', re.M | re.U), u"\u2026"),
    # en dash 123-123
    (re.compile(ur'(?<=[\d ])-(?=[\d ]|$)'), u"\u2013"),
    # en dash alphanum--alphanum
    (re.compile(ur'(?<=[^!*+,/:;<=>@\\\\_|-])--(?=[^!*+,/:;<=>@\\\\_|-])'), u"\u2013"),
    # en dash ,-
    (re.compile(ur',-'), ur",\u2013"),
    # date 23. 1. 1978
    (re.compile(ur'(?<!\d)(\d{1,2}\.) (\d{1,2}\.) (\d\d)'), ur"\1\u00a0\2\u00a0\3"),
    # date 23. 1.
    (re.compile(ur'(?<!\d)(\d{1,2}\.) (\d{1,2}\.)'), ur"\1\u00a0\2"),
    # em dash ---
    (re.compile(ur' --- '), u"\u00a0\u2014 "),
    # &nbsp; behind dash (dash stays at line end)
    (re.compile(ur' ([\u2013\u2014])', re.U), ur"\u00a0\1"),
    # left right arrow <-->
    (re.compile(ur' <-{1,2}> '), u" \u2194 "),
    # right arrow -->
    (re.compile(ur'-{1,}> '), u" \u2192 "),
    # left arrow <--
    (re.compile(ur' <-{1,}'), u" \u2190 "),
    # right arrow ==>
    (re.compile(ur'={1,}> '), u" \u21d2 "),
    # +-
    (re.compile(ur'\\+-'), ur"\u00b1"),

    # dimension sign 123 x 123...
    (re.compile(ur'(\d+)( ?)x\\2(?=\d)'), ur"\1\u00d7"),
    # dimension sign 123x
    (re.compile(ur'(?<=\d)x(?= |,|.|$)', re.M), ur"\u00d7"),
    # trademark (TM)
    (re.compile(ur'(\S ?)\(TM\)', re.I), ur"\1\u2122"),
    # registered (R)
    (re.compile(ur'(\S ?)\(R\)', re.I), ur"\1\u00ae"),
    # copyright (C)
    (re.compile(ur'\(C\)( ?\S)', re.I), ur"\u00a9\1"),
    # Euro (EUR)
    (re.compile(ur'\(EUR\)'), ur"\u20ac"),
    # (phone) number 1 123 123 123...
    (re.compile(ur'(\d) (?=\d{3})'), ur"\1\u00a0"),

    # remove intermarkup space phase 1
    (re.compile(ur'(?<=[^\s\x17])\s+([\x17-\x1F]+)(?=\s)', re.U), r"\1"),
    # remove intermarkup space phase 2
    (re.compile(ur'(?<=\s)([\x17-\x1F]+)\s+', re.U), r"\1"),

    # space between preposition and word
    (re.compile(ur"(?<=[^0-9%s])([\x17-\x1F]*[ksvzouiaKSVZOUIA][\x17-\x1F]*)\s+(?=[\x17-\x1F]*[0-9%s])" % (chars, chars), re.M | re.U | re.S), ur'\1\u00a0'),
    # nbsp space between number (optionally followed by dot) and word, symbol,
    # punctation, currency symbol
    (re.compile(ur'(?<= |\.|,|-|\+|\x16|\()([\x17-\x1F]*\d+\.?[\x17-\x1F]*)\s+(?=[\x17-\x1F]*[%' + chars + r'\u00B0-\u00be\u2020-\u214f])', re.M | re.U), ur'\1\u00a0'),
    (re.compile(ur'(?<=\d\u00A0)([\x17-\x1F]*\d+\.?[\x17-\x1F]*)\s+(?=[\x17-\x1F]*[%' + chars + r'\u00B0-\u00be\u2020-\u214f])', re.M | re.U), ur'\1\u00a0'),
    # space before last short word
    (re.compile(ur'(?<=.{50})\s+(?=[\x17-\x1F]*\S{1,6}[\x17-\x1F]*$)', re.S | re.U), u'\u00a0'),

    # double ""
    (re.compile('(?<!"|\w)"(?!\ |")(.+)(?<!\ |")"(?!")()', re.U), ur'\u201E\1\u201C'),
    # single ''
    (re.compile('(?<!\'|\w)\'(?!\ |\')(.+?)(?<!\ |\')\'(?!\')()', re.U), ur'\u201A\1\u2018'),
)


def _typography(html):
    html = lxml.html.fromstring(html)

    for el in html.iter():
        if not isinstance(el, lxml.html.HtmlElement):
            continue
        if el.tag in tag_blacklist:
            continue

        for pattern in typo_patterns:
            if el.text:
                el.text = pattern[0].sub(pattern[1], unicode(el.text))
            if el.tail:
                el.tail = pattern[0].sub(pattern[1], unicode(el.tail))

    return lxml.html.tostring(html, encoding='utf-8').decode('utf-8')


def typography(html):
    return html
