# Changelog

All notable, unreleased changes to this project will be documented in this file. For the released
changes, please visit
the [Releases](https://gitlab.com/true-web-app/true-checker/true-checker-python/-/releases) page.

## [Unreleased]

### Features

### Bugs

### Breaking

### Misc


## v2021.10.11

### Bugs

- return `NotFound` on 404 status instead of `BadRequest`


## v2021.10.10

### Bugs

- correct non-json response (for errors)
- you shouldn't pass token to TrueChecker (but you can pass it with a request)


## v2020.4.7

### Bugs

- enabled uvloop if installed
- test is no longer fails on a quick tasks

### Misc

- python requirements downgraded to 3.7
- add codecov.io support
- doc strings added

## v2020.4.6

### Features

- Implemented API v.1.1.0 client
- Added README.md examples
