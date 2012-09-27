%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary:  Simple connection pool framework
Name:     python-connectionpool
Version:  0.0.0
Release:  %{?dist}
Epoch:    %(date +%s)
License:  MIT
Group:    Development/Libraries

BuildRequires:  python, python-setuptools

Requires: python

URL:        https://github.com/sievlev/python-connectionpool
BuildRoot:  %_tmppath/%name-%version-root
BuildArch:  noarch

Source0: python-connectionpool.tar.gz

%description
Simple connection pool framework


%prep
%setup -q -n %name

%install
[ %buildroot = "/" ] || rm -rf %buildroot

%__python setup.py install \
	--root="%buildroot" \
	--prefix="%_prefix" \
	--install-lib="%python_sitearch"

mkdir -p -- %buildroot/%_localstatedir/run/billing

find %buildroot/ -name '*.egg-info' -exec rm -rf -- '{}' '+'

%clean
[ %buildroot = "/" ] || rm -rf %buildroot

%files
%python_sitearch/connectionpool

%changelog
