#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtracefs
Version  : 1.6.2
Release  : 18
URL      : https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-1.6.2.tar.gz
Source0  : https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-1.6.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0
Requires: libtracefs-lib = %{version}-%{release}
BuildRequires : libtraceevent-dev

%description
The official repository is here:
https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/

%package dev
Summary: dev components for the libtracefs package.
Group: Development
Requires: libtracefs-lib = %{version}-%{release}
Provides: libtracefs-devel = %{version}-%{release}
Requires: libtracefs = %{version}-%{release}

%description dev
dev components for the libtracefs package.


%package lib
Summary: lib components for the libtracefs package.
Group: Libraries

%description lib
lib components for the libtracefs package.


%prep
%setup -q -n libtracefs-1.6.2
cd %{_builddir}/libtracefs-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670529855
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1670529855
rm -rf %{buildroot}
%make_install prefix=/usr libdir=/usr/lib64 install_libs

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/tracefs/tracefs.h
/usr/lib64/libtracefs.so
/usr/lib64/pkgconfig/libtracefs.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtracefs.so.1
/usr/lib64/libtracefs.so.1.6.2
