import autopep8


def safe_fix(code):

    try:
        fixed = autopep8.fix_code(code)
        return fixed

    except Exception:
        return code