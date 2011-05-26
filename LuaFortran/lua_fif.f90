module lua_fif
  use, intrinsic :: iso_c_binding
  use lua_parameters
  ! This module provides a direct translation of the
  ! lua 5.1.4
  ! C-Interfaces to Fortran 2003 interfaces using the
  ! ISO_C_BINDING facilities.

  implicit none

  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  ! lua API interfaces
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  interface

    subroutine lua_getfield(L, index, k) bind(c, name="lua_getfield")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      character(kind=c_char), dimension(*) :: k
    end subroutine lua_getfield

    subroutine lua_gettable(L, index) bind(c, name="lua_gettable")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
    end subroutine lua_gettable

    function lua_gettop(L) bind(c, name="lua_gettop")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int) :: lua_gettop
    end function lua_gettop

    subroutine lua_close(L) bind(c, name="lua_close")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
    end subroutine lua_close

    function lua_isNumber(L, index) bind(c, name="lua_isnumber")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      integer(kind=c_int) :: lua_isnumber
    end function lua_isnumber

    function lua_next(L, index) bind(c, name="lua_next")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      integer(kind=c_int) :: lua_next
    end function lua_next

    function lua_pcall(L, nargs, nresults, errfunc) bind(c, name="lua_pcall")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: nargs
      integer(kind=c_int), value :: nresults
      integer(kind=c_int), value :: errfunc
      integer(kind=c_int) :: lua_pcall
    end function lua_pcall

    subroutine lua_pushinteger(L, n) bind(c, name="lua_pushinteger")
      use, intrinsic :: iso_c_binding
      use lua_parameters, only: lua_int
      type(c_ptr), value :: L
      integer(kind=lua_int), value :: n
    end subroutine lua_pushinteger

    subroutine lua_pushnil(L) bind(c, name="lua_pushnil")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
    end subroutine lua_pushnil

    subroutine lua_pushnumber(L, n) bind(c, name="lua_pushnumber")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      real(kind=c_double), value :: n
    end subroutine lua_pushnumber

    subroutine lua_pushvalue(L, index) bind(c, name="lua_pushvalue")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
    end subroutine lua_pushvalue

    subroutine lua_settop(L, index) bind(c, name="lua_settop")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
    end subroutine lua_settop

    function lua_tolstring(L, index, len) bind(c, name="lua_tolstring")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      integer(kind=c_size_t) :: len
      type(c_ptr) :: lua_tolstring
    end function lua_tolstring

    function lua_tonumber(L, index) bind(c, name="lua_tonumber")
      use, intrinsic :: iso_c_binding
      use lua_parameters, only: lua_num
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      real(kind=lua_num) :: lua_tonumber
    end function lua_tonumber

    function lua_toboolean(L, index) bind(c, name="lua_toboolean")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      integer(kind=c_int) :: lua_toboolean
    end function lua_toboolean

    function lua_type(L, index) bind(c, name="lua_type")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      integer(kind=c_int), value :: index
      integer(kind=c_int) :: lua_type
    end function lua_type

  end interface
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  ! lua auxiliary library interfaces
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  ! lua auxiliary library
  interface

    subroutine luaL_openlibs(L) bind(c, name="luaL_openlibs")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
    end subroutine luaL_openlibs

    function luaL_newstate() bind(c, name="luaL_newstate")
      use, intrinsic :: iso_c_binding
      type(c_ptr) :: luaL_newstate
    end function luaL_newstate

    function luaL_loadfile(L, filename) bind(c, name="luaL_loadfile")
      use, intrinsic :: iso_c_binding
      type(c_ptr), value :: L
      character(kind=c_char), dimension(*) :: filename
      integer(kind=c_int) :: luaL_loadfile
    end function luaL_loadfile

  end interface

end module lua_fif
