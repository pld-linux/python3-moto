#
# Conditional build:
%bcond_with	tests	# unit tests (some sure 2.0.0 issues?)

Summary:	Library that allows to easily mock out the boto library
Summary(pl.UTF-8):	Biblioteka pozwalająca łatwo podstawiać atrapy biblioteki boto
Name:		python3-moto
Version:	2.3.2
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/moto/
Source0:	https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
# Source0-md5:	c2a61a7e3d458f6f5237f4b5e0fda193
Patch0:		moto-mock.patch
URL:		https://pypi.org/project/moto/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:44
%if %{with tests}
BuildRequires:	python3-PyYAML >= 5.1
BuildRequires:	python3-aws_xray_sdk >= 0.97
BuildRequires:	python3-boto >= 2.45.0
BuildRequires:	python3-boto3 >= 1.9.201
BuildRequires:	python3-botocore >= 1.12.201
BuildRequires:	python3-cfn-lint >= 0.4.0
BuildRequires:	python3-cryptography >= 3.3.1
BuildRequires:	python3-dateutil >= 2.1
BuildRequires:	python3-dateutil < 3
BuildRequires:	python3-docker >= 2.5.1
BuildRequires:	python3-ecdsa >= 0.16.0
BuildRequires:	python3-flask
BuildRequires:	python3-flask_cors
BuildRequires:	python3-graphql-core >= 3
BuildRequires:	python3-idna >= 2.5
BuildRequires:	python3-idna < 4
%if "%py3_ver" == "3.7"
BuildRequires:	python3-importlib_metadata
%endif
BuildRequires:	python3-jinja2 >= 2.10.1
BuildRequires:	python3-jose >= 3.1.0
BuildRequires:	python3-jose < 4
BuildRequires:	python3-jsondiff >= 1.1.2
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
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moto is a library that allows your tests to easily mock out AWS
Services.

%description -l pl.UTF-8
Moto to biblioteka pozwalająca w testach łatwo podstawiać atrapy usług
AWS.

%prep
%setup -q -n moto-%{version}
%patch -P 0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/moto_server{,-3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md README.md
%attr(755,root,root) %{_bindir}/moto_server-3
%{py3_sitescriptdir}/moto
%{py3_sitescriptdir}/moto-%{version}-py*.egg-info
