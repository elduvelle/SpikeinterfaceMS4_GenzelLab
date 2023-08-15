#### Usage tests on Ubuntu 18.04

The instructions in README.txt actually work with the exception that `trodesexport` has to be appended with `.\trodesexport`
so the extraction in mountainsort format works
the sorting code (using mountainsort4) works
launching phy doesn't work: this error pops up:
> AttributeError: module 'numpy' has no attribute 'bool'.
`np.bool` was a deprecated alias for the builtin `bool`. To avoid this error in existing code, use `bool` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.bool_` here.

Did this on the local Ubuntu computer (see [this page](https://stackoverflow.com/questions/74893742/how-to-solve-attributeerror-module-numpy-has-no-attribute-bool)):

```
python -m pip uninstall numpy
python -m pip install numpy==1.23.1
```

Got this error, but we don't care about it:

> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
pandas 2.0.3 requires numpy>=1.23.2; python_version >= "3.11", but you have numpy 1.23.1 which is incompatible.

I ignored it and launched phy again and it worked!


