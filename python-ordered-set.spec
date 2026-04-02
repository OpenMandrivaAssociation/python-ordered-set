%define module ordered-set
%define oname ordered_set

Name:		python-ordered-set
Summary:	Custom MutableSet that remembers its order
Version:	4.1.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/rspeer/ordered-set
Source0:	%{URL}/archive/release/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
An OrderedSet is a mutable data structure that is a hybrid of a list and a set.

It remembers the order of its entries, and every entry has an index number
that can be looked up.

%files
%doc README.md
%{python3_sitelib}/%{oname}
%{python3_sitelib}/%{oname}-%{version}.dist-info
