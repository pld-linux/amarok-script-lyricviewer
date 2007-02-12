%define		scriptname	lyricviewer
Summary:	Extended Lyric Support
Summary(pl.UTF-8):   Rozszerzona obsługa tekstów piosenek
Name:		amarok-script-lyricviewer
Version:	0.2
Release:	0.2
Epoch:		0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/khotnewstuff/amarokscripts/downloads/27109-%{scriptname}-%{version}.amarokscript.tar.gz
# Source0-md5:	583def922138d183824eeae4b18ee16c
Patch0:		%{scriptname}-dcop.patch
URL:		http://www.kde-apps.org/content/show.php?content=27109
BuildRequires:	sed >= 4.0
Requires:	amarok
Requires:	html2text
Requires:	kdebase-kdialog
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir %{_datadir}/apps/amarok/scripts

%description
lyricviewer adds extended Lyric support into amarok. After fetching
lyrics from the Internet, you can view lyrics of any file that you
have previously gotten lyrics for.

This is an extension to the default of showing only the lyrics for
currently playing song. This support viewing lyrics for multiple songs
at once.

%description -l pl.UTF-8
lyricviewer dodaje rozszerzoną obsługę tekstów piosenek do amaroka.
Po pobraniu tekstów z Internetu można oglądać teksty dowolnego utworu,
którego tekst został uprzednio ściągnięty.

Jest to rozszerzenie dla domyślnego pokazywania tylko tekstu aktualnie
odtwarzanego utworu. Ten skrypt obsługuje oglądanie tekstów wielu
piosenek jednocześnie.

%prep
%setup -q -n %{scriptname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}
cp README *.sh $RPM_BUILD_ROOT%{_scriptdir}/%{scriptname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%dir %{_scriptdir}/%{scriptname}
%{_scriptdir}/%{scriptname}/README
%attr(755,root,root) %{_scriptdir}/%{scriptname}/*.sh
