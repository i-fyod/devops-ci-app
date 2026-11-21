"""Minimal Flask service for CI and container deployment exercises."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/')
def index():
    """Identify this isolated educational service."""
    return jsonify(service='devops-ci-app')


@app.get('/health')
def health():
    """Expose the health contract checked by tests and smoke-test."""
    return jsonify(status='ok')
