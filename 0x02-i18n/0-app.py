#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, render_template


@app.route('/')
def index:
    """ route that outputs hello world """
    return render_template("index.html")
