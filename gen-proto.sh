#!/usr/bin/env bash
set -euo pipefail

PROTO_DIR="$(cd "$(dirname "$0")" && pwd)"
PROTO_FILE="${PROTO_DIR}/rag.proto"

# Java 생성
JAVA_OUT="${PROTO_DIR}/gen-java"
mkdir -p "${JAVA_OUT}"
protoc \
  --proto_path="${PROTO_DIR}" \
  --java_out="${JAVA_OUT}" \
  --grpc-java_out="${JAVA_OUT}" \
  "${PROTO_FILE}"

# Python 생성
PYTHON_OUT="${PROTO_DIR}/gen-python"
mkdir -p "${PYTHON_OUT}"
python -m grpc_tools.protoc \
  --proto_path="${PROTO_DIR}" \
  --python_out="${PYTHON_OUT}" \
  --grpc_python_out="${PYTHON_OUT}" \
  --pyi_out="${PYTHON_OUT}" \
  "${PROTO_FILE}"

echo "Generated:"
echo "  Java   → ${JAVA_OUT}"
echo "  Python → ${PYTHON_OUT}"
