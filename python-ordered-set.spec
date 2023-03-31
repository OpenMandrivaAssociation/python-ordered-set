%global short_name ordered-set
%global dir_name ordered_set

Name:           python-%{short_name}
Version:	4.0.2
Release:	3
Summary:        Custom MutableSet that remembers its order
Group:          Development/Python
License:        MIT
URL:            https://github.com/LuminosoInsight/ordered-set
Source0:	https://files.pythonhosted.org/packages/f5/ab/8252360bfe965bba31ec05112b3067bd129ce4800d89e0b85613bc6044f6/ordered-set-4.0.2.tar.gz

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


%files
%license MIT-LICENSE
%{python3_sitelib}/%{dir_name}-*.egg-info/
%{python3_sitelib}/%{dir_name}.py
