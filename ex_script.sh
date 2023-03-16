#!/bin/bash
cd example_pipeline
poetry run pipeline run
head -n10 norm.csv