# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/uiza/#history


## 1.0.0

### New Feature
- Wrap user service.
- Wrap entity service.
- Wrap category service.
- Wrap storage service.
- Wrap live streaming service.
- Wrap callback service.
- Wrap analytic service.

### Documentation
- N/A


## 1.0.1

### Changed
- In live streaming service:

    - Instead function `get_view_feed` to `get_view`.
    - Instead Object `LiveStreaming` to `Live`.
- In storage service:
    - Instead function `create` to `add`.
    - Instead function `delete` to `remove`.

### Documentation
- N/A


## 1.1.0

### Changed
- In analytic service:
    - Add param `type` to function `get_line`.
- In user service:
    - Change value of field `isAdmin`: Set this account isAdmin or not (1 = Yes, 0 = No)
    - Instead function `update_password` to `change_password`.

### Documentation
- N/A


## 1.1.1

### Fixed
- In category service:
    - Fix delete relation category

### Documentation
- N/A


## 1.1.2

### Changed
- Update docs

### Documentation
- N/A
