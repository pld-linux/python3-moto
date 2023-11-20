#
# Conditional build:
%bcond_with	tests	# unit tests (some sure 2.0.0 issues?)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Library that allows to easily mock out the boto library
Summary(pl.UTF-8):	Biblioteka pozwalająca łatwo podstawiać atrapy biblioteki boto
Name:		python-moto
# keep 2.1.x here for python2 support
Version:	2.1.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/moto/
Source0:	https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
# Source0-md5:	373516346ee098804dbf0571e7b22011
Patch0:		%{name}-requires.patch
URL:		https://pypi.org/project/moto/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:44.0
%if %{with tests}
BuildRequires:	python-PyYAML >= 5.1
BuildRequires:	python-aws_xray_sdk >= 0.97
BuildRequires:	python-backports.tempfile
BuildRequires:	python-boto >= 2.36.0
BuildRequires:	python-boto3 >= 1.9.201
BuildRequires:	python-botocore >= 1.12.201
BuildRequires:	python-cfn-lint >= 0.4.0
BuildRequires:	python-configparser < 5
BuildRequires:	python-cryptography >= 3.3.1
BuildRequires:	python-dateutil >= 2.1
BuildRequires:	python-dateutil < 3
BuildRequires:	python-decorator >= 4.4.2
BuildRequires:	python-docker >= 2.5.1
BuildRequires:	python-ecdsa
BuildRequires:	python-flask
BuildRequires:	python-flask_cors
BuildRequires:	python-idna >= 2.5
BuildRequires:	python-idna < 3
BuildRequires:	python-jinja2 >= 2.10.1
BuildRequires:	python-jose >= 1.1.0
BuildRequires:	python-jsondiff >= 1.1.2
BuildRequires:	python-mock < 4
BuildRequires:	python-more_itertools >= 5.0.0
BuildRequires:	python-parameterized >= 0.7.0
BuildRequires:	python-pytz
BuildRequires:	python-requests >= 2.5
BuildRequires:	python-responses >= 0.9.0
BuildRequires:	python-six >= 1.9
BuildRequires:	python-sshpubkeys >= 3.1.0
BuildRequires:	python-sure >= 1.4.11
BuildRequires:	python-werkzeug
BuildRequires:	python-xmltodict
BuildRequires:	python-zipp
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:44
%if %{with tests}
BuildRequires:	python3-PyYAML >= 5.1
BuildRequires:	python3-aws_xray_sdk >= 0.97
BuildRequires:	python3-boto >= 2.36.0
BuildRequires:	python3-boto3 >= 1.9.201
BuildRequires:	python3-botocore >= 1.12.201
BuildRequires:	python3-cfn-lint >= 0.4.0
BuildRequires:	python3-cryptography >= 3.3.1
BuildRequires:	python3-dateutil >= 2.1
BuildRequires:	python3-dateutil < 3
BuildRequires:	python3-docker >= 2.5.1
BuildRequires:	python3-ecdsa
BuildRequires:	python3-flask
BuildRequires:	python3-flask_cors
BuildRequires:	python3-idna >= 2.5
#BuildRequires:	python3-idna < 3
BuildRequires:	python3-jinja2 >= 2.10.1
BuildRequires:	python3-jose >= 1.1.0
BuildRequires:	python3-jsondiff
BuildRequires:	python3-more_itertools >= 5.0.0
BuildRequires:	python3-parameterized >= 0.7.0
BuildRequires:	python3-pytz
BuildRequires:	python3-requests >= 2.5
BuildRequires:	python3-responses >= 0.9.0
BuildRequires:	python3-six >= 1.9
BuildRequires:	python3-sshpubkeys >= 3.1.0
BuildRequires:	python3-sure >= 1.4.11
BuildRequires:	python3-werkzeug
BuildRequires:	python3-xmltodict
BuildRequires:	python3-zipp
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moto is a library that allows your tests to easily mock out AWS
Services.

%description -l pl.UTF-8
Moto to biblioteka pozwalająca w testach łatwo podstawiać atrapy usług
AWS.

%package -n python3-moto
Summary:	Library that allows to easily mock out the boto library
Summary(pl.UTF-8):	Biblioteka pozwalająca łatwo podstawiać atrapy biblioteki boto
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-moto
Moto is a library that allows your tests to easily mock out AWS
Services.

%description -n python3-moto -l pl.UTF-8
Moto to biblioteka pozwalająca w testach łatwo podstawiać atrapy usług
AWS.

%prep
%setup -q -n moto-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/moto_server{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/moto_server{,-3}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.md README.md
%attr(755,root,root) %{_bindir}/moto_server-2
%{py_sitescriptdir}/moto
%{py_sitescriptdir}/moto-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-moto
%defattr(644,root,root,755)
%doc AUTHORS.md README.md
%attr(755,root,root) %{_bindir}/moto_server-3
%{py3_sitescriptdir}/moto
%{py3_sitescriptdir}/moto-%{version}-py*.egg-info
%endif
