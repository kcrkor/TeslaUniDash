"""Version and update checking functionality."""

import requests

VERSION = {"major": 0, "minor": 1, "patch": 21, "beta": 2}
VERSION_STR = f"v{VERSION['major']}.{VERSION['minor']}.{VERSION['patch']}"

if VERSION["beta"] > -1:
    VERSION_STR = f"{VERSION_STR}b{VERSION['beta']}"

GITHUB = {
    "URL": "https://api.github.com",
    "owner": "ehendrix23",
    "repo": "tesla_dashcam",
}

def check_latest_release(include_beta):
    """Checks GitHub for latest release"""

    url = f"{GITHUB['URL']}/repos/{GITHUB['owner']}/{GITHUB['repo']}/releases"

    if not include_beta:
        url = url + "/latest"
    try:
        releases = requests.get(url)
    except requests.exceptions.RequestException as exc:
        print(f"Unable to check for latest release: {exc}")
        return None

    release_data = releases.json()
    # If we include betas then we would have received a list, thus get 1st
    # element as that is the latest release.
    if include_beta:
        release_data = release_data[0]

    return release_data

def is_new_version_available(release_info, include_beta=False):
    """Check if a new version is available."""
    if release_info is None:
        return False, None

    new_version = False
    beta = ""
    if release_info.get("tag_name") is not None:
        github_version = release_info.get("tag_name").split(".")
        if len(github_version) == 3:
            # Release tags normally start with v. If that is the case
            # then strip the v.
            try:
                major_version = int(github_version[0])
            except ValueError:
                major_version = int(github_version[0][1:])

            minor_version = int(github_version[1])
            if release_info.get("prerelease"):
                # Drafts will have b and then beta number.
                patch_version = int(github_version[2].split("b")[0])
                beta_version = int(github_version[2].split("b")[1])
            else:
                patch_version = int(github_version[2])
                beta_version = -1

            if major_version == VERSION["major"]:
                if minor_version == VERSION["minor"]:
                    if patch_version == VERSION["patch"]:
                        if beta_version > VERSION["beta"] or (
                            beta_version == -1 and VERSION["beta"] != -1
                        ):
                            new_version = True
                    elif patch_version > VERSION["patch"]:
                        new_version = True
                elif minor_version > VERSION["minor"]:
                    new_version = True
            elif major_version > VERSION["major"]:
                new_version = True

    if new_version and release_info.get("prerelease"):
        beta = "beta "

    return new_version, beta 