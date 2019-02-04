%global short_name ordered-set
%global dir_name ordered_set

Name:           python-%{short_name}
Version:        2.0.2
Release:        1
Summary:        Custom MutableSet that remembers its order

License:        MIT
URL:            https://github.com/LuminosoInsight/ordered-set
Source0:        https://pypi.python.org/packages/source/o/%{short_name}/%{short_name}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

BuildArch:      noarch

%description
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

%prep
%autosetup -n %{short_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py nosetests

%files
%license MIT-LICENSE
%doc README
%{python3_sitelib}/%{dir_name}-*.egg-info/
%{python3_sitelib}/%{dir_name}.py
%{python3_sitelib}/__pycache__/%{dir_name}.*
