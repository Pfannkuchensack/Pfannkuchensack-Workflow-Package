"""Pfannkuchensacks Workflow Package.

InvokeAI loads this file with `importlib.util.spec_from_file_location(pack_name, __init__.py)`
and then `exec_module`. Because the spec is built from a bare file path, the module is not
guaranteed to be set up as a package with a `__path__`, so a relative import
(`from .pfannis_dummy_node import ...`) is not safe here. Loading the sibling module by
explicit file path always works and keeps the node in its own file.
"""

import importlib.util
import sys
from pathlib import Path

_PACK_DIR = Path(__file__).parent
_PACK_NAME = __name__


def _load_sibling(module_filename: str) -> None:
    """Import a module that sits next to this __init__.py, under this pack's namespace."""
    module_name = f"{_PACK_NAME}.{Path(module_filename).stem}"
    if module_name in sys.modules:
        return
    spec = importlib.util.spec_from_file_location(module_name, _PACK_DIR / module_filename)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {module_filename} from {_PACK_DIR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


_load_sibling("pfannis_dummy_node.py")
