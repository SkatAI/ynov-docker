# Use a lightweight base image
FROM alpine:3.14

# Install necessary dependencies
RUN apk add --no-cache git g++ make cmake

# Clone and build llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    make

# Download a small, quantized model (example: GGML version of GPT-J 6B)
RUN wget https://huggingface.co/ocordeiro/ggml-gpt-j-6b-q4_0/blob/main/gpt-j-ggml-model-q4_0.bin -O model.bin
# RUN wget https://huggingface.co/ggerganov/ggml/blob/main/ggml-shakespeare-768x12-q8_0.bin -O model.bin

# Set up a script to run the model
# COPY run.sh /run.sh
# RUN chmod +x /run.sh

# Set the entrypoint
# ENTRYPOINT ["/run.sh"]

# Contents of run.sh
# !/bin/sh
# ./llama.cpp/main -m model.bin -p "Once upon a time" -n 100
