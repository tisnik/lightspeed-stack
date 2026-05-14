# Releasing

<!-- vim-markdown-toc GFM -->

* [Semantic versioning](#semantic-versioning)
    * [Rules (concise)](#rules-concise)
* [Prerequisites](#prerequisites)
* [Update version in sources](#update-version-in-sources)
* [Regenerate OpenAPI specification](#regenerate-openapi-specification)
* [Publishing the Python package on PyPi](#publishing-the-python-package-on-pypi)
    * [Cleanup the whole repository](#cleanup-the-whole-repository)
    * [Build the distribution archive](#build-the-distribution-archive)
    * [Upload distribution archives into Python registry](#upload-distribution-archives-into-python-registry)
    * [Check packages on PyPI and Test PyPI](#check-packages-on-pypi-and-test-pypi)
* [New tag and release on GitHub](#new-tag-and-release-on-github)
    * [Create a new tag](#create-a-new-tag)
    * [Update link in `README.md`](#update-link-in-readmemd)

<!-- vim-markdown-toc -->

## Semantic versioning

Each LCORE release is identified by semantic version.

Semantic Versioning (SemVer) is a versioning scheme that conveys meaning about
changes in a release using a three-part number: `MAJOR.MINOR.PATCH`. In LCORE it
is possible to append a *release candidate* number in a form `MAJOR.MINOR.PATCHrcNUMBER`.



### Rules (concise)

* Format: MAJOR.MINOR.PATCH (e.g., 2.5.1).

* Increment MAJOR when you make incompatible API changes.

* Increment MINOR when you add functionality in a backwards-compatible manner.

* Increment PATCH when you make backwards-compatible bug fixes.

* Release candidates, e.g. 0.6.0rc1 (there is no hyphen!)

* Build metadata: append a plus and metadata ignored for precedence (e.g.,
  1.0.0+20130313144700).

* Precedence: Compare MAJOR, then MINOR, then PATCH numerically; pre-release
  versions have lower precedence than the associated normal version.

## Prerequisites

* Access to https://github.com/lightspeed-core/lightspeed-stack as owner or maintainer
* Access token to https://pypi.org/ and/or to https://test.pypi.org/py
* `git`
* text editor
* basic file system manipulation tools (`cp`, `rm`)

## Update version in sources

First step is to update version in sources. The version is stored in the file `src/version.py`:
https://github.com/lightspeed-core/lightspeed-stack/blob/main/src/version.py

Then update the version in other files, especially in tests:

1. src/observability/README.md
1. tests/e2e/features/info.feature
1. tests/integration/endpoints/test_rlsapi_v1_integration.py
1. tests/unit/app/endpoints/conftest.py
1. tests/unit/observability/test_rlsapi.py

NOTE: there's a task to make this step easier by using the same `version.py` everywhere:
LCORE-2248: Use only one version value stored in version.py everywhere across the LCORE sources and tests
https://redhat.atlassian.net/browse/LCORE-2248

## Regenerate OpenAPI specification

It is needed to generate OpenAPI specification that is stored in `docs/openapi.json`. In order to do it, run the following command:

```bash
make schema
```

NOTE: there's a task to automate these steps:
LCORE-1647: Automate versioning and changelog generation
https://redhat.atlassian.net/browse/LCORE-1647

## Publishing the Python package on PyPi

To publish the service as an Python package on PyPI to be installable by anyone
(including Konflux hermetic builds), perform the following three steps:

### Cleanup the whole repository

Source and tests folders must contain just source files and README.mds, nothing else. Make sure that all `__pycache__` and `.mypy_cache` directories are deleted (the latest are hidden on Unit systems!)

### Build the distribution archive

```bash
make distribution-archives
```

This command should finish with message:

```text
Successfully built lightspeed_stack-{version}.tar.gz and lightspeed_stack-{version}-py3-none-any.whl
```

Please double check that the `{version}` really contains the correct version number.
Also please make sure that the archive was really built to avoid publishing older one.

### Upload distribution archives into Python registry

```bash
make upload-distribution-archives      
```

The Python registry to where the package should be uploaded can be configured
by changing `PYTHON_REGISTRY`. It is possible to select `pypi` or `testpypi`.

You might have your API token stored in file `~/.pypirc`. That file should have
the following form:

```ini
[testpypi]
  username = __token__
  password = pypi-{your-API-token}

[pypi]
  username = __token__
  password = pypi-{your-API-token}
```

If this configuration file does not exist, you will be prompted to specify API token from keyboard every time you try to upload the archive.

### Check packages on PyPI and Test PyPI

* https://pypi.org/project/lightspeed-stack/
* https://test.pypi.org/project/lightspeed-stack/

## New tag and release on GitHub

### Create a new tag

1. Open https://github.com/lightspeed-core/lightspeed-stack in a web browser
1. Go to the *Releases* section and click on *"Draft a new release"*
1. Create a tag, for example `0.6.0rc1` and fill-in release name such as `Lightspeed Stack version 0.6.0rc1`
1. Press the button *"Create a release notes"*
1. Press the button *"Publish release"*

### Update link in `README.md`

At the beggining of `README.md` there's a line:

```text
[![Tag](https://img.shields.io/github/v/tag/lightspeed-core/lightspeed-stack)](https://github.com/lightspeed-core/lightspeed-stack/releases/tag/0.5.0)
```

Update the link on this line, i.e. replace, for example, `0.5.0` by `0.6.0rc1`

