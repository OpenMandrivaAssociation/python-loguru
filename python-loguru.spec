%define module loguru

Name:		python-loguru
Summary:	Python logging made (stupidly) simple
Version:	0.7.3
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://github.com/Delgan/loguru
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Loguru is a library which aims to bring enjoyable logging in Python.

Did you ever feel lazy about configuring a logger and used print() instead?... 
I did, yet logging is fundamental to every application and eases the process of debugging. 
Using Loguru you have no excuse not to use logging from the start, this is as simple as from loguru import logger.

Also, this library is intended to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers. 
Using logs in your application should be an automatism, Loguru tries to make it both pleasant and powerful.

%files
%doc README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
