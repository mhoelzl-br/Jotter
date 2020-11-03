# %% [markdown]
#
# # Support for interactive sessions
#
# We want to use the code both in interactive session where we want more output,
# etc., and for batch processing. This file contains utilities for writing code
# that outputs interesting information when being run interactively without
# being annoying when batch processing data.

# %%
from IPython.core.display import display
from pprint import pprint

# %%
class Session:
    """"Different behavior for interactive and batch use."""

    def __init__(self) -> None:
        self._is_interactive = False

    @property
    def is_interactive(self):
        # TODO: Maybe find a way to figure out whether we are in IPython or a
        # notebook?
        return self._is_interactive  # and ("get_ipython" in globals())

    @is_interactive.setter
    def is_interactive(self, value=True):
        self._is_interactive= value


# %%
session = Session()


# %%
def display_interactive(obj):
    if session.is_interactive:
        display(obj)


# %%
def pprint_interactive(obj):
    if session.is_interactive:
        pprint(obj)


# %%
def print_interactive(*obj):
    if session.is_interactive:
        print(*obj)
