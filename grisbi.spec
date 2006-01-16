Summary:	Personal finances manager
Summary(br):	Program a gonterezh an ti
Summary(fr):	Gestionnaire de finances personnelles
Summary(pl):	Zarz±dca finansów osobistych
Name:		grisbi
Version:	0.5.8
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/grisbi/%{name}-%{version}.tar.bz2
# Source0-md5:	6637c02bfad46ac061b9d0e91e404721
URL:		http://www.grisbi.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libofx-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Personal finance manager with a simple and intuitive interface for
basic usage, Grisbi also possesses advanced features that allow the
management of accounts for associations.

The application has been written by French developers, and thus
conforms to French accounting logic. Grisbi is accompanied with an
excellent user manual, updated in every version, as well as a quick
start guide.

%description -l br
Program a gonterezh aes d'ober gantañ evit ezhomoù eeun, Grisbi en
deus ivez tammoù avansetoc'h d'ober war-dro kontoù kevredigezhioù.
Ar program-mañ 'zo bet savet gant gallaoued, neuze e vo kap da heul
reolennoù konterezh gall.
Grisbi 'zo gantañ ul levr mat-tre evit deskiñ ober gantañ.

%description -l fr
Programme de gestion de finances personnelles à l'interface simple et
intuitive pour un usage de base, Grisbi possède également des
fonctionnalités avancées permettant la gestion des comptes
d'associations. Ce logiciel étant développé par des français, il est
donc en totale conformité avec la logique française de la
comptabilité. Grisbi est accompagné d'un excellent manuel de
l'utilisateur, mis à jour à chaque version, ainsi que d'un guide de
démarrage rapide.

%description -l pl
Grisbi to zarz±dca finansów osobistych z prostym i intuicyjnym
interfejsem przy podstawowych funkcjach. Posiada tak¿e funkcje
zaawansowane pozwalaj±ce na zarz±dzanie kontami dla stowarzyszeñ.

Aplikacja zosta³a napisana przez programistów francuskich, przez co
zgodna jest z logik± kont francuskich. Grisbi zawiera doskona³y
podrêcznik u¿ytkownika, uaktualniany dla ka¿dej wersji, a tak¿e
szybki przewodnik dla pocz±tkuj±cych.

%prep
%setup -q

%build
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mime-info/*
%{_pixmapsdir}/grisbi
%dir %{_docdir}/grisbi
%dir %{_docdir}/grisbi/help
%{_docdir}/grisbi/help/C
%lang(fr) %{_docdir}/grisbi/help/fr
%lang(de) %{_docdir}/grisbi/help/de
%{_mandir}/man1/*.1*
