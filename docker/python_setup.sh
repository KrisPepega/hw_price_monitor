#!/bin/sh

cd /usr/src/app
pip install --no-cache-dir --upgrade -r ./requirements.txt
pip list >> installed

uvicorn core.api.app:app --host 0.0.0.0 --port 80