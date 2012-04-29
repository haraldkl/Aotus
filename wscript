#! /usr/bin/env python
# encoding: utf-8
# Harald Klimach 2011
import os

APPNAME = 'aotus'
VERSION = '1'

top = '.'
out = 'build'

def options(opt):
    from waflib.Tools.compiler_fc import fc_compiler
    opt.load('compiler_fc')
    opt.load('compiler_c')

def configure(conf):
    from waflib import Logs
    # The fcopts provide some sane flag combinations
    # for different variants in the various compilers.
    # They are found in apes/sys_env, and included in
    # the waf script, when built with build_waf.sh.
    from waflib.extras.fc_flags import fcopts
    # includes options for:
    # * 'warn': activate compile time warnings
    # * 'w2e': turn warnings into errors
    # * 'standard': check for standard compliance
    # * 'debug': activate debugging facilities
    # * 'optimize': turn optimization on
    # * 'profile': activate profiling facilities
    # * 'double': promote default reals to double precision

    # Load the compiler informations
    conf.load('compiler_fc')
    conf.load('compiler_c')
    conf.env.stash()
    try:
        conf.load('doxygen')
    except conf.errors.ConfigurationError, e:
        Logs.debug('doxygen: %r' % e)
        conf.env.revert()

    conf.env['FCSTLIB_MARKER'] = ''
    conf.env['FCSHLIB_MARKER'] = ''

    conf.check_fortran()
    subconf(conf)

    # Flags for the default (production) variant
    conf.env['FCFLAGS'] = ( fcopts[conf.env.FC_NAME, 'optimize']
                          + fcopts[conf.env.FC_NAME, 'warn'] )
    conf.env['LINKFLAGS'] = conf.env['FCFLAGS']

    # Set flags for the debugging variant
    # DEBUG Variant
    conf.setenv('debug',conf.env)
    conf.env['FCFLAGS'] = ( fcopts[conf.env.FC_NAME, 'standard']
                          + fcopts[conf.env.FC_NAME, 'warn']
                          + fcopts[conf.env.FC_NAME, 'w2e']
                          + fcopts[conf.env.FC_NAME, 'debug'] )
    conf.env['LINKFLAGS'] = conf.env['FCFLAGS']

def subconf(conf):
    """
    Configure parts, which are relevant, even when called
    from parent wscripts.
    Useful to restrict parent recursions to just this part
    of the configuration.
    """
    # Do not change the DEFINES themselves, use the lib_store instead
    tmpDEF = conf.env.DEFINES
    conf.check_cc(function_name='mkstemp',
                  header_name=['stdlib.h', 'unistd.h'],
                  defines=['LUA_USE_MKSTEMP=1'],
                  uselib_store='MKSTEMP', mandatory=False)
    conf.check_cc(function_name='popen',
                  header_name=['stdio.h'],
                  defines=['LUA_USE_POPEN=1'],
                  uselib_store='POPEN', mandatory=False)
    # Cleanup the DEFINES again
    conf.env.DEFINES = tmpDEF

def build(bld):
    core_sources = ['external/lua-5.2.0/src/lapi.c',
                    'external/lua-5.2.0/src/lcode.c',
                    'external/lua-5.2.0/src/lctype.c',
                    'external/lua-5.2.0/src/ldebug.c',
                    'external/lua-5.2.0/src/ldo.c',
                    'external/lua-5.2.0/src/ldump.c',
                    'external/lua-5.2.0/src/lfunc.c',
                    'external/lua-5.2.0/src/lgc.c',
                    'external/lua-5.2.0/src/llex.c',
                    'external/lua-5.2.0/src/lmem.c',
                    'external/lua-5.2.0/src/lobject.c',
                    'external/lua-5.2.0/src/lopcodes.c',
                    'external/lua-5.2.0/src/lparser.c',
                    'external/lua-5.2.0/src/lstate.c',
                    'external/lua-5.2.0/src/lstring.c',
                    'external/lua-5.2.0/src/ltable.c',
                    'external/lua-5.2.0/src/ltm.c',
                    'external/lua-5.2.0/src/lundump.c',
                    'external/lua-5.2.0/src/lvm.c',
                    'external/lua-5.2.0/src/lzio.c']
    lib_sources = ['external/lua-5.2.0/src/lauxlib.c',
                   'external/lua-5.2.0/src/lbaselib.c',
                   'external/lua-5.2.0/src/lbitlib.c',
                   'external/lua-5.2.0/src/lcorolib.c',
                   'external/lua-5.2.0/src/ldblib.c',
                   'external/lua-5.2.0/src/liolib.c',
                   'external/lua-5.2.0/src/lmathlib.c',
                   'external/lua-5.2.0/src/loslib.c',
                   'external/lua-5.2.0/src/ltablib.c',
                   'external/lua-5.2.0/src/lstrlib.c',
                   'external/lua-5.2.0/src/loadlib.c',
                   'external/lua-5.2.0/src/linit.c']
    lua_sources = ['external/lua-5.2.0/src/lua.c']
    luac_sources = ['external/lua-5.2.0/src/luac.c']

    flu_sources = ['LuaFortran/lua_fif.f90',
                   'LuaFortran/lua_parameters.f90',
                   'LuaFortran/flu_binding.f90']

    aotus_sources = ['source/aotus_module.f90',
                     'source/aot_fun_module.f90',
                     'source/aot_kinds_module.f90',
                     'source/aot_table_module.f90',
                     'source/aot_top_module.f90',
		     'source/aot_out_module.f90',
                     'source/aot_path_module.f90',
                     'source/aot_vector_module.f90']

    bld(
        features = 'c',
        source = core_sources + lib_sources,
        defines = ['LUA_ANSI'],
        use = ['MKSTEMP', 'POPEN'],
        target = 'luaobjs')

    bld(
        features = 'c cstlib',
        defines = ['LUA_ANSI'],
        use = 'luaobjs',
        target = 'lua')

    bld(
        features = 'fc',
        source = flu_sources,
        target = 'fluobjs')

    bld(
        features = 'fc fcstlib',
        use = ['luaobjs', 'fluobjs'],
        target = 'flu')

    bld(
        features = 'fc fcstlib',
        source = aotus_sources,
        use = ['luaobjs', 'fluobjs'],
        target = 'aotus')

    bld(
        features = 'fc fcprogram',
        source = ['sample/aotus_sample.f90'],
        use = 'aotus',
        target = 'aotus_sample')

    bld(
        features = 'fc fcprogram',
        source = ['LuaFortran/examples/test.f90'],
        use = 'flu',
        target = 'flu_sample')

    if bld.cmd == 'test':
        for utest in bld.path.ant_glob('utests/*_test.f90'):
            bld(
                features = 'fc fcprogram',
                source = utest,
                use = 'aotus',
                target = utest.change_ext(''))

    if bld.cmd == 'doxy':
        bld(features = 'doxygen',
            doxyfile = 'Doxyfile')

    bld.install_files('${PREFIX}/include', bld.path.get_bld().ant_glob('*.mod'))
    bld.install_files('${PREFIX}/lib', 'libaotus.a')

### Building the lua interpreter, usually not needed.
#    bld(
#        features = 'c cprogram',
#        use = 'lualib',
#        source = lua_sources,
#        defines = ['LUA_ANSI'],
#        stlib = bld.env['STLIBS'],
#        target = 'lua')


from waflib.Build import BuildContext
class debug(BuildContext):
    "Build a debug executable"
    cmd = 'debug'
    variant = 'debug'

class test(BuildContext):
    "Unit Tests"
    cmd = 'test'

class doxy(BuildContext):
    "Doxygen documentation"
    cmd = 'doxy'
