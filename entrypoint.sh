#!/bin/bash
set -e

python3 scripts/db_setup.py
python3 scripts/import_data.py

CMD_STR="uvicorn app.main:app --host 0.0.0.0 --port 8000"

exec /bin/bash -c "$CMD_STR"