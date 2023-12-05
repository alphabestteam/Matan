#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Give Output file path"
  exit 1
fi

OUTPUT_FILE="$1"

RUNNING_PODS=$(kubectl get pods --field-selector=status.phase=Running -o=jsonpath='{range .items[*]}{.metadata.name} ({.status.phase})\n{end}')

echo -e "$RUNNING_PODS" >> "$OUTPUT_FILE"

#./running_pods.sh ./test.txt 
