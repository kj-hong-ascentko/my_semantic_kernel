from semantic_kernel.template_engine.blocks.symbols import Symbols

def _is_blank_space(self, c: str) -> bool:
    return c in (
        Symbols.SPACE,
        Symbols.NEW_LINE,
        Symbols.CARRIAGE_RETURN,
        Symbols.TAB,
    )

def _can_be_escaped(self, c: str) -> bool:
    return c in (
        Symbols.DBL_QUOTE,
        Symbols.SGL_QUOTE,
        Symbols.ESCAPE_CHAR,
    )
