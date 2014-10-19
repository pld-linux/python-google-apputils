#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Google Application Utilities for Python
Summary(pl.UTF-8):	Google Application Utilities dla Pythona
Name:		python-google-apputils
Version:	0.4.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/g/google-apputils/google-apputils-%{version}.tar.gz
# Source0-md5:	049ed237ad43afdc0931c2e5a0c50f3a
URL:		http://code.google.com/p/google-apputils-python
BuildRequires:	python-dateutil >= 1.4
BuildRequires:	python-gflags >= 1.4
BuildRequires:	python-modules >= 2
%{?with_tests:BuildRequires:	python-mox >= 0.5}
BuildRequires:	python-pytz >= 2010
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-dateutil >= 1.4
Requires:	python-gflags >= 1.4
Requires:	python-modules
Requires:	python-pytz >= 2010
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Google Application Utilities is a small collection of utilities for
building Python applications. It includes some of the same set of
utilities used to build and run internal Python apps at Google.

%description -l pl.UTF-8
Google Application Utilities to mały zbiór narzędzi do tworzenia
aplikacji w Pythonie. Zawiera podzbiór narzędzi używanych do
tworzenia i uruchamiania wewnętrznych aplikacji pythonowych w
Google.

%prep
%setup -q -n google-apputils-%{version}

%{__sed} -i -e '/ez_setup/d' setup.py

%build
%{__python} setup.py build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/google
%{py_sitescriptdir}/google/apputils
%{py_sitescriptdir}/google_apputils-%{version}-py*-nspkg.pth
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/google_apputils-%{version}-py*.egg-info
%endif
