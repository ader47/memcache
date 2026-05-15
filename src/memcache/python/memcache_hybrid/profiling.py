#!/usr/bin/env python
# coding=utf-8
# Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
# MemCache_Hybrid is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

"""Helpers for collecting memcache traces alongside vLLM profiling."""

import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Optional

_DEFAULT_METRICS_URL = "http://127.0.0.1:8000/metrics/ptracer"
_ACTIVE_SESSION: Optional[Dict[str, str]] = None


def _is_enabled() -> bool:
    return os.getenv("MEMCACHE_PROFILE_WITH_VLLM", "1").upper() not in {
        "0",
        "FALSE",
        "NO",
        "OFF",
    }


def _metrics_url() -> str:
    return os.getenv("MEMCACHE_PROFILE_METRICS_URL", _DEFAULT_METRICS_URL)


def _resolve_output_dir(output_dir: Optional[str]) -> Path:
    raw_dir = (
        output_dir
        or os.getenv("MEMCACHE_PROFILE_DIR")
        or os.getenv("VLLM_TORCH_PROFILER_DIR")
        or os.getcwd()
    )
    path = Path(raw_dir).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path


def _read_ptracer_snapshot() -> str:
    url = _metrics_url()
    try:
        with urllib.request.urlopen(url, timeout=2) as response:
            return response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return f"failed to read {url}: {exc}\n"


def _write_snapshot(output_dir: Path, name: str) -> None:
    snapshot = _read_ptracer_snapshot()
    timestamp_ns = time.time_ns()
    path = output_dir / f"{name}.{timestamp_ns}.ptracer.txt"
    path.write_text(snapshot, encoding="utf-8")


def start_profile(output_dir: Optional[str] = None, profile_prefix: Optional[str] = None) -> None:
    """Start a memcache profiling sidecar for a vLLM profile window."""
    global _ACTIVE_SESSION
    if not _is_enabled():
        return
    resolved_dir = _resolve_output_dir(output_dir)
    prefix = profile_prefix or "memcache"
    _ACTIVE_SESSION = {
        "output_dir": str(resolved_dir),
        "prefix": prefix,
    }
    _write_snapshot(resolved_dir, f"{prefix}.start")


def stop_profile() -> None:
    """Stop the memcache profiling sidecar and dump a final ptracer snapshot."""
    global _ACTIVE_SESSION
    if not _is_enabled() or _ACTIVE_SESSION is None:
        return
    output_dir = Path(_ACTIVE_SESSION["output_dir"])
    prefix = _ACTIVE_SESSION["prefix"]
    _write_snapshot(output_dir, f"{prefix}.stop")
    _ACTIVE_SESSION = None
