import difflib


def generate_diff(old, new):

    diff = difflib.HtmlDiff().make_file(
        old.splitlines(),
        new.splitlines(),
        fromdesc='Original',
        todesc='Optimized'
    )

    return diff