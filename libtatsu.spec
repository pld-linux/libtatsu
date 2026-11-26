#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Library handling the communication with Apple's Tatsu Signing Server (TSS)
Summary(pl.UTF-8):	Biblioteka obsługująca komunikację z serwerem podpisującym Apple Tatsu (TSS)
Name:		libtatsu
Version:	1.1.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libtatsu/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	189fed5ae9b226c14fefdc38324e2c01
URL:		https://libimobiledevice.org/
BuildRequires:	curl-devel >= 7.0
BuildRequires:	libplist-devel >= 2.6.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library handling the communication with Apple's Tatsu Signing Server
(TSS).

This library is part of the libimobiledevice project
(<https://github.com/libimobiledevice>). The main purpose of this
library is to allow creating TSS request payloads, sending them to
Apple's TSS server, and retrieving and processing the response.

The code was originally part of idevicerestore and has been split out
to its own library, while obviously idevicerestore will remain the
main consumer.

%description -l pl.UTF-8
Biblioteka obsługująca komunikację z serwerem podpisującym Apple Tatsu
(TSS - Tatsu Signing Server).

Biblioteka jest częścią projektu libimobiledevice
(<https://github.com/libimobiledevice>). Głównym celem biblioteki jest
tworzenie zawartości żądań TSS, wysyłanie ich do serwera Apple TSS i
przyjmowanie oraz przetwarzanie odpowiedzi.

Kod był pierwotnie częścią idevicerestore i został wydzielony do
osobnej biblioteki, podczas gdy idevicerestore pozostaje głównym jej
konsumentem.

%package devel
Summary:	Header files for Tatsu library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Tatsu
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libplist-devel >= 2.6.0

%description devel
Header files for Tatsu library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Tatsu.

%package static
Summary:	Static Tatsu library
Summary(pl.UTF-8):	Statyczna biblioteka Tatsu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Tatsu library.

%description static -l pl.UTF-8
Statyczna biblioteka Tatsu.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtatsu.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%{_libdir}/libtatsu.so.*.*.*
%ghost %{_libdir}/libtatsu.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libtatsu.so
%{_includedir}/libtatsu
%{_pkgconfigdir}/libtatsu-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtatsu.a
%endif
