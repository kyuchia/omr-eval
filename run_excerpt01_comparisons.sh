#!/bin/bash

# Define variables
GROUND_TRUTH="./ground_truth/excerpt01.xml"
TOOLS=("soundslice" "newzik" "photoscore" "playscore2")
OUTPUT_DIR="./mupix_results"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run comparisons
for TOOL in "${TOOLS[@]}"; do
  OMR_OUTPUT="./omr_outputs/${TOOL}/excerpt01.xml"
  OUTPUT_JSON="${OUTPUT_DIR}/${TOOL}_excerpt01.json"
  mupix -pT compare "$GROUND_TRUTH" "$OMR_OUTPUT" > "$OUTPUT_JSON"
  echo "Saved result for $TOOL to $OUTPUT_JSON"
done
