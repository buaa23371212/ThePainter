from src.main.python.terminal_logger.logger import log

def title(show: bool, message: str, show_caller: bool = True) -> None:
    """
    Log a title message.

    :param show: Whether to show the log.
    :param message: The message to log.
    :param show_caller: Whether to show the caller information.
    """
    source_file = None
    log("TITLE", show, message, source_file)

def step(show: bool, message: str, show_caller: bool = True) -> None:
    """
    Log a step message.

    :param show: Whether to show the log.
    :param message: The message to log.
    :param show_caller: Whether to show the caller information.
    """
    source_file = None
    log("STEP", show, message, source_file)