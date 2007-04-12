%define name	passwd-gen
%define version	1.01a
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Password generator
License:	GPL
Group:		System/Base
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
passwd-gen is a very powerful password generator written in C to help
you choose a good password. It contains many options to help you
customize your password. The program has been developed for Linux but
may run on many other system (if you are using it from something else
than linux, please contact the author).

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
install -d 755 %{buildroot}%{_bindir}
install %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/%{name}

