#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-numpoly
Version  : 1.2.10
Release  : 21
URL      : https://files.pythonhosted.org/packages/1f/38/660d34a8d15b09f318d0accfc8e0af9153bfaab16036875933203da812f8/numpoly-1.2.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/38/660d34a8d15b09f318d0accfc8e0af9153bfaab16036875933203da812f8/numpoly-1.2.10.tar.gz
Summary  : Polynomials as a numpy datatype
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-numpoly-license = %{version}-%{release}
Requires: pypi-numpoly-python = %{version}-%{release}
Requires: pypi-numpoly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://github.com/jonathf/numpoly/raw/master/docs/.static/numpoly_logo.svg
:height: 200 px
:width: 200 px
:align: center

%package license
Summary: license components for the pypi-numpoly package.
Group: Default

%description license
license components for the pypi-numpoly package.


%package python
Summary: python components for the pypi-numpoly package.
Group: Default
Requires: pypi-numpoly-python3 = %{version}-%{release}

%description python
python components for the pypi-numpoly package.


%package python3
Summary: python3 components for the pypi-numpoly package.
Group: Default
Requires: python3-core
Provides: pypi(numpoly)
Requires: pypi(importlib_metadata)
Requires: pypi(numpy)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-numpoly package.


%prep
%setup -q -n numpoly-1.2.10
cd %{_builddir}/numpoly-1.2.10
pushd ..
cp -a numpoly-1.2.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688572584
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-numpoly
cp %{_builddir}/numpoly-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-numpoly/e4a3a7723c8c4b8983a586e0af62f15a5e98483a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-numpoly/e4a3a7723c8c4b8983a586e0af62f15a5e98483a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
