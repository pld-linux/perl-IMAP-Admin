%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	IMAP-Admin perl module
Summary(pl):	Modu³ perla IMAP-Admin
Name:		perl-IMAP-Admin
Version:	0.8.2
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/IMAP/IMAP-Admin-%{version}.tar.gz
Patch:		perl-IMAP-Admin-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
IMAP-Admin provides basic IMAP server adminstration.  It provides functions 
for creating and deleting mailboxes and setting various information such as
quotas and access rights.

%description -l pl
IMAP-Admin umo¿liwia podstawowe administrowanie serwerem IMAP. Udostêpnia
funkcje do tworzenia i usuwania skrzynek pocztowych oraz ustawiania ró¿nych
parametrów takich jak quota czy prawa dostêpu.

%prep
%setup -q -n IMAP-Admin-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/IMAP/Admin
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.gz examples/*

%{perl_sitelib}/IMAP/Admin.pm
%{perl_sitelib}/auto/IMAP/Admin/autosplit.ix
%{perl_sitearch}/auto/IMAP/Admin

%{_mandir}/man3/*
