#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require IMAP server access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IMAP
%define		pnam	Admin
Summary:	IMAP::Admin Perl module
Summary(cs):	Modul IMAP::Admin pro Perl
Summary(da):	Perlmodul IMAP::Admin
Summary(de):	IMAP::Admin Perl Modul
Summary(es):	Módulo de Perl IMAP::Admin
Summary(fr):	Module Perl IMAP::Admin
Summary(it):	Modulo di Perl IMAP::Admin
Summary(ja):	IMAP::Admin Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	IMAP::Admin ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul IMAP::Admin
Summary(pl):	Modu³ Perla IMAP::Admin
Summary(pt):	Módulo de Perl IMAP::Admin
Summary(pt_BR):	Módulo Perl IMAP::Admin
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl IMAP::Admin
Summary(sv):	IMAP::Admin Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl IMAP::Admin
Summary(zh_CN):	IMAP::Admin Perl Ä£¿é
Name:		perl-IMAP-Admin
Version:	1.6.1
Release:	4
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8215f41efca2d96b5e2902b8e413a751
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMAP::Admin provides basic IMAP server adminstration. It provides
functions for creating and deleting mailboxes and setting various
information such as quotas and access rights.

%description -l pl
IMAP::Admin umo¿liwia podstawowe administrowanie serwerem IMAP.
Udostêpnia funkcje do tworzenia i usuwania skrzynek pocztowych oraz
ustawiania ró¿nych parametrów takich jak quota czy prawa dostêpu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

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
%doc Changes examples/*
%{perl_vendorlib}/IMAP
%{_mandir}/man3/*
