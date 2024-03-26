
import os
from pathlib import Path
list_of_files=[
    "githu/workflow/.gitkeep",
    "src/__init__.py",
    "src/component/data_ingestion.py",
    "src/component/data_transformation.py",
    "src/component/model_trainer.py",
    "src/component/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exxception.py",
    "src/tests/unit/__init__.py",
    "src/tests/integration/__init__.py",
    "init_setup.sh",
    "requirement.text",
    "setup.py",
    "setup.cnf",
    "pyprojects.toml",
    "tox.ini",
    "experiment/experiment.ipynb",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file