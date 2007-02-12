#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require IMAP server access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IMAP
%define		pnam	Admin
Summary:	IMAP::Admin Perl module
Summary(cs.UTF-8):   Modul IMAP::Admin pro Perl
Summary(da.UTF-8):   Perlmodul IMAP::Admin
Summary(de.UTF-8):   IMAP::Admin Perl Modul
Summary(es.UTF-8):   Módulo de Perl IMAP::Admin
Summary(fr.UTF-8):   Module Perl IMAP::Admin
Summary(it.UTF-8):   Modulo di Perl IMAP::Admin
Summary(ja.UTF-8):   IMAP::Admin Perl モジュール
Summary(ko.UTF-8):   IMAP::Admin 펄 모줄
Summary(nb.UTF-8):   Perlmodul IMAP::Admin
Summary(pl.UTF-8):   Moduł Perla IMAP::Admin
Summary(pt.UTF-8):   Módulo de Perl IMAP::Admin
Summary(pt_BR.UTF-8):   Módulo Perl IMAP::Admin
Summary(ru.UTF-8):   Модуль для Perl IMAP::Admin
Summary(sv.UTF-8):   IMAP::Admin Perlmodul
Summary(uk.UTF-8):   Модуль для Perl IMAP::Admin
Summary(zh_CN.UTF-8):   IMAP::Admin Perl 模块
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

%description -l pl.UTF-8
IMAP::Admin umożliwia podstawowe administrowanie serwerem IMAP.
Udostępnia funkcje do tworzenia i usuwania skrzynek pocztowych oraz
ustawiania różnych parametrów takich jak quota czy prawa dostępu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
