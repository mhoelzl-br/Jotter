# %%
from pathlib import Path
import os


# %% [markdown]
#
# # Utilities for Data Processing
#
# ## Development Mode
# To speed up iteration in development mode we reduce the size of
# datasets, etc.


class DevMode:
    """Changing behavior during development and runtime

    An instance of this class can be used to globally control behavior that
    should differ during interactive development and production, e.g., the size
    of data sets used for training machine learning models."""

    def __init__(self) -> None:
        self._is_active = False

    @property
    def is_active(self) -> bool:
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        self._is_active = value


# %%
"""Global variable used to control dev mode."""
dev_mode = DevMode()

# %% [markdowm]
#
# ## Path Utilities
#
# Support for finding the data directory

DATA_PATH_VAR = "DATA_PATH"

# %%
def compute_data_path(start_path=None, data_folder_name="data"):
    """Try to compute an absolute path name for data files.

    This tries to locate a folder named `data_folder_name` (`data` by default).

    - If `start_path` is given and `data_folder_name` is truthy, find a
      subfolder of `start_path` that matches the name and is in a likely
      position (either in the `data`, `src`, or `src/data` subdirectory.
    - If no `start_path` is given and and environment variable named `DATA_PATH`
      exists, use its value (without further processing).
    - Otherwise perform the same search as for `start_path` starting from the
      current directory."""
    env_path = os.environ.get(DATA_PATH_VAR)
    if start_path:
        if data_folder_name:
            path = start_path.absolute()
        else:
            return start_path
    elif env_path:
        # Don't search for a data folder if the user set it up in the environment
        return Path(env_path).absolute()
    else:
        path = Path().absolute()

    if path.parts[-1] == data_folder_name:
        return path
    elif (path / data_folder_name).exists():
        return path / data_folder_name
    elif (path / "data" / data_folder_name).exists():
        return path / "data" / data_folder_name
    elif (path / "src" / data_folder_name).exists():
        return path / "src" / data_folder_name
    else:
        raise FileNotFoundError("Cannot determine data path.")
