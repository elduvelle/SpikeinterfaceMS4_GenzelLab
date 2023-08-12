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


Did full reinstall of Anaconda
Now using the version that comp1 has: 2021.11
Did not work (still missing the stdlib thing)

Going to try again with the visual studio developer command line
Actually it has this weird error that I noticed before but maybe I should fix it:
![image](https://github.com/elduvelle/SpikeinterfaceMS4_GenzelLab/assets/64431932/189b76da-4637-480c-97d7-cf9bbfa1058a)

This page explains how to fix it so I'm trying that: https://stackoverflow.com/questions/71813161/the-system-cannot-find-the-file-specified-in-developer-command-prompt-for-vs-202
https://code.visualstudio.com/docs/cpp/config-msvc
doing the install of everything listed there

The Developer command prompt is working now!
![image](https://github.com/elduvelle/SpikeinterfaceMS4_GenzelLab/assets/64431932/0af5d283-a3c8-4b4e-b25c-35cfede81560)

Will restart and check isosplit..

Using Anaconda Powershell
building isosplit worked!!!

But then it failed again at `pip install mountainsort4`

> Collecting mountainsort4
  Downloading mountainsort4-1.0.4.tar.gz (13 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: dask in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from mountainsort4) (2023.8.0)
Requirement already satisfied: pybind11 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from mountainsort4) (2.11.1)
Collecting isosplit5==0.1.3 (from mountainsort4)
  Using cached isosplit5-0.1.3.tar.gz (17 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: numpy in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from mountainsort4) (1.25.2)
Requirement already satisfied: h5py in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from mountainsort4) (3.9.0)
Requirement already satisfied: scikit-learn in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from mountainsort4) (1.3.0)
Collecting spikeextractors>=0.9.5 (from mountainsort4)
  Downloading spikeextractors-0.9.11-py3-none-any.whl (174 kB)
     ---------------------------------------- 174.6/174.6 kB 3.5 MB/s eta 0:00:00
Requirement already satisfied: tqdm in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from spikeextractors>=0.9.5->mountainsort4) (4.66.1)
Requirement already satisfied: joblib in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from spikeextractors>=0.9.5->mountainsort4) (1.3.2)
Requirement already satisfied: click>=8.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (8.1.6)
Requirement already satisfied: cloudpickle>=1.5.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (2.2.1)
Requirement already satisfied: fsspec>=2021.09.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (2023.6.0)
Requirement already satisfied: packaging>=20.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (23.1)
Requirement already satisfied: partd>=1.2.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (1.4.0)
Requirement already satisfied: pyyaml>=5.3.1 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (6.0.1)
Requirement already satisfied: toolz>=0.10.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (0.12.0)
Requirement already satisfied: importlib-metadata>=4.13.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from dask->mountainsort4) (6.8.0)
Requirement already satisfied: scipy>=1.5.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from scikit-learn->mountainsort4) (1.11.1)
Requirement already satisfied: threadpoolctl>=2.0.0 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from scikit-learn->mountainsort4) (3.2.0)
Requirement already satisfied: colorama in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from click>=8.0->dask->mountainsort4) (0.4.6)
Requirement already satisfied: zipp>=0.5 in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from importlib-metadata>=4.13.0->dask->mountainsort4) (3.16.2)
Requirement already satisfied: locket in c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages (from partd>=1.2.0->dask->mountainsort4) (1.0.0)
Building wheels for collected packages: mountainsort4, isosplit5
  Building wheel for mountainsort4 (setup.py) ... done
  Created wheel for mountainsort4: filename=mountainsort4-1.0.4-py3-none-any.whl size=14449 sha256=e0344a812ca5cc55a461094d204a741e4ce0e379498c2d1e1f510b1d7ab9fdc9
  Stored in directory: c:\users\ele\appdata\local\pip\cache\wheels\38\42\ba\5107a3dd9929901dc14bbac762682a808fde54fb462211137b
  Building wheel for isosplit5 (setup.py) ... error
  error: subprocess-exited-with-error
  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [34 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-39
      creating build\lib.win-amd64-cpython-39\isosplit5
      copying isosplit5\__init__.py -> build\lib.win-amd64-cpython-39\isosplit5
      running build_ext
      building 'isosplit5_interface' extension
      creating build\temp.win-amd64-cpython-39
      creating build\temp.win-amd64-cpython-39\Release
      creating build\temp.win-amd64-cpython-39\Release\src
      "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.1.3\\\"
      isocut5.cpp
      C:\Users\Ele\AppData\Local\Temp\pip-install-tlh2ts8_\isosplit5_fb800209654b4f09abe579d134cb2d7b\src\isocut5.h(21): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
      C:\Users\Ele\AppData\Local\Temp\pip-install-tlh2ts8_\isosplit5_fb800209654b4f09abe579d134cb2d7b\src\isocut5.h(21): error C2146: syntax error: missing ';' before identifier 'bigint'
      C:\Users\Ele\AppData\Local\Temp\pip-install-tlh2ts8_\isosplit5_fb800209654b4f09abe579d134cb2d7b\src\isocut5.h(27): error C2061: syntax error: identifier 'bigint'
      src/isocut5.cpp(39): warning C4244: '=': conversion from 'double' to 'float', possible loss of data
      src/isocut5.cpp(40): error C2660: 'isocut5': function does not take 5 arguments
      C:\Users\Ele\AppData\Local\Temp\pip-install-tlh2ts8_\isosplit5_fb800209654b4f09abe579d134cb2d7b\src\isocut5.h(27): note: see declaration of 'isocut5'
      src/isocut5.cpp(40): note: while trying to match the argument list '(double *, double *, int, float *, isocut5_opts)'
      src/isocut5.cpp(55): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
      src/isocut5.cpp(57): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
      src/isocut5.cpp(62): warning C4244: '=': conversion from 'int' to 'float', possible loss of data
      src/isocut5.cpp(64): warning C4244: '=': conversion from 'int' to 'float', possible loss of data
      src/isocut5.cpp(65): warning C4244: 'initializing': conversion from 'double' to 'float', possible loss of data
      src/isocut5.cpp(81): warning C4244: '=': conversion from 'bigint' to 'float', possible loss of data
      src/isocut5.cpp(136): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
      src/isocut5.cpp(138): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
      src/isocut5.cpp(143): warning C4244: '=': conversion from 'int' to 'float', possible loss of data
      src/isocut5.cpp(145): warning C4244: '=': conversion from 'int' to 'float', possible loss of data
      src/isocut5.cpp(146): warning C4244: 'initializing': conversion from 'double' to 'float', possible loss of data
      src/isocut5.cpp(162): warning C4244: '=': conversion from 'bigint' to 'float', possible loss of data
      error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.37.32822\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for isosplit5
  Running setup.py clean for isosplit5
Successfully built mountainsort4
Failed to build isosplit5
ERROR: Could not build wheels for isosplit5, which is required to install pyproject.toml-based projects


Tried to install isosplit the 'setup.py' way: it worked (again!!) but with a LOT of errors / warnings:

> C:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\setuptools\__init__.py:84: _DeprecatedInstaller: setuptools.installer and fetch_build_eggs are deprecated.
!!
        ********************************************************************************
        Requirements should be satisfied by a PEP 517 installer.
        If you are using pip, you can try `pip install --use-pep517`.
        ********************************************************************************
!!
  dist.fetch_build_eggs(dist.setup_requires)
running install
C:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\setuptools\_distutils\cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!
        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.
        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************
!!
  self.initialize_options()
C:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\setuptools\_distutils\cmd.py:66: EasyInstallDeprecationWarning: easy_install command is deprecated.
!!
        ********************************************************************************
        Please avoid running ``setup.py`` and ``easy_install``.
        Instead, use pypa/build, pypa/installer or other
        standards-based tools.
        See https://github.com/pypa/setuptools/issues/917 for details.
        ********************************************************************************
!!
  self.initialize_options()
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
running build_ext
building 'isosplit5_interface' extension
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isocut5.cpp
src/isocut5.cpp(33): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(35): warning C4244: 'argument': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(35): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(40): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(42): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(59): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(115): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(117): warning C4244: 'argument': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(117): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(122): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(124): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(141): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isosplit5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isosplit5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isosplit5.cpp
src/isosplit5.cpp(210): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(220): warning C4267: '=': conversion from 'size_t' to 'int', possible loss of data
src/isosplit5.cpp(228): warning C4477: 'printf' : format string '%ld' requires an argument of type 'long', but variadic argument 1 has type 'bigint'
src/isosplit5.cpp(228): note: consider using '%lld' in the format string
src/isosplit5.cpp(228): note: consider using '%Id' in the format string
src/isosplit5.cpp(228): note: consider using '%I64d' in the format string
src/isosplit5.cpp(280): warning C4244: 'initializing': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(294): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit5.cpp(383): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit5.cpp(416): warning C4244: '=': conversion from '_Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(443): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(617): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(675): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isosplit5.cpp(692): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(723): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(951): warning C4244: 'argument': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1085): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(1086): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(1361): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1384): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1461): warning C4244: 'initializing': conversion from 'bigint' to 'int', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isosplit5_pybind11.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isosplit5_pybind11.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isosplit5_pybind11.cpp
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(13): warning C4244: '=': conversion from 'pybind11::ssize_t' to 'long', possible loss of data
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(11): note: while compiling class template member function 'NDArray<int>::NDArray(pybind11::array_t<int,16> &)'
src/isosplit5_pybind11.cpp(10): note: see the first reference to 'NDArray<int>::NDArray' in 'isosplit5_interface'
src/isosplit5_pybind11.cpp(10): note: see reference to class template instantiation 'NDArray<int>' being compiled
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(14): warning C4244: '=': conversion from 'pybind11::ssize_t' to 'long', possible loss of data
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(16): warning C4244: 'argument': conversion from '_Ty' to '_Ty', possible loss of data
        with
        [
            _Ty=pybind11::ssize_t
        ]
        and
        [
            _Ty=int
        ]
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/jisotonic5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/jisotonic5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
jisotonic5.cpp
src/jisotonic5.cpp(78): warning C4244: '+=': conversion from 'double' to 'bigint', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy\libs /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy\PCbuild\amd64 "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.22621.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.22621.0\\um\x64" /EXPORT:PyInit_isosplit5_interface build\temp.win-amd64-cpython-39\Release\src/isocut5.obj build\temp.win-amd64-cpython-39\Release\src/isosplit5.obj build\temp.win-amd64-cpython-39\Release\src/isosplit5_pybind11.obj build\temp.win-amd64-cpython-39\Release\src/jisotonic5.obj /OUT:build\lib.win-amd64-cpython-39\isosplit5_interface.cp39-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-39\Release\src\isosplit5_interface.cp39-win_amd64.lib
   Creating library build\temp.win-amd64-cpython-39\Release\src\isosplit5_interface.cp39-win_amd64.lib and object build\temp.win-amd64-cpython-39\Release\src\isosplit5_interface.cp39-win_amd64.exp
Generating code
Finished generating code
building 'isosplit6_interface' extension
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isocut5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isocut5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isocut5.cpp
src/isocut5.cpp(33): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(35): warning C4244: 'argument': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(35): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(40): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(42): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(59): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(115): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(117): warning C4244: 'argument': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(117): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isocut5.cpp(122): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(124): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
src/isocut5.cpp(141): warning C4244: '=': conversion from 'bigint' to 'double', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isocut6.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isocut6.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isocut6.cpp
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isosplit5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isosplit5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isosplit5.cpp
src/isosplit5.cpp(210): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(220): warning C4267: '=': conversion from 'size_t' to 'int', possible loss of data
src/isosplit5.cpp(228): warning C4477: 'printf' : format string '%ld' requires an argument of type 'long', but variadic argument 1 has type 'bigint'
src/isosplit5.cpp(228): note: consider using '%lld' in the format string
src/isosplit5.cpp(228): note: consider using '%Id' in the format string
src/isosplit5.cpp(228): note: consider using '%I64d' in the format string
src/isosplit5.cpp(280): warning C4244: 'initializing': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(294): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit5.cpp(383): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit5.cpp(416): warning C4244: '=': conversion from '_Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(443): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(617): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(675): warning C4244: 'initializing': conversion from 'double' to 'bigint', possible loss of data
src/isosplit5.cpp(692): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(723): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(951): warning C4244: 'argument': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1085): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(1086): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit5.cpp(1361): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1384): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit5.cpp(1461): warning C4244: 'initializing': conversion from 'bigint' to 'int', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isosplit6.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isosplit6.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isosplit6.cpp
src/isosplit6.cpp(44): warning C4244: 'initializing': conversion from 'bigint' to 'int', possible loss of data
src/isosplit6.cpp(58): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit6.cpp(147): warning C4244: 'argument': conversion from 'bigint' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
src/isosplit6.cpp(180): warning C4244: '=': conversion from '_Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit6.cpp(207): warning C4244: '=': conversion from 'bigint' to 'int', possible loss of data
src/isosplit6.cpp(329): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
src/isosplit6.cpp(330): warning C4244: 'initializing': conversion from 'const _Ty' to 'int', possible loss of data
        with
        [
            _Ty=bigint
        ]
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/isosplit6_pybind11.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/isosplit6_pybind11.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
isosplit6_pybind11.cpp
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(13): warning C4244: '=': conversion from 'pybind11::ssize_t' to 'long', possible loss of data
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(11): note: while compiling class template member function 'NDArray<int>::NDArray(pybind11::array_t<int,16> &)'
src/isosplit6_pybind11.cpp(10): note: see the first reference to 'NDArray<int>::NDArray' in 'isosplit6_interface'
src/isosplit6_pybind11.cpp(10): note: see reference to class template instantiation 'NDArray<int>' being compiled
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(14): warning C4244: '=': conversion from 'pybind11::ssize_t' to 'long', possible loss of data
C:\Users\Ele\Documents\GitHub\isosplit5_python\src\ndarray.h(16): warning C4244: 'argument': conversion from '_Ty' to '_Ty', possible loss of data
        with
        [
            _Ty=pybind11::ssize_t
        ]
        and
        [
            _Ty=int
        ]
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\lib\site-packages\pybind11\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\include -IC:\Users\Ele\anaconda3\envs\mountainsort_phy\Include "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22621.0\\cppwinrt" /EHsc /Tpsrc/jisotonic5.cpp /Fobuild\temp.win-amd64-cpython-39\Release\src/jisotonic5.obj /EHsc /DVERSION_INFO=\\\"0.2.2\\\"
jisotonic5.cpp
src/jisotonic5.cpp(78): warning C4244: '+=': conversion from 'double' to 'bigint', possible loss of data
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy\libs /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy /LIBPATH:C:\Users\Ele\anaconda3\envs\mountainsort_phy\PCbuild\amd64 "/LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.37.32822\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.22621.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.22621.0\\um\x64" /EXPORT:PyInit_isosplit6_interface build\temp.win-amd64-cpython-39\Release\src/isocut5.obj build\temp.win-amd64-cpython-39\Release\src/isocut6.obj build\temp.win-amd64-cpython-39\Release\src/isosplit5.obj build\temp.win-amd64-cpython-39\Release\src/isosplit6.obj build\temp.win-amd64-cpython-39\Release\src/isosplit6_pybind11.obj build\temp.win-amd64-cpython-39\Release\src/jisotonic5.obj /OUT:build\lib.win-amd64-cpython-39\isosplit6_interface.cp39-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-39\Release\src\isosplit6_interface.cp39-win_amd64.lib
   Creating library build\temp.win-amd64-cpython-39\Release\src\isosplit6_interface.cp39-win_amd64.lib and object build\temp.win-amd64-cpython-39\Release\src\isosplit6_interface.cp39-win_amd64.exp
Generating code
Finished generating code
creating build\bdist.win-amd64
creating build\bdist.win-amd64\egg
creating build\bdist.win-amd64\egg\isosplit5
copying build\lib.win-amd64-cpython-39\isosplit5\__init__.py -> build\bdist.win-amd64\egg\isosplit5
copying build\lib.win-amd64-cpython-39\isosplit5_interface.cp39-win_amd64.pyd -> build\bdist.win-amd64\egg
copying build\lib.win-amd64-cpython-39\isosplit6_interface.cp39-win_amd64.pyd -> build\bdist.win-amd64\egg
byte-compiling build\bdist.win-amd64\egg\isosplit5\__init__.py to __init__.cpython-39.pyc
creating stub loader for isosplit5_interface.cp39-win_amd64.pyd
creating stub loader for isosplit6_interface.cp39-win_amd64.pyd
byte-compiling build\bdist.win-amd64\egg\isosplit5_interface.py to isosplit5_interface.cpython-39.pyc
byte-compiling build\bdist.win-amd64\egg\isosplit6_interface.py to isosplit6_interface.cpython-39.pyc
creating build\bdist.win-amd64\egg\EGG-INFO
copying isosplit5.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
copying isosplit5.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying isosplit5.egg-info\dependency_links.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying isosplit5.egg-info\requires.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying isosplit5.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
writing build\bdist.win-amd64\egg\EGG-INFO\native_libs.txt
zip_safe flag not set; analyzing archive contents...
__pycache__.isosplit5_interface.cpython-39: module references __file__
__pycache__.isosplit6_interface.cpython-39: module references __file__
creating dist
creating 'dist\isosplit5-0.2.2-py3.9-win-amd64.egg' and adding 'build\bdist.win-amd64\egg' to it
removing 'build\bdist.win-amd64\egg' (and everything under it)
Processing isosplit5-0.2.2-py3.9-win-amd64.egg
creating c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages\isosplit5-0.2.2-py3.9-win-amd64.egg
Extracting isosplit5-0.2.2-py3.9-win-amd64.egg to c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages
Adding isosplit5 0.2.2 to easy-install.pth file
Installed c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages\isosplit5-0.2.2-py3.9-win-amd64.egg
Processing dependencies for isosplit5==0.2.2
Searching for pybind11==2.11.1
Best match: pybind11 2.11.1
Adding pybind11 2.11.1 to easy-install.pth file
detected new path './isosplit5-0.2.2-py3.9-win-amd64.egg'
Installing pybind11-config-script.py script to C:\Users\Ele\anaconda3\envs\mountainsort_phy\Scripts
Installing pybind11-config.exe script to C:\Users\Ele\anaconda3\envs\mountainsort_phy\Scripts
Using c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages
Searching for numpy==1.25.2
Best match: numpy 1.25.2
Adding numpy 1.25.2 to easy-install.pth file
Installing f2py-script.py script to C:\Users\Ele\anaconda3\envs\mountainsort_phy\Scripts
Installing f2py.exe script to C:\Users\Ele\anaconda3\envs\mountainsort_phy\Scripts
Using c:\users\ele\anaconda3\envs\mountainsort_phy\lib\site-packages
Finished processing dependencies for isosplit5==0.2.2

tried `pip install mountainsort4` and it failed again. at least we don't have the stdlib problem anymore... we have a millon more errors and it still ends in 
>  error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2022\\BuildTools\\VC\\Tools\\MSVC\\14.37.32822\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2



---- list of modules used by the original (working) computer ----

Anaconda version: 2021.11; build channel py39_0

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
