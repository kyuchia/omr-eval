#####------------- run_mupix_comparisons.sh

#!/bin/bash

# Define excerpt numbers
excerpts=(01 02 03 04 05 06 07 08 09 10)

# Define tools
tools=("soundslice" "photoscore" "playscore2" "newzik")

# Loop through tools and excerpts
for tool in "${tools[@]}"; do
  for ex in "${excerpts[@]}"; do

    # Skip excerpt02 and excerpt03 for newzik
    if [[ "$tool" == "newzik" && ( "$ex" == "02" || "$ex" == "03" ) ]]; then
      echo "Skipping ${tool} excerpt${ex}.xml (file not available)"
      continue
    fi

    # Run Mupix comparison
    echo "Running Mupix for ${tool} excerpt${ex}.xml..."
    mupix -pT compare ./ground_truth/excerpt${ex}.xml ./omr_outputs/${tool}/excerpt${ex}.xml > ./mupix_results/${tool}_excerpt${ex}.json
  done
done


