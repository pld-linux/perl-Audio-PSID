#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Audio
%define		pnam	PSID
%include	/usr/lib/rpm/macros.perl
Summary:	Audio::PSID Perl module - handle PlaySID files (Commodore C-64 music files)
Summary(pl.UTF-8):	Moduł Perla Audio::PSID - obsługa plików PlaySID (muzyki z Commodore C-64)
Name:		perl-Audio-PSID
Version:	2.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	cc2b5cf99af51a163c0beb1773193734
URL:		http://search.cpan.org/dist/Audio-PSID/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is designed to handle PlaySID files (usually bearing a
.sid extension), which are music player and data routines converted
from the Commodore C-64 computer with an additional informational
header prepended.

%description -l pl.UTF-8
Ten moduł służy do obsługi plików PlaySID (zazwyczaj z rozszerzeniem
.sid), które są procedurami odtwarzacza i danymi przekonwertowanymi z
Commodore C-64 z dołączonym nagłówkiem informacyjnym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Audio/PSID.pm
%{_mandir}/man3/*
