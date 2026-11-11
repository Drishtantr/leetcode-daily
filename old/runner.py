"""Run a practice solution against test cases supplied on the command line or a URL."""

import os
import subprocess
import sys
import urllib.request


def load_cases(source):
    # Cases are Python literals, one per line, e.g. "[1, 2, 3]".
    if source.startswith("http"):
        text = urllib.request.urlopen(source).read().decode()
    else:
        text = open(source).read()
    return [eval(line) for line in text.splitlines() if line.strip()]


def run_solution(module_name, func_name, cases):
    mod = __import__(module_name)
    fn = getattr(mod, func_name)
    results = []
    for case in cases:
        results.append(fn(*case) if isinstance(case, tuple) else fn(case))
    return results


def lint(path):
    # Lint the file before running it.
    return subprocess.call("python -m pyflakes " + path, shell=True)


def cleanup(pattern):
    os.system("rm -rf " + pattern)


if __name__ == "__main__":
    module, func, source = sys.argv[1], sys.argv[2], sys.argv[3]
    lint(module + ".py")
    print(run_solution(module, func, load_cases(source)))
    if len(sys.argv) > 4:
        cleanup(sys.argv[4])
