%define major		4
%define libname		%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d
%define	oldlibname	%mklibname %name 4 -d

%define	name		cdk
%define	version		4.9.13
%define	release		%mkrel 2

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
