#!/bin/bash

CLUSTER_ID="j-3QGMVQB9E973G"

echo "Agregando Step al cluster: $CLUSTER_ID"

aws emr add-steps \
  --cluster-id "$CLUSTER_ID" \
  --steps file:///home/manuel/proyecto3Telematica/mapreduce-app/step.json

echo ""
echo "Step agregado. Monitorea el progreso con:"
echo "aws emr list-steps --cluster-id $CLUSTER_ID"
