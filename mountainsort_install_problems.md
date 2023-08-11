#### Installation tests & errors

*When trying to install our pipeline on another computer, I've encountered many problems, listed here*


> error: command 'C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.36.32532\bin\HostX86\x64\cl.exe' failed with exit code 2
[end of output]
note: This error originates from a subprocess, and is likely not a problem with pip.
ERROR: Failed building wheel for isosplit5
Running setup.py clean for isosplit5
Failed to build isosplit5
ERROR: Could not build wheels for isosplit5, which is required to install pyproject.toml-based projects


when running `pip install mountainsort4`

beyond the fixes suggested in the readme.md file, I have tried:



- changing the python version in the environment
- changing the mountainsort version


- installing everything from scratch using the versions listed below which are on the working install:

```
conda create --name mountainsort_phy python=3.9.12
```
(change mountainsort_phy to the name of the new environment you want)
```
conda activate mountainsort_phy
```
```
conda install spyder=5.1.5
```
(possibly:
```
conda install spyder-kernels=2.1.3
```
)

```
pip install spikeinterface[full]==0.93
```

```
*pip install phy==2.0b5*
```
This creates an error:
> ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
python-lsp-black 1.0.0 requires black>=19.3b0, but you have black 0.0 which is incompatible.
spyder 5.1.5 requires pyqt5<5.13, but you have pyqt5 5.15.9 which is incompatible.
spyder 5.1.5 requires pyqtwebengine<5.13, but you have pyqtwebengine 5.15.6 which is incompatible.
I tried this instead and it worked:

```
pip install phy --pre --upgrade
```
```
pip install pybind11==2.9.2
```
```
pip install isosplit5==0.1.3
```
Without prior install of pybind11, this generates the `No module named 'pybind11'` error. Adding pip install pybind=2.9.2
After prior install of pybind11, this generates the main error, which happens with pip install mountainsort4 too and which at this stage I do not know how to fix:

> C:\Users\Ele\AppData\Local\Temp\pip-install-cf4tf315\isosplit5_e7d4eff6a1d04927837a401449873461\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2


I noticed that 'good computer' has Microsoft Visual Studio 2022 installed, but this current computer has 2019. Will attempt to install [MS visual studio 2022](https://visualstudio.microsoft.com/vs/) and restart and then reinstall isosplit.

```
pip install mountainsort4==1.0.0
```


-------------
I will attempt to focus on getting isosplit to install as it seems to be the one causing problems.
The isosplit5 github page actually lists several related problems but they seem to have been solved...
https://github.com/magland/isosplit5_python/issues?q=is%3Aissue+is%3Aclosed

`conda create --name isosplit_test python=3.7`

`conda install isosplit5`
-> doesn't work

`pip install isosplit5`
Generates the `stdlib.h` error and the `cl.exe` error

> Collecting isosplit5
  Using cached isosplit5-0.2.2.tar.gz (22 kB)
  Preparing metadata (setup.py) ... done
Collecting numpy
  Downloading numpy-1.21.6-cp37-cp37m-win_amd64.whl (14.0 MB)
     ---------------------------------------- 14.0/14.0 MB 9.6 MB/s eta 0:00:00
Collecting pybind11>=2.2
  Using cached pybind11-2.11.1-py3-none-any.whl (227 kB)
Building wheels for collected packages: isosplit5
  Building wheel for isosplit5 (setup.py) ... error
  error: subprocess-exited-with-error
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [18 lines of output]
      C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\installer.py:30: SetuptoolsDeprecationWarning: setuptools.installer is deprecated. Requirements should be satisfied by a PEP 517 installer.
        SetuptoolsDeprecationWarning,
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-37
      creating build\lib.win-amd64-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win-amd64-cpython-37
      creating build\temp.win-amd64-cpython-37\Release
      creating build\temp.win-amd64-cpython-37\Release\src
      "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -Ic:\users\ele\appdata\local\temp\pip-install-joley5fr\isosplit5_f8fae35e525a461dbf8013820d82a511\.eggs\pybind11-2.11.1-py3.7.egg\pybind11\include -Ic:\users\ele\appdata\local\temp\pip-install-joley5fr\isosplit5_f8fae35e525a461dbf8013820d82a511\.eggs\pybind11-2.11.1-py3.7.egg\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      isocut5.cpp
      C:\Users\Ele\AppData\Local\Temp\pip-install-joley5fr\isosplit5_f8fae35e525a461dbf8013820d82a511\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for isosplit5
  Running setup.py clean for isosplit5
Failed to build isosplit5
Installing collected packages: pybind11, numpy, isosplit5
  Running setup.py install for isosplit5 ... error
  error: subprocess-exited-with-error
  × Running setup.py install for isosplit5 did not run successfully.
  │ exit code: 1
  ╰─> [18 lines of output]
      running install
      C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        setuptools.SetuptoolsDeprecationWarning,
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-37
      creating build\lib.win-amd64-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win-amd64-cpython-37
      creating build\temp.win-amd64-cpython-37\Release
      creating build\temp.win-amd64-cpython-37\Release\src
      "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      isocut5.cpp
      C:\Users\Ele\AppData\Local\Temp\pip-install-joley5fr\isosplit5_f8fae35e525a461dbf8013820d82a511\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure
× Encountered error while trying to install package.
╰─> isosplit5

did `pip cache purge` because it seems that it was using cached files

tried `pip install isosplit5` again and got a similar but different error:

> Collecting isosplit5
  Downloading isosplit5-0.2.2.tar.gz (22 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: numpy in c:\users\ele\anaconda3\envs\test_isosplit\lib\site-packages (from isosplit5) (1.21.6)
Requirement already satisfied: pybind11>=2.2 in c:\users\ele\anaconda3\envs\test_isosplit\lib\site-packages (from isosplit5) (2.11.1)
Building wheels for collected packages: isosplit5
  Building wheel for isosplit5 (setup.py) ... error
  error: subprocess-exited-with-error
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [16 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-37
      creating build\lib.win-amd64-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win-amd64-cpython-37
      creating build\temp.win-amd64-cpython-37\Release
      creating build\temp.win-amd64-cpython-37\Release\src
      "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      isocut5.cpp
      C:\Users\Ele\AppData\Local\Temp\pip-install-e2t2_vem\isosplit5_dcfcc4a37df34c93a3ae547be29865bf\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for isosplit5
  Running setup.py clean for isosplit5
Failed to build isosplit5
Installing collected packages: isosplit5
  Running setup.py install for isosplit5 ... error
  error: subprocess-exited-with-error
  × Running setup.py install for isosplit5 did not run successfully.
  │ exit code: 1
  ╰─> [18 lines of output]
      running install
      C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        setuptools.SetuptoolsDeprecationWarning,
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-37
      creating build\lib.win-amd64-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win-amd64-cpython-37
      creating build\temp.win-amd64-cpython-37\Release
      creating build\temp.win-amd64-cpython-37\Release\src
      "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      isocut5.cpp
      C:\Users\Ele\AppData\Local\Temp\pip-install-e2t2_vem\isosplit5_dcfcc4a37df34c93a3ae547be29865bf\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure
× Encountered error while trying to install package.
╰─> isosplit5
note: This is an issue with the package mentioned above, not pip.

- Now trying the option suggested [here](https://github.com/magland/isosplit5_python/issues/9):
> Worked for me after cloning the isosplit5 repo and installing with the setup.py file using the command: python setup.py install
- clone the repo
- from the conda environment, cd to the repo `cd C:\Users\Ele\Documents\GitHub\isosplit5_python`
- run `python setup.py install`

A same / similar error is encountered:
> running install
C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  setuptools.SetuptoolsDeprecationWarning,
C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\easy_install.py:147: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  EasyInstallDeprecationWarning,
running bdist_egg
running egg_info
writing isosplit5.egg-info\PKG-INFO
writing dependency_links to isosplit5.egg-info\dependency_links.txt
writing requirements to isosplit5.egg-info\requires.txt
writing top-level names to isosplit5.egg-info\top_level.txt
reading manifest file 'isosplit5.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'isosplit5.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_py
creating build\lib.win-amd64-cpython-37
creating build\lib.win-amd64-cpython-37\isosplit5
copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-37\isosplit5
running build_ext
building 'isosplit5_interface' extension
creating build\temp.win-amd64-cpython-37
creating build\temp.win-amd64-cpython-37\Release
creating build\temp.win-amd64-cpython-37\Release\src
"C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isocut5.cpp
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\isocut5.h(19): fatal error C1083: Cannot open include file: 'stdlib.h': No such file or directory
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.29.30133\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
>
> 

- try with an Administrator console
` conda activate test_isosplit`
` pip install isosplit5`: same error
install from setup: same error

- try from the Microsoft visual studio tools console
run 'Visual Studio developer command prompt for vs2022' as administrator
error at launch:
> the system cannot find the file specified

still gives us a prompt so:
` conda activate test_isosplit`
same error as before I think:
> Collecting isosplit5
  Using cached isosplit5-0.2.2.tar.gz (22 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: numpy in c:\users\ele\anaconda3\envs\test_isosplit\lib\site-packages (from isosplit5) (1.21.6)
Requirement already satisfied: pybind11>=2.2 in c:\users\ele\anaconda3\envs\test_isosplit\lib\site-packages (from isosplit5) (2.11.1)
Building wheels for collected packages: isosplit5
  Building wheel for isosplit5 (setup.py) ... error
  error: subprocess-exited-with-error
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [14 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win32-cpython-37
      creating build\lib.win32-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win32-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win32-cpython-37
      creating build\temp.win32-cpython-37\Release
      creating build\temp.win32-cpython-37\Release\src
      cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win32-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      error: command 'cl.exe' failed: None
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for isosplit5
  Running setup.py clean for isosplit5
Failed to build isosplit5
Installing collected packages: isosplit5
  Running setup.py install for isosplit5 ... error
  error: subprocess-exited-with-error
  × Running setup.py install for isosplit5 did not run successfully.
  │ exit code: 1
  ╰─> [16 lines of output]
      running install
      C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        setuptools.SetuptoolsDeprecationWarning,
      running build
      running build_py
      creating build
      creating build\lib.win32-cpython-37
      creating build\lib.win32-cpython-37\isosplit5
      copying isosplit5\__init__.py -> build\lib.win32-cpython-37\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win32-cpython-37
      creating build\temp.win32-cpython-37\Release
      creating build\temp.win32-cpython-37\Release\src
      cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win32-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
      error: command 'cl.exe' failed: None
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure
× Encountered error while trying to install package.
╰─> isosplit5
note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.


clear the cache, try again, same problem

try solution 2:
- from the conda environment, cd to the repo `cd C:\Users\Ele\Documents\GitHub\isosplit5_python`
- run `python setup.py install`
- same error

> C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  setuptools.SetuptoolsDeprecationWarning,
C:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\setuptools\command\easy_install.py:147: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  EasyInstallDeprecationWarning,
running bdist_egg
running egg_info
writing isosplit5.egg-info\PKG-INFO
writing dependency_links to isosplit5.egg-info\dependency_links.txt
writing requirements to isosplit5.egg-info\requires.txt
writing top-level names to isosplit5.egg-info\top_level.txt
reading manifest file 'isosplit5.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'isosplit5.egg-info\SOURCES.txt'
installing library code to build\bdist.win32\egg
running install_lib
running build_py
creating build\lib.win32-cpython-37
creating build\lib.win32-cpython-37\isosplit5
copying isosplit5\__init__.py -> build\lib.win32-cpython-37\isosplit5
running build_ext
building 'isosplit5_interface' extension
creating build\temp.win32-cpython-37
creating build\temp.win32-cpython-37\Release
creating build\temp.win32-cpython-37\Release\src
cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\include -IC:\Users\Ele\anaconda3\envs\test_isosplit\Include /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win32-cpython-37\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
error: command 'cl.exe' failed: None


---- list of modules used by the original (working) computer ----

|Package|                       Version|
|-----------------------------| -----------|
alabaster                     0.7.12
appdirs                       1.4.4
arrow                         1.2.2
astroid                       2.6.6
asttokens                     2.0.5
atomicwrites                  1.4.0
attrs                         21.4.0
autopep8                      1.6.0
Babel                         2.9.1
backcall                      0.2.0
bcrypt                        3.2.0
beautifulsoup4                4.11.1
binaryornot                   0.4.4
black                         19.10b0
bleach                        4.1.0
brotlipy                      0.7.0
certifi                       2022.5.18.1
cffi                          1.15.0
chardet                       4.0.0
charset-normalizer            2.0.4
click                         8.0.4
cloudpickle                   2.0.0
colorama                      0.4.4
colorcet                      3.0.0
cookiecutter                  1.7.3
cryptography                  37.0.1
cycler                        0.11.0
Cython                        0.29.30
dask                          2022.6.0
debugpy                       1.5.1
decorator                     5.1.1
defusedxml                    0.7.1
diff-match-patch              20200713
docutils                      0.17.1
entrypoints                   0.4
executing                     0.8.3
fastjsonschema                2.15.1
flake8                        3.9.2
fonttools                     4.33.3
fsspec                        2022.5.0
ghp-import                    2.1.0
h5py                          3.7.0
idna                          3.3
imagesize                     1.3.0
importlib-metadata            4.11.3
inflection                    0.5.1
intervaltree                  3.1.0
ipykernel                     6.9.1
ipython                       8.3.0
ipython-genutils              0.2.0
isort                         5.9.3
isosplit5                     0.1.3
jedi                          0.18.1
Jinja2                        3.0.3
jinja2-time                   0.2.0
joblib                        1.1.0
jsonschema                    4.4.0
jupyter-client                6.1.12
jupyter-core                  4.10.0
jupyterlab-pygments           0.1.2
keyring                       23.4.0
kiwisolver                    1.4.2
lazy-object-proxy             1.6.0
locket                        1.0.0
Markdown                      3.3.7
MarkupSafe                    2.1.1
matplotlib                    3.5.2
matplotlib-inline             0.1.2
mccabe                        0.6.1
mergedeep                     1.3.4
mistune                       0.8.4
mkdocs                        1.3.0
mountainsort4                 1.0.0
mtscomp                       1.0.2
mypy-extensions               0.4.3
nbclient                      0.5.13
nbconvert                     6.4.4
nbformat                      5.3.0
neo                           0.10.2
nest-asyncio                  1.5.5
networkx                      2.8.3
numpy                         1.22.4
numpydoc                      1.2
packaging                     21.3
pandas                        1.4.2
pandocfilters                 1.5.0
param                         1.12.1
paramiko                      2.8.1
parso                         0.8.3
partd                         1.2.0
pathspec                      0.7.0
pexpect                       4.8.0
phy                           2.0b5
phylib                        2.4.1
pickleshare                   0.7.5
Pillow                        9.1.1
pip                           21.2.4
pluggy                        1.0.0
poyo                          0.5.0
probeinterface                0.2.9
prompt-toolkit                3.0.20
psutil                        5.8.0
ptyprocess                    0.7.0
pure-eval                     0.2.2
pybind11                      2.9.2
pycodestyle                   2.7.0
pycparser                     2.21
pyct                          0.4.8
pydocstyle                    6.1.1
pyflakes                      2.3.1
Pygments                      2.11.2
pylint                        2.9.6
pyls-spyder                   0.4.0
PyNaCl                        1.4.0
PyOpenGL                      3.1.6
pyOpenSSL                     22.0.0
pyparsing                     3.0.4
PyQt5                         5.15.6
PyQt5-Qt5                     5.15.2
PyQt5-sip                     12.10.1
PyQtWebEngine                 5.15.5
PyQtWebEngine-Qt5             5.15.2
pyrsistent                    0.18.0
PySocks                       1.7.1
python-dateutil               2.8.2
python-lsp-black              1.0.0
python-lsp-jsonrpc            1.0.0
python-lsp-server             1.2.4
python-slugify                5.0.2
pytz                          2022.1
pywin32                       302
pywin32-ctypes                0.2.0
PyYAML                        6.0
pyyaml_env_tag                0.1
pyzmq                         22.3.0
QDarkStyle                    3.0.2
qstylizer                     0.1.10
QtAwesome                     1.0.3
qtconsole                     5.3.0
QtPy                          2.0.1
quantities                    0.13.0
regex                         2022.3.15
requests                      2.27.1
rope                          0.22.0
Rtree                         0.9.7
scikit-learn                  1.1.1
scipy                         1.8.1
setuptools                    61.2.0
sip                           4.19.13
six                           1.16.0
sklearn                       0.0
snowballstemmer               2.2.0
sortedcontainers              2.4.0
soupsieve                     2.3.1
Sphinx                        4.4.0
sphinxcontrib-applehelp       1.0.2
sphinxcontrib-devhelp         1.0.2
sphinxcontrib-htmlhelp        2.0.0
sphinxcontrib-jsmath          1.0.1
sphinxcontrib-qthelp          1.0.3
sphinxcontrib-serializinghtml 1.1.5
spikeextractors               0.9.9
spikeinterface                0.93.0
spyder                        5.1.5
spyder-kernels                2.1.3
stack-data                    0.2.0
testpath                      0.5.0
text-unidecode                1.3
textdistance                  4.2.1
threadpoolctl                 3.1.0
three-merge                   0.1.1
tinycss                       0.4
toml                          0.10.2
toolz                         0.11.2
tornado                       6.1
tqdm                          4.64.0
traitlets                     5.1.1
typed-ast                     1.4.3
typing_extensions             4.1.1
ujson                         5.1.0
Unidecode                     1.2.0
urllib3                       1.26.9
watchdog                      2.1.6
wcwidth                       0.2.5
webencodings                  0.5.1
wheel                         0.37.1
win-inet-pton                 1.1.0
wincertstore                  0.2
wrapt                         1.12.1
yapf                          0.31.0
zipp                          3.8.0
