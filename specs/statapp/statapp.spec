%define pypi_name statapp

%def_without check

Name: statapp
Version: 0.5.0
Release: alt1

Summary: Automated software for statistical analysis and regression modeling
Summary(ru_RU.UTF-8): Автоматизированное программное средство по статистическому анализу и регрессионному моделированию.
License: GPL-3.0
Group: Development/Python3
Url: https://github.com/shizand/statapp
Source: %pypi_name-%version.tar

BuildArch: noarch

Packager: Maxim Slipenko <maxim@slipenko.com>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%description
%summary

%description -l ru_RU.UTF8
Автоматизированное программное средство по статистическому анализу 
и регрессионному моделированию. Является идейным продолжателем программы 
STAT.exe (Produced by Reutov V.N., Donetsk University, 1990)

Разработано двумя студентами ФГБОУ ВО «ДонНТУ» для своего университета.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir_noarch/%pypi_name/**/*.ui

%changelog
* Sat Oct 08 2023 Maxim Slipenko <maxim@slipenko.com> 0.5.0-alt1
- Initial build
