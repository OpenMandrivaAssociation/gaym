%define name	gaym
%define version 0.9.8
%define svn	302
%if %svn
%define release	%mkrel 0.%svn.2
%else
%define release %mkrel 1
%endif

Name:		%{name}
Summary:	Plugin for Pidgin to access gay.com chat
Version:	%{version}
Release:	%{release}
%if %svn
# svn checkout svn://svn.berlios.de/qrc/qrc/trunk gaym
Source0:	%{name}-%{svn}.tar.lzma
%else
Source0:	%{name}-%{version}.tar.bz2
%endif
Group:		Networking/Instant messaging
License:	GPLv2+
BuildRequires:	pidgin-devel
BuildRequires:	libtool-base
BuildRequires:	autoconf
Requires:	pidgin
Url:		http://developer.berlios.de/projects/qrc/

%description
Gaym is a Pidgin plugin that allows it to access the gay.com chat
area. Gay.com uses an obfuscated and extended version of the IRC
protocol.

If you don't already know what gay.com chat is and why you'd want
to go there...you probably don't want this package.

%prep
%setup -q -n %{name}

%build
autoreconf --force --install --symlink
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README TODO
%_libdir/purple-2/*
%_datadir/pixmaps/pidgin/protocols/*/gaym.png
