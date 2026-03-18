"""Module for downloading Marimo themes from a GitHub repository."""

from __future__ import annotations

import base64
from typing import TYPE_CHECKING

import requests

from .util import get_themes_dir

if TYPE_CHECKING:
    from pathlib import Path


def _get_api_url(repo_url: str) -> str:
    """Convert GitHub repo URL to API URL."""
    return repo_url.replace(
        "https://github.com", "https://api.github.com/repos"
    )


def _download_theme(
    api_base_url: str, theme_folder: dict, themes_dir: Path
) -> None:
    """Download a single theme CSS file."""
    theme_name = theme_folder["name"]
    css_file_url = (
        f"{api_base_url}/contents/themes/{theme_name}/{theme_name}.css"
    )

    css_response = requests.get(css_file_url, timeout=10)
    css_response.raise_for_status()

    css_content = base64.b64decode(css_response.json()["content"]).decode(
        "utf-8"
    )

    css_path = themes_dir / f"{theme_name}.css"
    with css_path.open("w") as f:
        f.write(css_content)

    print(f"Downloaded: {css_path}")


def download_themes(
    repo_url: str = "https://github.com/Haleshot/marimo-themes",
) -> Path | None:
    """
    Download Marimo themes CSS files from GitHub repository.

    Args:
        repo_url (str): GitHub repository URL

    Returns:
        Path: Local directory where themes are stored

    """
    themes_dir = get_themes_dir()
    api_base_url = _get_api_url(repo_url)
    themes_api_url = f"{api_base_url}/contents/themes"

    try:
        response = requests.get(themes_api_url, timeout=10)
        response.raise_for_status()
        theme_folders = response.json()

        for theme_folder in theme_folders:
            if theme_folder["type"] == "dir":
                _download_theme(api_base_url, theme_folder, themes_dir)

    except requests.RequestException as e:
        print(f"Error downloading themes: {e}")
        return None

    return themes_dir
