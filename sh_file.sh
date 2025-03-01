#!/bin/bash
echo "Activating virtual environment"
source /home/aws2024/myenv/bin/activate
echo "Virtual environment activated"

echo "run serial script"
python /home/aws2024/aws2024_code/raspberryPI/raspberryPI_ver3.1.1.py
