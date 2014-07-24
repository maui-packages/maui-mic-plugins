# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       maui-mic-plugins

# >> macros
# << macros

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Summary:    mic plugins for Maui
Version:    0.2.4
Release:    1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/mauios/maui-mic-plugins
Source0:    %{name}-%{version}.tar.xz
Source100:  maui-mic-plugins.yaml
Requires:   mic
BuildRequires:  pkgconfig(python2)

%description
mic plugins for Maui.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{__python} setup.py install --root=%{buildroot} -O1

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%dir %{_prefix}/lib/mic
%{_prefix}/lib/mic/*
# >> files
# << files
