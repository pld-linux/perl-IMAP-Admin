%include	/usr/lib/rpm/macros.perl
%define	pdir	IMAP
%define	pnam	Admin
Summary:	IMAP::Admin perl module
Summary(pl):	Modu³ perla IMAP::Admin
Name:		perl-IMAP-Admin
Version:	1.6.0
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/*
%{perl_sitelib}/IMAP/Admin.pm
%{_mandir}/man3/*
