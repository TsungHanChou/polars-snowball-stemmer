from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl
from polars.plugins import register_plugin_function

from polars_snowball_stemmer._internal import __version__ as __version__

if TYPE_CHECKING:
    from polars_snowball_stemmer.typing import IntoExprColumn

LIB = Path(__file__).parent

def snowball_stem(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="snowball_stem",
        is_elementwise=True,
    )

