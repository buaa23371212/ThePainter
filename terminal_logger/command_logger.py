import inspect
import os
from terminal_logger.logger import log

def title(show: bool, message: str, show_caller: bool = False) -> None:
    source_file = None
    log("TITLE", show, message, source_file)

def step(show: bool, message: str, show_caller: bool = False) -> None:
    source_file = None
    log("STEP", show, message, source_file)