#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_sugar
Version  : 0.9.4
Release  : 26
URL      : https://files.pythonhosted.org/packages/5d/ca/0e96605e91dff95ce058a704406701d5ab8f5f3a53e8c800e5186290498c/pytest-sugar-0.9.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/5d/ca/0e96605e91dff95ce058a704406701d5ab8f5f3a53e8c800e5186290498c/pytest-sugar-0.9.4.tar.gz
Summary  : pytest-sugar is a plugin for pytest that changes the default look and feel of pytest (e.g. progressbar, show tests that fail instantly).
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pytest_sugar-license = %{version}-%{release}
Requires: pypi-pytest_sugar-python = %{version}-%{release}
Requires: pypi-pytest_sugar-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: pytest-sugar
Provides: pytest-sugar-python
Provides: pytest-sugar-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(packaging)
BuildRequires : pypi(pytest)
BuildRequires : pypi(termcolor)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# pytest-sugar
[![Build status](https://travis-ci.org/Teemu/pytest-sugar.svg?branch=master)](https://travis-ci.org/Teemu/pytest-sugar)
[![Pypi version](https://img.shields.io/pypi/v/pytest-sugar.svg)](https://pypi.org/project/pytest-sugar/)

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
%setup -q -n pytest-sugar-0.9.4
cd %{_builddir}/pytest-sugar-0.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641482138
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_sugar
cp %{_builddir}/pytest-sugar-0.9.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_sugar/ddb1f9409837a9415697b56693032fc8dd25d287
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
