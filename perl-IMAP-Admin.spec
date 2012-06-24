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
Summary(es):	M�dulo de Perl IMAP::Admin
Summary(fr):	Module Perl IMAP::Admin
Summary(it):	Modulo di Perl IMAP::Admin
Summary(ja):	IMAP::Admin Perl �⥸�塼��
Summary(ko):	IMAP::Admin �� ����
Summary(nb):	Perlmodul IMAP::Admin
Summary(pl):	Modu� Perla IMAP::Admin
Summary(pt):	M�dulo de Perl IMAP::Admin
Summary(pt_BR):	M�dulo Perl IMAP::Admin
Summary(ru):	������ ��� Perl IMAP::Admin
Summary(sv):	IMAP::Admin Perlmodul
Summary(uk):	������ ��� Perl IMAP::Admin
Summary(zh_CN):	IMAP::Admin Perl ģ��
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
IMAP::Admin umo�liwia podstawowe administrowanie serwerem IMAP.
Udost�pnia funkcje do tworzenia i usuwania skrzynek pocztowych oraz
ustawiania r�nych parametr�w takich jak quota czy prawa dost�pu.

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
