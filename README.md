# Broken mypy example

## Set up on master branch

If you're switching back to `master` branch, run this first: `pre-commit uninstall`

```bash
cd backend
pre-commit install
pre-commit run --all-files
```

## Set up on 

Check the branch `working-example` to see that it can work if not in a directory
But need to run:

```bash
cd ..
pre-commit uninstall
git switch working-example
pre-commit install
```
