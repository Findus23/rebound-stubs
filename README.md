# PEP 561 compatible type-hint package for [rebound](https://github.com/hannorein/rebound)

----------
install with

```shell
pip install git+https://github.com/Findus23/rebound-stubs.git#main
# or
poetry add git+https://github.com/Findus23/rebound-stubs.git#main
```

afterwards type-based suggestions should be shown in the IDE and mypy should consider rebound in its type checks.

rebound-stubs doesn't do anything at runtime, so it doesn't affect how the program runs and bugs in it should not be able to interfere with rebound code

### License

Licensed under GPL-3.0, based on [rebound](https://github.com/hannorein/rebound) by Hanno Rein
