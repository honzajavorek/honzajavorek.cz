import re
import contextlib

from lxml import html


@contextlib.contextmanager
def modify_html(content, prop='_content'):
    html_string = getattr(content, prop)
    html_tree = html.fromstring(html_string)

    yield html_tree

    html_string = html.tostring(html_tree, encoding='unicode')
    html_string = re.sub(r'%7B(\w+)%7D', r'{\1}', html_string)
    html_string = re.sub(r'%7C(\w+)%7C', r'|\1|', html_string)
    setattr(content, prop, html_string)


def wrap_element(element, wrapper_element):
    element.addprevious(wrapper_element)
    wrapper_element.insert(0, element)
    return wrapper_element
