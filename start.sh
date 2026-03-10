#!/bin/bash

# Install groq to user directory
python3 -m pip install --user groq packaging

# Get the user site-packages directory
USER_SITE=$(python3 -m site --user-site)

# Add it to PYTHONPATH
export PYTHONPATH="$USER_SITE:$PYTHONPATH"

# Run streamlit
python3 -m streamlit run main.py --server.address=0.0.0.0 --server.port=8080