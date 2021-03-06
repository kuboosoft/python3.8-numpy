%global modname numpy
%undefine _missing_build_ids_terminate_build
%define debug_package %{nil}

%define _legacy_common_support 1

%global __requires_exclude ^libgfortran-ed201abd\\.so.*$

Name:           python3.8-numpy
Version:        1.18.5
Release:        0.2%{?dist}
Summary:        A fast multidimensional array facility for Python

# Everything is BSD except for class SafeEval in numpy/lib/utils.py which is Python
License:        BSD and Python and ASL 2.0
URL:            http://www.numpy.org/
Source0:        https://github.com/numpy/numpy/releases/download/v%{version}/numpy-%{version}.tar.gz

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
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib64/python3.8/site-packages/
mkdir -p %{buildroot}/usr/lib/python3.8/site-packages/
/usr/bin/python3.8 -m pip install --user 'Cython==0.29.16' 'hypothesis==5.15.1' 'numpy==1.18.5' 
pushd $HOME
# cp -rf .local/lib/python3.8/site-packages/* %{buildroot}/usr/lib64/python3.8/site-packages/
pushd .local/lib/python3.8/site-packages
cp -r `ls -A | grep -ve "hypothesis" -ve "sortedcontainers"` %{buildroot}/usr/lib64/python3.8/site-packages/
cp -r `ls -A | grep  -e "hypothesis" -e "sortedcontainers"` %{buildroot}/usr/lib/python3.8/site-packages/
popd

cp -f .local/bin/cygdb %{buildroot}/usr/bin/cygdb3.8
cp -f .local/bin/cython %{buildroot}/usr/bin/cython3.8
cp -f .local/bin/cythonize %{buildroot}/usr/bin/cythonize3.8
cp -f .local/bin/f2py3.8 %{buildroot}/usr/bin/

find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!/usr/bin/python3.8=' {} +


%files 
/usr/lib64/python3.8/site-packages/numpy/
/usr/lib64/python3.8/site-packages/numpy.libs/
/usr/lib64/python3.8/site-packages/numpy-1.18.5.dist-info/

# Cython
/usr/bin/cygdb3.8
/usr/bin/cython3.8
/usr/bin/cythonize3.8
/usr/bin/f2py3.8
/usr/lib64/python3.8/site-packages/Cython-0.29.16.dist-info/
/usr/lib64/python3.8/site-packages/Cython/
/usr/lib64/python3.8/site-packages/__pycache__/cython.cpython-38.opt-1.pyc
/usr/lib64/python3.8/site-packages/__pycache__/cython.cpython-38.pyc
/usr/lib64/python3.8/site-packages/attr/
/usr/lib64/python3.8/site-packages/attrs-*.dist-info/
/usr/lib64/python3.8/site-packages/cython.py
/usr/lib64/python3.8/site-packages/pyximport/
/usr/lib64/python3.8/site-packages/cython.pyE

# hypothesis
/usr/lib/python3.8/site-packages/hypothesis-5.15.1.dist-info/
/usr/lib/python3.8/site-packages/hypothesis/

# sortedcontainers
/usr/lib/python3.8/site-packages/sortedcontainers/
/usr/lib/python3.8/site-packages/sortedcontainers-2.2.2.dist-info/

%changelog
