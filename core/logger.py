import os
import json
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'anima_exo.jsonl')

def _ensure_dir():
    os.makedirs(LOG_DIR, exist_ok=True)

def _make_logger():
    _ensure_dir()
    logger = logging.getLogger('anima_exo')
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    # Rotating file handler writes JSON-lines; we also add a StreamHandler for console
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(file_handler)
    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    logger.addHandler(ch)
    return logger

def _log(record: dict):
    logger = _make_logger()
    record.setdefault('ts', datetime.utcnow().isoformat() + 'Z')
    logger.info(json.dumps(record, ensure_ascii=False))

def log_input(source: str, data: str):
    _log({'type': 'input', 'level': 'INFO', 'source': source, 'data': data})

def log_decision(decision: str):
    _log({'type': 'decision', 'level': 'INFO', 'decision': decision})

def log_action(action: str, result: str = ''):
    _log({'type': 'action', 'level': 'INFO', 'action': action, 'result': result})

def log_guardian(blocked: bool, reason: str = ''):
    _log({'type': 'guardian', 'level': 'WARNING' if blocked else 'INFO', 'blocked': bool(blocked), 'reason': reason})
