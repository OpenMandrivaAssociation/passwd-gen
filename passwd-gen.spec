%define name	passwd-gen
%define version	1.01a
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Password generator
License:	GPL
Group:		System/Base
Source:		%{name}-%{version}.tar.bz2
#gw: remove a compiler warning and convert the output message to UTF-8
Patch: passwd-gen-1.01a-warning.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
passwd-gen is a very powerful password generator written in C to help
you choose a good password. It contains many options to help you
customize your password. The program has been developed for Linux but
may run on many other system (if you are using it from something else
than linux, please contact the author).

%prep
%setup -q
%patch -p1

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.01a-11mdv2010.0
+ Revision: 430240
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.01a-10mdv2009.0
+ Revision: 268358
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Götz Waschk <waschk@mandriva.org> 1.01a-9mdv2009.0
+ Revision: 196221
- remove a build warning
- convert copyright message to UTF-8

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01a-8mdv2008.0
+ Revision: 67059
- rebuild


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01a-7mdv2007.0
- %%mkrel

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01a-6mdk 
- spec cleanup
- correct optimisations

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.01a-5mdk 
- rebuild

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.01a-4mdk
- rebuild
- dropped invalid URL

