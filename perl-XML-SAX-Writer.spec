#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	SAX-Writer
Summary:	XML::SAX::Writer Perl module - SAX2 XML Writer
Summary(pl):	Modu³ Perla XML::SAX::Writer - zapisuj±cy XML z SAX2
Name:		perl-XML-SAX-Writer
Version:	0.44
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%{!?_without_tests:BuildRequires:	perl-Test-Simple >= 0.40}
BuildRequires:	perl-Text-Iconv >= 1.2
BuildRequires:	perl-XML-Filter-BufferText >= 0.01
BuildRequires:	perl-XML-NamespaceSupport >= 0.03
BuildRequires:	perl-XML-SAX
BuildRequires:	perl(XML::SAX::Exception) >= 1.01
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Text-Iconv >= 1.2
Requires:	perl-XML-Filter-BufferText >= 0.01
Requires:	perl-XML-NamespaceSupport >= 0.03
Requires:	perl(XML::SAX::Exception) >= 1.01
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::SAX::Writer Perl module - SAX2 XML Writer.

%description -l pl
Modu³ Perla XML::SAX::Writer - zapisuj±cy XML z SAX2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/SAX/Writer.pm
%{perl_vendorlib}/XML/SAX/Writer
%{_mandir}/man3/*
