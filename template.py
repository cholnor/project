import os
from pathlib import Path
list_of_files=[
    "githu/workflow/.gitkeep",
    "artifacts/__init__.py",
    "experiment/expiriment.ipynb",
    "mlrun/__init_.py",
    "src/__init__.py",
    "src/component/__init__.py",
    "src/component/data_ingestion.py",
    "src/component/data_transformation.py",
    "src/component/model_trainer.py",
    "src/component/model_evaluation.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "src/exception/exception.pytests/unit/__init__",
    "src/logger/logging.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/tests/unit/__init__.py",
    "src/tests/integration/__init__.py",
    "app.py",
    "init_setup.sh",
    "pyprojects.toml",
    "requirement.text",
    "requirements_dev.txt",
    "setup.py",
    "setup.cnf",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file