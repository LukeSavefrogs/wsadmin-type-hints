# Git hooks
This folder keeps track of all the Git hooks used.

- [`commit-msg`](commit-msg): Validates commit messages against the following rules:
  - Must not be empty
  - Must follow the [Angular standard format](https://gist.github.com/brianclements/841ea7bffdb01346392c)

To apply them after a `git clone` run the following command:
```shell
git config --local core.hooksPath .githooks/
```