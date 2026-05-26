import argparse

from ai_code_engine.lsp_server import run_server


parser = argparse.ArgumentParser()

parser.add_argument("--server", action="store_true")
parser.add_argument("--watch", action="store_true")

args = parser.parse_args()


if args.server:
    run_server()

if args.watch:
    import ai_code_engine.watcher