---
name: aiolyric-release
description: Release aiolyric to PyPI. Use when preparing or publishing a GitHub release, choosing the next version, writing release notes, checking what a release published, or debugging .github/workflows/release.yml.
---

# Releasing aiolyric

Publishing a non-prerelease GitHub release runs `.github/workflows/release.yml`, which builds the package and publishes it to PyPI as `aiolyric`.

Releasing is a public, irreversible publish. Create a tag or release only when the user asks, and use their chosen version.

## Versions

- Tags are the exact version with no `v` prefix, as in `2.1.2`.
- Nothing needs bumping before a release. `version` in `pyproject.toml` stays `0.0.0`, and the workflow sets it from the tag with `uv version`.
- Patch for fixes, dependency updates and maintenance, minor for new fields or methods, major for breaking API changes such as renamed properties or removed methods.

## Release

Check `master` has passed the Check workflow first, so the release builds the same commit that passed.

### Notes

Write the release notes by hand rather than using GitHub's generated list. Read `git log <previous version>..<master commit>` and the previous release (`gh release view <version> --json body -q .body`), and follow the `writing-style` skill:

- One or two sentences on what the release does.
- `##` sections such as `Fixes`, `Features`, `Dependencies` and `Maintenance`.
- Bullets that start with a verb and name real identifiers in backticks. Link PRs as `(#123)`.
- Credit first-time contributors under `New contributors`.
- End with `**Full Changelog**: https://github.com/timmo001/aiolyric/compare/<previous version>...<version>`.

### Publish

```bash
gh release create <version> --target <master commit sha> --title <version> --notes-file notes.md
```

`--target` needs the full 40-character SHA (`git rev-parse <sha>`). GitHub rejects a short one.

To fix notes after publishing, `gh release edit <version> --notes-file notes.md`.

## Checks

```bash
gh run list -R timmo001/aiolyric --workflow release.yml --limit 1
curl -s https://pypi.org/pypi/aiolyric/json | jq -r .info.version
```

## Setup

PyPI trusted publishing on `aiolyric` must allow `timmo001/aiolyric`, workflow `release.yml`, no environment. It only needs redoing if the workflow is renamed.

## After a release

Home Assistant pins aiolyric in its `lyric` integration. Bumping it there is a separate Home Assistant core pull request, done only when the user asks.
