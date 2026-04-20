#!/usr/bin/env bash
set -euo pipefail

PROTO_DIR="$(cd "$(dirname "$0")" && pwd)"
PROTO_FILE="${PROTO_DIR}/rag.proto"

# Java — Gradle handles this now
echo "Java: use './gradlew build' instead"

# Python 생성
PYTHON_OUT="${PROTO_DIR}/gen-python"
rm -rf "${PYTHON_OUT}"
mkdir -p "${PYTHON_OUT}/myrag_proto/v1"

python -m grpc_tools.protoc \
  --proto_path="${PROTO_DIR}" \
  --python_out="${PYTHON_OUT}" \
  --grpc_python_out="${PYTHON_OUT}" \
  --pyi_out="${PYTHON_OUT}" \
  "${PROTO_FILE}"

touch "${PYTHON_OUT}/myrag_proto/__init__.py"
touch "${PYTHON_OUT}/myrag_proto/v1/__init__.py"

echo "Generated:"
echo "  Python → ${PYTHON_OUT}"
