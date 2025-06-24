# ai-ethics

This repository contains Python code to audit and analyze racial bias in the COMPAS Recidivism Dataset using IBM’s AI Fairness 360 toolkit. The audit identifies disparities in risk assessment scores between Caucasian and African-American defendants, with visualizations and a summary report.

## Overview

Risk assessment tools like COMPAS are widely used in criminal justice to predict recidivism risk. However, concerns about racial bias have been raised, particularly regarding false positive rates for African-American defendants.

This project:

- Loads and preprocesses the COMPAS dataset following ProPublica’s methodology.
- Uses AI Fairness 360 to calculate fairness metrics such as False Positive Rate, Disparate Impact, and Average Odds Difference.
- Visualizes disparities in false positive rates and risk score distributions by race.
- Generates a textual audit report summarizing findings and recommendations.

## Dataset

The dataset used is the COMPAS Recidivism Scores dataset provided by ProPublica:
[https://github.com/KerryNK/ai-ethics.git](https://github.com/KerryNK/ai-ethics.git)

## Features

- Data filtering and preprocessing for Caucasian and African-American groups.
- Calculation of key fairness metrics using AI Fairness 360.
- Bar plot of false positive rates by race.
- Box plot showing distribution of COMPAS risk scores by race.
- Function to generate a markdown-formatted audit report.
