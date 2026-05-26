import ast

def is_valid_python(code):

    try:
        ast.parse(code)
        return True

    except Exception:
        return False