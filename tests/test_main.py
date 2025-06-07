import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import builtins
from src.main import run


def test_birth(capsys):
    run()
    captured = capsys.readouterr()
    assert "born" in captured.out


def test_oracle_output(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['main', '--oracle'])
    outputs = []
    def fake_print(msg):
        outputs.append(msg)
    monkeypatch.setattr(builtins, 'print', fake_print)
    run()
    assert outputs
    assert any(word in outputs[0] for word in ["You will", "Today is", "Your keyboard"])
