Summary:	Personal finances manager
Summary(br):	Program a gonterezh an ti
Summary(fr):	Gestionnaire de finances personnelles
Summary(pl):	Zarz�dca finans�w osobistych
Name:		grisbi
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/grisbi/%{name}-%{version}.tar.bz2
# Source0-md5:	ceccf6799317686fe53f61730241f7e1
BuildRequires:	gtk+2-devel
URL:		http://www.grisbi.org/
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
Program a gonterezh aes d'ober ganta� evit ezhomo� eeun, Grisbi en
deus ivez tammo� avansetoc'h d'ober war-dro konto� kevredigezhio�.
Ar program-ma� 'zo bet savet gant gallaoued, neuze e vo kap da heul
reolenno� konterezh gall.
Grisbi 'zo ganta� ul levr mat-tre evit deski� ober ganta�.

%description -l fr
Programme de gestion de finances personnelles � l'interface simple et
intuitive pour un usage de base, Grisbi poss�de �galement des
fonctionnalit�s avanc�es permettant la gestion des comptes
d'associations. Ce logiciel �tant d�velopp� par des fran�ais, il est
donc en totale conformit� avec la logique fran�aise de la
comptabilit�. Grisbi est accompagn� d'un excellent manuel de
l'utilisateur, mis � jour � chaque version, ainsi que d'un guide de
d�marrage rapide.

%description -l pl
Grisbi to zarz�dca finans�w osobistych z prostym i intuicyjnym
interfejsem przy podstawowych funkcjach. Posiada tak�e funkcje
zaawansowane pozwalaj�ce na zarz�dzanie kontami dla stowarzysze�.

Aplikacja zosta�a napisana przez programist�w francuskich, przez co
zgodna jest z logik� kont francuskich. Grisbi zawiera doskona�y
podr�cznik u�ytkownika, uaktualniany dla ka�dej wersji, a tak�e
szybki przewodnik dla pocz�tkuj�cych.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/???