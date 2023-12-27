#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pytest_sugar
Version  : 0.9.7
Release  : 41
URL      : https://files.pythonhosted.org/packages/57/18/fe569040c5796879288544b1cc98888fce1754138d54e8287ed21614491e/pytest-sugar-0.9.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/18/fe569040c5796879288544b1cc98888fce1754138d54e8287ed21614491e/pytest-sugar-0.9.7.tar.gz
Summary  : pytest-sugar is a plugin for pytest that changes the default look and feel of pytest (e.g. progressbar, show tests that fail instantly).
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pytest_sugar-license = %{version}-%{release}
Requires: pypi-pytest_sugar-python = %{version}-%{release}
Requires: pypi-pytest_sugar-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# pytest-sugar ✨
[![PyPI version](https://img.shields.io/pypi/v/pytest-sugar.svg)](https://pypi.org/project/pytest-sugar/)

%package license
Summary: license components for the pypi-pytest_sugar package.
Group: Default

%description license
license components for the pypi-pytest_sugar package.


%package python
Summary: python components for the pypi-pytest_sugar package.
Group: Default
Requires: pypi-pytest_sugar-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_sugar package.


%package python3
Summary: python3 components for the pypi-pytest_sugar package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_sugar)
Requires: pypi(packaging)
Requires: pypi(pytest)
Requires: pypi(termcolor)

%description python3
python3 components for the pypi-pytest_sugar package.


%prep
%setup -q -n pytest-sugar-0.9.7
cd %{_builddir}/pytest-sugar-0.9.7
pushd ..
cp -a pytest-sugar-0.9.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681145362
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_sugar
cp %{_builddir}/pytest-sugar-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_sugar/ddb1f9409837a9415697b56693032fc8dd25d287 || :
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
/usr/share/package-licenses/pypi-pytest_sugar/ddb1f9409837a9415697b56693032fc8dd25d287

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
