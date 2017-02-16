Advanced Options and Tables in Universal Scripting
==================================================

The AOTUS library provides a Fortran wrapper around the C-API of the
[Lua](http://www.lua.org) scripting language, allowing a convenient usage of Lua
scripts as configuration files in Fortran applications.

Please visit the [Wiki](https://bitbucket.org/apesteam/aotus/wiki/Home)
for more information on its usage.
And for a detailed interface reference visit its
[FORD generated documentation](https://geb.sts.nt.uni-siegen.de/doxy/aotus)

*This library is released under a simplified MIT licence, please have a look into the COPYRIGHT file for details.*

Aotus is part of the APES suite, for which there is a
[mailing list](https://listserv.uni-siegen.de/cgi-bin/mailman/listinfo/apes)
where questions can be asked.


How To Build
------------

[Waf](http://code.google.com/p/waf/) is used as build system.
Run:

~~~~~~~~~~~{.sh}
./waf configure build
~~~~~~~~~~~

to build the aotus library.
If you want to select a specific Fortran compiler, set the environment variable
*FC*.
And for a specific C compiler, set the environment variable *CC*.
The Fortran compiler flags are set with the help of fcopts, which provide
a set of compiler flag combinations for various compilers.
They are found in the fortran_compiler.py file in the root directory of the project.

By running:

~~~~~~~~~~~{.sh}
./waf --help
~~~~~~~~~~~

you get a list of available options to the waf script.

### Build using Makefile

Aotus also enables building the library, *libaotus.a*, using GNU `Makefile`.

The build system is based on the [smeka][smeka] build system.  
This build system requires compilation in subdirectory. A minimal compilation
(defaulting to the GNU compiler suite, `gfortran`/`gcc`) is this:

~~~~~{.sh}
mkdir build
cd build
{
echo 'TOP_DIR=..'
echo 'include $(TOP_DIR)/Makefile
} > Makefile
make
~~~~~
and the resulting *libaotus.a* will be present.  
To control the compiler flags one may create a file `setup.make` which may
contain the regular `FC`, `FFLAGS`, `CC`, `CFLAGS`, `INCLUDES` and `LIBS`
variables which are used to compile, and link.
For instance to compile using only the `-g` flag:
~~~~~{.sh}
{
echo FFLAGS = -g
echo CFLAGS = -g
} > setup.make
~~~~~
note that the default compiler is still the GNU suite.

Aotus may be built with two variations of extended precisions. They may
individually be turned on by setting these variables:
~~~~~{makefile}
EXTDOUBLE = 1 # defaults to 0 == do not build with extended double
QUADRUPLE = 1 # defaults to 0 == do not build with quadruple double
~~~~~

To install the library together with the modules one may perform this:
~~~~~{.sh}
make install PREFIX=$HOME/aotus
~~~~~
which creates `bin/`, `include/` and `lib/` folders with the typical libraries
and modules.


What is Built
-------------

For your convenience the Lua library is included in version 5.3.4 (released
2017-01-30).
Its objects are completely gathered into the final *libaotus* library, so you
only need to link against this single static library to gain the
configuration features of Aotus in your Fortran application.
Due to the compiler specific module information required by any application
using libaotus, the suggested approach to incorporate libaotus is to include
its building in the build process of the final application. This is straight
forward if waf is used for the complete project. But also in other build
environments it should not be too hard to make use of the generated *build*
directory.
Yet, if you would rather install the *libaotus.a* and the module files into a
*$PREFIX* directory, you can make use of:

~~~~~~~~~~~{.sh}
./waf install
~~~~~~~~~~~

The default build process will also create some unit test executables and
execute them to ensure functionality of the various parts in the library.

The documentation can be built with [FORD](https://github.com/cmacmackin/ford)
by running:

~~~~~~~~~~~{.sh}
ford aot_mainpage.md
~~~~~~~~~~~

This will build a docu directory with the resulting documentation.
Note, that this requires
[FORD to be installed](https://github.com/cmacmackin/ford#installation)
beforehand.
This documentation is also online available at
[our server](https://geb.sts.nt.uni-siegen.de/aotus).

### Example

There is an example program built, called aotus_sample, which you will find in
the *build* directory.
It can be used with the provided *config.lua* in the *sample* directory, where
also the source of this small program is found.

Getting Started
---------------
The central module in this library is the [[aotus_module]].
Its documentation and the [Aotus overview](page/index.html) would be good
starting points.

Related Projects
----------------

Some projects with similar goals or related information:

* [f2k3-lua](https://github.com/MaikBeckmann/f2k3-lua/tree/simple)
* [FortLua](https://github.com/adolgert/FortLua)

License
=======

Aotus is licensed under the terms of the MIT license reproduced below.
This means that Aotus is free software and can be used for both academic and
commercial purposes at absolutely no cost. You are free to do with the code
whatever you want.
The only requirement is that some credit to the authors is given by putting this
copyright notice somewhere in your project.
The MIT license is chosen for full compatibility with Lua.

For the license of the underlying Lua library have a look at
http://www.lua.org/license.html.

---
Copyright (C) 2011-2013 German Research School for Simulation Sciences GmbH,
                        Aachen and others.
              2014-2017 University of Siegen.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

---


[smeka]: https://github.com/zerothi/smeka
