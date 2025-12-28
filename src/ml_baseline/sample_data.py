from pathlib import Path
import numpy as np


def make_sample_feature_table(*, root: Path | None = None,
                              n_users: int= 50,
                              seed: int= 0):
    
    # paths = Path.from_repo_root() if root is None else Path(root=root)
    # paths.data_processed_dir.mkdir(paren)
    
    paths = Path(root=root)
    
    rng = np