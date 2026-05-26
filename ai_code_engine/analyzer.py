import ast
class CodeAnalyzer:

    def __init__(self, code):
        self.code = code

    def analyze(self):

        result = {
            "issues": [],
            "risk": 0,
            "complexity": 0
        }

        try:
            tree = ast.parse(self.code)

            loops = sum(
                isinstance(n, (ast.For, ast.While))
                for n in ast.walk(tree)
            )

            funcs = sum(
                isinstance(n, ast.FunctionDef)
                for n in ast.walk(tree)
            )

            imports = sum(
                isinstance(n, (ast.Import, ast.ImportFrom))
                for n in ast.walk(tree)
            )

            result["complexity"] = loops + funcs + imports

            for node in ast.walk(tree):

                if (
                    isinstance(node, ast.Call)
                    and getattr(node.func, 'id', '') == 'eval'
                ):
                    result["issues"].append("Unsafe eval detected")
                    result["risk"] += 50

                if (
                    isinstance(node, ast.Call)
                    and getattr(node.func, 'id', '') == 'exec'
                ):
                    result["issues"].append("Unsafe exec detected")
                    result["risk"] += 50

            if loops > 5:
                result["issues"].append("High loop complexity")

            if funcs > 10:
                result["issues"].append("Too many functions")

            return result

        except Exception:
            result["issues"].append("Syntax error")
            result["risk"] = 100
            return result