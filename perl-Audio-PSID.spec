#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
# 
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	PSID
Summary:	Audio::PSID Perl module - handle PlaySID files (Commodore C-64 music files)
Summary(pl):	Modu³ Perla Audio::PSID - obs³uga plików PlaySID (muzyki z Commodore C-64)
Name:		perl-Audio-PSID
Version:	2.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	cc2b5cf99af51a163c0beb1773193734
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is designed to handle PlaySID files (usually bearing a
.sid extension), which are music player and data routines converted
from the Commodore C-64 computer with an additional informational
header prepended.

%description -l pl
Ten modu³ s³u¿y do obs³ugi plików PlaySID (zazwyczaj z rozszerzeniem
.sid), które s± procedurami odtwarzacza i danymi przekonwertowanymi z
Commodore C-64 z do³±czonym nag³ówkiem informacyjnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes PSID_v2NG.txt README
%{perl_sitelib}/Audio/PSID.pm
%{_mandir}/man3/*
