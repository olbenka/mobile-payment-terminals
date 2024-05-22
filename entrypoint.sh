#!/bin/sh

# Запуск consumer.py в фоновом режиме
python3 consumer.py &

# Запуск screen.py
python3 screen.py
