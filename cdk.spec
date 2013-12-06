%define debug_package %{nil}

%define devname %mklibname %{name} -d

Summary:	Curses Development Kit
Name:		cdk
Version:	4.9.13
Release:	10
License:	BSD
Group:		System/Libraries
Url:		http://invisible-island.net/cdk/
Source0:	http://invisible-island.net/datafiles/release/%{name}.tar.gz
BuildRequires:	pkgconfig(ncurses)

%description
Cdk stands for 'Curses Development Kit' and it currently contains 21 ready
to use widgets which facilitate the speedy development of full screen
curses programs.

%package -n	%{devname}
Summary:	Headers to develop cdk-based applications
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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
install -d %{buildroot}%{_includedir}/%{name}
make installCDKHeaderFiles installCDKLibrary INSTALL_DIR=%{buildroot}%{_prefix}
install -d %{buildroot}%{_mandir}/man3
make installCDKManPages INSTALL_DIR=%{buildroot}%{_datadir}

%files -n %{devname}
%doc COPYING README BUGS TODO CHANGES NOTES EXPANDING
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib*.a
%{_mandir}/man3/*

