"""Tests for scripts/track.py, run against a temporary copy of the memory files."""
import importlib.util
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def load_track(tmp_path: Path):
    """Copy the memory files into tmp_path and load track.py pointed at them."""
    shutil.copytree(REPO / "memory", tmp_path / "memory")
    shutil.copy(REPO / "ROADMAP.md", tmp_path / "ROADMAP.md")
    spec = importlib.util.spec_from_file_location("track", REPO / "scripts" / "track.py")
    track = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(track)
    track.ROOT = tmp_path
    track.MEM = tmp_path / "memory"
    track.STATUS = track.MEM / "STATUS.md"
    track.LOG = track.MEM / "SESSION_LOG.md"
    track.DECISIONS = track.MEM / "DECISIONS.md"
    track.LEARN = track.MEM / "LEARNINGS.md"
    track.ROADMAP = tmp_path / "ROADMAP.md"
    return track


def test_next_then_done_moves_task_to_log(tmp_path):
    t = load_track(tmp_path)
    before = len(t.get_actions(t.read(t.STATUS)))
    t.cmd_next("Fit GJR-GARCH")
    assert t.get_actions(t.read(t.STATUS))[-1] == "Fit GJR-GARCH"
    t.cmd_done(before + 1)
    assert "Fit GJR-GARCH" not in t.get_actions(t.read(t.STATUS))
    assert "DONE: Fit GJR-GARCH" in t.read(t.LOG)


def test_decision_numbering_increments(tmp_path):
    t = load_track(tmp_path)
    existing = t.read(t.DECISIONS).count("\n## D-")
    t.cmd_decide("Use log returns", why="additive over time")
    assert f"## D-{existing + 1:03d}" in t.read(t.DECISIONS)


def test_status_runs(tmp_path, capsys):
    t = load_track(tmp_path)
    t.cmd_status()
    assert "Next actions" in capsys.readouterr().out
