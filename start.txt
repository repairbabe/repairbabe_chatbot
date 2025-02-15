#!/bin/bash
gunicorn -w 4 -b 0.0.0.0:5000 repair_babe_bot:app
