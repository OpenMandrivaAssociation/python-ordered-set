%global short_name ordered-set
%global dir_name ordered_set

Name:           python-%{short_name}
Version:	4.0.1
Release:	1
Summary:        Custom MutableSet that remembers its order
Group:          Development/Python
License:        MIT
URL:            https://github.com/LuminosoInsight/ordered-set
Source0:	https://files.pythonhosted.org/packages/89/5d/60db38c980730fc91a0a9cf4c2b932037eecfbd6926aa2ebf450247c0096/ordered-set-4.0.1.tar.gz

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
%{python3_sitelib}/%{dir_name}-*.egg-info/
%{python3_sitelib}/%{dir_name}.py
%{python3_sitelib}/__pycache__/%{dir_name}.*
