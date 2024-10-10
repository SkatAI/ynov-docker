#!/bin/sh

# Set default values
MODEL_PATH=${MODEL_PATH:-"/model.bin"}
PROMPT=${PROMPT:-"Once upon a time"}
NUM_TOKENS=${NUM_TOKENS:-100}

# Run the model
echo "Running model with prompt: $PROMPT"
./llama.cpp/main -m $MODEL_PATH -p "$PROMPT" -n $NUM_TOKENS