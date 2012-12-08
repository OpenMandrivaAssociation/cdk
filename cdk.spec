%define major		4
%define libname		%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d
%define	oldlibname	%mklibname %name 4 -d

%define	name		cdk
%define	version		4.9.13
%define	release		%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.vexus.ca/products/CDK/%{name}.tar.gz
License:	BSD
Group:		System/Libraries
URL:		http://www.vexus.ca/products/CDK
Summary:	Curses Development Kit
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cdk stands for 'Curses Development Kit' and it currently contains 21 ready
to use widgets which facilitate the speedy development of full screen
curses programs.

%package -n	%{develname}
Summary:	Headers to develop cdk-based applications
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel
Provides:	%{oldlibname}
Obsoletes:	%{oldlibname}

%description -n	%{develname}
These are the header files, and cdk preprocessor for developing
cdk-based applications.

%prep
%setup -q
perl -pi -e '/^LIB_DIR/ and s,/lib\b,/%{_lib},' Makefile.in

%build
export CFLAGS="%{optflags} -fPIC"
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
make installCDKHeaderFiles installCDKLibrary INSTALL_DIR=$RPM_BUILD_ROOT%{_prefix}
install -d $RPM_BUILD_ROOT%{_mandir}/man3
make installCDKManPages INSTALL_DIR=$RPM_BUILD_ROOT%{_datadir}
 
%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING README BUGS TODO CHANGES NOTES EXPANDING
%dir %{_includedir}/%{name}
%attr(644,root,root) %{_includedir}/%{name}/*
%{_libdir}/lib*.a
%{_mandir}/man3/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.9.13-6mdv2011.0
+ Revision: 663358
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 4.9.13-5mdv2011.0
+ Revision: 603818
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 4.9.13-4mdv2010.1
+ Revision: 522337
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 4.9.13-3mdv2010.0
+ Revision: 413222
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 4.9.13-2mdv2009.0
+ Revision: 220499
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.9.13-1mdv2008.1
+ Revision: 136289
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 17 2007 Adam Williamson <awilliamson@mandriva.org> 4.9.13-1mdv2008.0
+ Revision: 53082
- new release 4.9.13, clean spec
- Import cdk



* Sun Jul 02 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 4.9.11-5mdv2007.0
- %%mkrel
- fix mixed-use-of-spaces-and-tabs

* Fri Apr 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.9.11-4mdk
- pass -fPIC to CFLAGS, needed on the x86_64 arch

* Mon Nov 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.9.11-3mdk
- rebuild

* Mon Sep  1 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 4.9.11-2mdk
- lib64 fixes

* Sun Jul 27 2003 Till Kamppeter <till@mandrakesoft.com> 4.9.11-1mdk
- Updated to 4.9.11.

* Wed Jul 09 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 4.9.10-4mdk
- use %%mklibname macro

* Fri Feb 07 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 4.9.10-3mdk
- Corrected URL
- Minor fixes
- Only static libraries, no libmajor, wronwrongwrong, obsolete old name,
  no ldconfig

* Sun Dec 29 2002 Stefan van der Eijk <stefan@eijk.nu> 4.9.10-2mdk
- BuildRequires
- add man pages (unpackaged files)

* Mon Oct 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 4.9.10-1mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Initial release.
