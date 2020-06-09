%global modname numpy
%undefine _missing_build_ids_terminate_build
%define debug_package %{nil}

%global __requires_exclude ^libgfortran-ed201abd\\.so.*$

Name:           python3.8-numpy
Version:        1.18.5
Release:        0.1%{?dist}
Summary:        A fast multidimensional array facility for Python

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:        BSD and Python and ASL 2.0
URL:            http://www.numpy.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}rc2/numpy-1.19.0rc2.tar.gz

BuildRequires:  python3.8-devel
#BuildRequires:  python3-setuptools
#BuildRequires:  python3-Cython
BuildRequires:  gcc-gfortran gcc
BuildRequires:  lapack-devel
#BuildRequires:  python3-hypothesis

%ifarch %{openblas_arches}
BuildRequires: openblas-devel
%else
BuildRequires: atlas-devel
%endif

Requires: python3-Cython
Requires: python3-numpy-f2py

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.


%prep
mkdir -p python3.8-numpy
%setup -T -D -n python3.8-numpy

%build


%install
mkdir -p %{buildroot}/usr/lib64/python3.8/site-packages/
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages/
/usr/bin/python3.8 -m pip install --user 'Cython==0.29.16' 'hypothesis==5.15.1' numpy 
pushd $HOME
# cp -rf .local/lib/python3.8/site-packages/* %{buildroot}/usr/lib64/python3.8/site-packages/
pushd .local/lib/python3.8/site-packages
cp -r `ls -A | grep -ve "hypothesis" -ve "sortedcontainers"` %{buildroot}/usr/lib64/python3.8/site-packages/
cp -r `ls -A | grep  -e "hypothesis" -e "sortedcontainers"` %{buildroot}/usr/lib/python3.8/site-packages/
popd

%files 
/usr/lib64/python3.8/site-packages/numpy/
/usr/lib64/python3.8/site-packages/numpy.libs/
/usr/lib64/python3.8/site-packages/numpy-1.18.5.dist-info/

# Cython
/usr/lib64/python3.8/site-packages/Cython-0.29.16.dist-info/
/usr/lib64/python3.8/site-packages/Cython/
/usr/lib64/python3.8/site-packages/__pycache__/cython.cpython-38.opt-1.pyc
/usr/lib64/python3.8/site-packages/__pycache__/cython.cpython-38.pyc
/usr/lib64/python3.8/site-packages/attr/
/usr/lib64/python3.8/site-packages/attrs-19.3.0.dist-info/
/usr/lib64/python3.8/site-packages/cython.py
/usr/lib64/python3.8/site-packages/pyximport/

# hypothesis
/usr/lib/python3.8/site-packages/hypothesis-5.15.1.dist-info/
/usr/lib/python3.8/site-packages/hypothesis/

# sortedcontainers
/usr/lib/python3.8/site-packages/sortedcontainers/
/usr/lib/python3.8/site-packages/sortedcontainers-2.2.2.dist-info/

%changelog
