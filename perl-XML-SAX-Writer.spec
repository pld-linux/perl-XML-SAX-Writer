#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	SAX-Writer
Summary:	XML::SAX::Writer Perl module - SAX2 XML writer
Summary(pl):	Modu� Perla XML::SAX::Writer - zapis XML-u z SAX2
Name:		perl-XML-SAX-Writer
Version:	0.44
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8c80d6538562925a96ce1c6e00d7f20
BuildRequires:	perl-devel >= 5.6
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.40}
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
Modu� Perla XML::SAX::Writer - zapisuj�cy XML z SAX2.

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
%doc Changes README
%{perl_vendorlib}/XML/SAX/Writer.pm
%{perl_vendorlib}/XML/SAX/Writer
%{_mandir}/man3/*
