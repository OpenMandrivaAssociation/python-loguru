%define module	loguru

Summary:	Python logging made (stupidly) simple

Name:		python-%{module}
Version:	0.7.2
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://github.com/Delgan/loguru
Source0:	https://files.pythonhosted.org/packages/source/l/loguru/loguru-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools

%description
Loguru is a library which aims to bring enjoyable logging in Python.

Did you ever feel lazy about configuring a logger and used print() instead?... 
I did, yet logging is fundamental to every application and eases the process of debugging. 
Using Loguru you have no excuse not to use logging from the start, this is as simple as from loguru import logger.

Also, this library is intended to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers. 
Using logs in your application should be an automatism, Loguru tries to make it both pleasant and powerful.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitelib}/loguru-%{version}-py*.*.egg-info
%{python_sitelib}/loguru/
