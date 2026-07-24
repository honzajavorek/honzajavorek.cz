def process_code_blocks(html_tree):
    for pre in html_tree.findall('.//div/pre'):
        pre.getparent().tag = 'pre'
        pre.tag = 'code'
