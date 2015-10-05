%define debug_package %{nil}
%define date 20150928
%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Curses Development Kit
Name:		cdk
Version:	5.0
Release:	0.%{date}.1
License:	BSD
Group:		System/Libraries
Url:		http://invisible-island.net/cdk/
Source0:	ftp://invisible-island.net/cdk/cdk-%{version}-%{date}.tgz
Patch0:		cdk-5.0-20150928-do-not-hardcode-gcc.patch
BuildRequires:	pkgconfig(ncurses)

%description
Cdk stands for 'Curses Development Kit' and it currently contains 21 ready
to use widgets which facilitate the speedy development of full screen
curses programs.

%package -n %{libname}
Summary:	CDK library
Group:		Development/C

%description -n %{libname}
This the cdk library for developing cdk-based applications.

%package -n %{develname}
Summary:	Headers to develop cdk-based applications
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{develname}
These are the header files, and cdk preprocessor for developing
cdk-based applications.

%prep
%setup -qn %{name}-%{version}-%{date}
%apply_patches

perl -pi -e '/^LIB_DIR/ and s,/lib\b,/%{_lib},' Makefile.in

%build
export CFLAGS="%{optflags} -fPIC"
%configure \
        --with-ncurses \
        --enable-const \
        --with-shared \
        --disable-rpath-hack

# (tpg) fix for llvm-ar
sed -i -e "s/${AR} -cr/${AR} cr/g" Makefile

%make cdkshlib

%install
%makeinstall_std installCDKSHLibrary INSTALL="install -pD"

# fixes rpmlint unstripped-binary-or-object
chmod +x %{buildroot}%{_libdir}/*.so*

rm -rf %{buildroot}%{_docdir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc COPYING README TODO CHANGES NOTES EXPANDING
%{_includedir}/cdk.h
%dir %{_includedir}/%{name}
%attr(644,root,root) %{_includedir}/%{name}/*
%{_bindir}/cdk5-config
%{_libdir}/lib*.a
%{_libdir}/*.so
%{_mandir}/man3/*
