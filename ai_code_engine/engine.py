import copy
import os

from ai_code_engine.analyzer import CodeAnalyzer
from ai_code_engine.ai import AIEngine
from ai_code_engine.validator import is_valid_python
from ai_code_engine.optimizer import safe_fix
from ai_code_engine.cache import CacheManager
from ai_code_engine.cli_report import show_report

OPTIMIZED_DIR = "optimized"
BACKUP_DIR = "backups"

os.makedirs(OPTIMIZED_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)


def clean(code):

    if not code:
        return ""

    return (
        code
        .replace("```python", "")
        .replace("```", "")
        .strip()
    )


def process_file(code, path):

    # TEMPORARILY DISABLE CACHE
    cached = None

    static = CodeAnalyzer(code).analyze()

    ai = AIEngine.analyze(code) or {}

    fixed = clean(ai.get("fixed_code", code))
    optimized = clean(ai.get("optimized_code", code))

    print("\n========== AI DEBUG ==========")
    print("ORIGINAL:\n", code)
    print("\nOPTIMIZED:\n", optimized)
    print("================================\n")

    # PRIORITY → OPTIMIZED CODE
    if (
        optimized
        and optimized.strip() != code.strip()
        and is_valid_python(optimized)
    ):

        final = optimized
        print("✅ USING OPTIMIZED CODE")

    elif is_valid_python(fixed):

        final = fixed
        print("⚠ USING FIXED CODE")

    else:

        final = safe_fix(code)
        print("❌ USING SAFE FIX")

    filename = os.path.basename(path)

    optimized_path = os.path.join(
        OPTIMIZED_DIR,
        f"optimized_{filename}"
    )

    with open(
        optimized_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(final)

    result = {
        "file": path,
        "static": static,
        "ai": ai,
        "optimized": final,
        "optimized_path": optimized_path
    }

    show_report(result)

    return result