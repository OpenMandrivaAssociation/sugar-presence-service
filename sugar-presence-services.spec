Name: sugar-presence-service
Version: 0.82.2
Release: 1%{?dist}
Summary: The Sugar presence service

Group: System Environment/Libraries
License: GPLv2+
URL: http://dev.laptop.org/
Source0: http://dev.laptop.org/pub/sugar/sources/%{name}/%{name}-%{version}.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: python

Requires: python-telepathy >= 0.14.0
Requires: python-dbus >= 0.82.0
Requires: telepathy-gabble
Requires: telepathy-salut

%description
The Sugar presence service.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/sugar-presence-service
%{_datadir}/sugar-presence-service
%{_datadir}/dbus-1/services/org.laptop.Sugar.Presence.service

%changelog
* Fri Aug  8 2008 Guillaume Desmottes <guillaume.desmottes@collabora.co.uk> - 0.82.2-1
- Update to 0.82.2

* Thu Aug  7 2008 Guillaume Desmottes <guillaume.desmottes@collabora.co.uk> - 0.82.1-1
- Update to 0.82.1
- dev.laptop.org #5618: PS should drop handles causing InspectHandles failing

* Wed Aug  6 2008 Guillaume Desmottes <guillaume.desmottes@collabora.co.uk> - 0.82.0-1
- Update to 0.82.0

* Wed Jul 23 2008 Morgan Collett <morgan@laptop.org> - 0.81.4-1
- Update to 0.81.4

* Tue Jul  8 2008 Morgan Collett <morgan@laptop.org> - 0.81.3-2
- Depends on telepathy-salut and telepathy-gabble

* Tue Jul  8 2008 Morgan Collett <morgan@laptop.org> - 0.81.3-1
- Update to 0.81.3

* Fri Jun 20 2008 Morgan Collett <morgan.collett@gmail.com> - 0.81.2-1
- Update to 0.81.2

* Mon Feb 11 2008 Marco Pesenti Gritti <mpg@redhat.com> - 0.79.0-1
- Update to 0.79.0

* Wed Jan 30 2008 Morgan Collett <morgan.collett@collabora.co.uk> - 0.70.0
- dev.laptop.org #6142: Don't update buddy properties without a key

* Thu Jan 03 2008 Dafydd Harries <dafydd.harries@collabora.co.uk> - 0.65-0.31.20080103git76984f3f28
- dev.laptop.org #5368: Delay setting a buddy's current activity (morgs)

* Mon Dec 10 2007 Dafydd Harries <dafydd.harries@collabora.co.uk> - 0.65-0.30.20071127git5650e153bd
- #4965: Add SyncFriends method as temporary measure for synchronising friends
  list to roster group on Jabber server (Guillaume Desmottes).

* Tue Nov 27 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.29.20071127git150051a3a9
- #4920: harden _add_buddies to cope with no handle when calling
  BuddyHandleJoined (morgs)
- #4993: Only approve subscriptions coming from a trusted server (cassidy)

* Tue Nov 20 2007 Dafydd Harries <dafydd.harries@collabora.co.uk> - 0.65-0.28.20071120git4c8e8b71b5
- #4986: apply patch by Guillaume so that subscribe/presence channel tracking
  is not dependent on which order they appear in

* Wed Nov 14 2007 Dafydd Harries <dafydd.harries@collabora.co.uk> - 0.65-0.27.20071114git128c59c612
- #4936: Enable SSL so we can use DEFLATE compression (robot101)
- #4896: Wait for NewChannel with roster channels to avoid timeout leaving
  you with no buddies (daf)
- #2522: Use an exponential backoff when trying to reconnect CM (cassidy)
- #4907: Try to reconnect Gabble if initial attempt failed (cassidy)

* Tue Nov 13 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.26.20071113git89c33bcf93
- #4660: fix regression in sharing (cassidy)

* Mon Nov 12 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.25.20071112git43d1d48b27
- #4692: correct a wrong part of the #4585 patch to avoid putting sharer in
  'private' property, avoid forcing value of 'private' property on join, and
  clarify related code (smcv)
- #4660: when calling ShareActivity() allow private and tags properties to
  be set in the (previously unused) properties dict (smcv)

* Mon Nov 05 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.24.20071105git944c5280b4
- #4585: Watch activity unique names on D-Bus for disappearences, implying
  the activity crashed; this time, treat that as the local user leaving,
  not as the activity disappearing! (smcv)
- #4659: Revert part of #4585 fix (this part didn't make sense anyway)
  to fix inability to join activities (smcv)
- #4631: don't break the debug log if names are non-ASCII (smcv)

* Fri Nov 02 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.23.20071102git0d8c69c14b
- laptop.org #4585: Leave shared activities if the unique name disappears
  (i.e. the activity instance exits without calling Leave(), probably due to
  a crash) (morgs)

* Fri Nov 02 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.22.20071101git1effa5a10d
- Change python-dbus dependency to dbus-python

* Thu Nov 01 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.21.20071101git1effa5a10d
- laptop.org #2421: improve ability to cope with disconnections and CM crashes
  (morgs)

* Wed Oct 31 2007 Simon McVittie <simon.mcvittie@collabora.co.uk> - 0.65-0.20.20071031git11d8103108
- laptop.org #4027: associate activity debug messages with the relevant
  activity (smcv)
- laptop.org #4537: actually set registered = True (again) (smcv)
- Document requirements python-dbus >= 0.82.0, python-telepathy >= 0.14.0 in
  RPM dependencies (smcv)

* Sun Oct  7 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.19.20071007git6d79687f8b
- New snapshot

* Wed Sep 19 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.18.20070918git6df1f3eca5
- New snapshot

* Mon Sep 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.17.20070917git46898a3e00
- New snapshot

* Wed Sep 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.16.20070912gitb8d04713ac
- New snapshot

* Tue Sep 11 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.15.20070911gitbff163d57b
- New snapshot

* Mon Sep 10 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.14.20070910git3ed091301b
- New snapshot

* Sun Sep  9 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.13.20070909git3b1f4a0c42
- New snapshot

* Tue Sep  4 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.12.20070904gita79f7b6488
- New snapshot

* Thu Aug 30 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.11.20070830git25218b4642
- New snapshot

* Wed Aug 29 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.10.20070829git1c58a0be88
- New snapshot

* Tue Aug 14 2007 John (J5) Palmieri <johnp@redhat.com> - 0.65-0.9.20070814git970ca27db7
- New snapshot

* Wed Aug  1 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.9.20070731git8dc589f5b0
- New snapshot
    * #2214: Gracefully handle blank server field (dcbw)

* Tue Jul 31 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.9.20070731gitfbc25c93ad
- New snapshot
    * Cope with arbitrary Unicode in nicknames, bug#2611 (smcv)

* Tue Jul 31 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.9.20070731gitbc7fc5f02d
- New snapshot

* Fri Jul 27 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.8.20070727gitce62f752b2
- New snapshot

* Fri Jul 20 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.7.20070720git79251459e5
- Return buddy properties as a byte array, not an array of bytes
- Don't list the owner twice in GetBuddies method

* Tue Jul 17 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.7.20070716git650c323462
- New snapshot

* Sun Jul 15 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.6.20070715git6c86d827b5
- Set Buddy current-activity property to none if leaving the current activity
- Hook up to owner current activity change signal so current activity changes
  get propagated
- Fix re-appearance of buddies by actually forgetting about the buddy completely
  when a buddy disappears

* Thu Jul 12 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.6.20070712gitb539f146e9
- New snapshot

* Wed Jul 11 2007 Dan Williams <dcbw@redhat.com> - 0.65-0.5.20070711gite9c851eb8f
- New snapshot

* Mon Jul  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.4.20070709git6f2584d5eb
- New snapshot

* Mon Jul  9 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.3.20070709gite26e3c0294
- New snapshot

* Thu Jun 21 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.2.20070618gite335c3678f
- python-telepathy is the name of the package in Fedora

* Thu Jun 14 2007 Marco Pesenti Gritti <mpg@redhat.com> - 0.65-0.1.20070618gite335c3678f
- Initial build.
