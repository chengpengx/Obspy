# Obspy
some examples about Obspy,such as MDS、Merging.

ObsPy is an open-source project dedicated to provide a Python framework for processing seismological data. 
It provides parsers for common file formats, 
clients to access data centers and seismological signal processing routines which allow the manipulation of seismological time series.

Acknowledging

Please support the project by acknowledging the use of it. This helps us keep it alive. If you use ObsPy (directly or as a dependency of another package) for work resulting in an academic publication, we would be grateful if one of the following papers is cited:

M. Beyreuther, R. Barsch, L. Krischer, T. Megies, Y. Behr and J. Wassermann (2010)
ObsPy: A Python Toolbox for Seismology
SRL, 81(3), 530-533
DOI: 10.1785/gssrl.81.3.530
T. Megies, M. Beyreuther, R. Barsch, L. Krischer, J. Wassermann (2011)
ObsPy – What can it do for data centers and observatories?
Annals Of Geophysics, 54(1), 47-58
DOI: 10.4401/ag-4838
L. Krischer, T. Megies, R. Barsch, M. Beyreuther, T. Lecocq, C. Caudron, J. Wassermann (2015)
ObsPy: a bridge for seismology into the scientific Python ecosystem
Computational Science & Discovery, 8(1), 014003
DOI: 10.1088/1749-4699/8/1/014003
You can also cite the used ObsPy version:
DOIs for released ObsPy versions (e.g. for ObsPy 0.10.2: 10.5281/zenodo.17641)

News

[Feb 17 2019] Release of ObsPy 1.1.1

This is the first bug fix release in the 1.1.x release cycle. It does not change functionality/API but fixes quite a number of bugs resulting in an overall more stable ObsPy package. It is planned to be the only bug fix release for 1.1.x as well as we plan to do the release of 1.2.0 as soon as possible.

We recommend all users to upgrade through one of the usual channels. Please see the full changelog for all details:

Release Including Full Changelog
[Oct 27 2017] Release of ObsPy 1.1.0

This is a major release with a lot of new features, bug fixes, and general improvements and we strongly recommend all users to update. Follow these link to learn more:

What's New in ObsPy 1.1
Release Including Full Changelog
[Feb 27 2017] Release of ObsPy 1.0.3

This is the third bug fix release in the 1.0.x release cycle. It does not change functionality/API but fixes quite a number of bugs resulting in an overall more stable ObsPy package. It is planned to be the last bug fix release for 1.0.x as well as we plan to do the release of 1.1.0 as soon as possible.

We recommend all users to upgrade through one of the usual channels. Please see the full changelog for all details:

Release Including Full Changelog
[Aug 03 2016] Release of ObsPy 1.0.2

This is the second bug fix release in the 1.0 release cycle. It does not change functionality/API but fixes quite a number of bugs resulting in an overall more stable ObsPy package.

We recommend all users to upgrade through one of the usual channels. Please see the full changelog for all details:

Release Including Full Changelog
[Mar 24 2016] Release of ObsPy 1.0.1

This is the first bug fix release in the 1.0 release cycle. It does not change functionality/API but fixes several bugs in 1.0.0, most notably fixing decryption of encrypted data from requests on restricted data via ArcLink and some bugs when working with SAC headers in the rewritten SAC module.

We recommend all users to upgrade through one of the usual channels. Please see the full changelog for all details:

Release Including Full Changelog
[Feb 19 2016] Release of ObsPy 1.0.0

This is a big release with significant internal changes, new features, stability improvements, and much more to prepare ObsPy for future challenges and get rid of accumulated technical debt. It is now stable enough to officially declare it version 1.0. Changes are broad and numerous - follow these links to learn more:

What's New in ObsPy 1.0
Release Including Full Changelog
[May 15 2015] Release of ObsPy 0.10.2

ObsPy 0.10.2 is a maintenance release and it contains a number of bug fixes and minor feature improvements so we advise all users to upgrade through one of the usual channels.

Release Including Full Changelog
[March 20 2015] Release of ObsPy 0.10.1

ObsPy 0.10.1 is once again our biggest release yet with over 2200 single commits from 25 individual contributors! We strongly encourage all users to update to the new version as it will effectively end support for the 0.9.x line. Major new features are Python 3 support, a new TauP implementation, Anaconda packages, ...

Release Including Full Changelog
What's New in ObsPy 0.10.1
[May 4 2014] Release of ObsPy 0.9.2

ObsPy 0.9.2 is a maintenance release and contains the collective bug fixes and minor feature improvements of around 150 commits so we advise all users to upgrade.

Release including full changelog
[January 9 2014] Release of ObsPy 0.9.0

ObsPy 0.9.0 offers (amongst many other things) two major new features: support for the FDSN webservices and the FDSN StationXML format.

Release including full changelog
Migration to ObsPy 0.9.0
Getting Started

The ObsPy Gallery and its related ObsPy Tutorial are maybe the best point to get a first impression of what ObsPy is all about. The tutorial is a collection of short example programs with explanations and program output. For help getting started with Python, have a look at this collection of links to Tutorials.

Installation

ObsPy is currently running and tested on Linux (32 and 64 bit), Windows (32 bit and/or 64 bit) and Mac OS X.

ObsPy runs on Python 2.7, 3.4, 3.5, and 3.6. We highly recommend and only officially support the latest release of each series. Additionally, we recommend you use the latest version of python 3 if possible.

For individual users we strongly recommend Installation via Anaconda.

System administrators can also install system packages (where available, see below). Detailed information on installing the latest stable version of ObsPy on various operating systems:

via Anaconda, a scientific Python distribution (all systems) (works without root access)
normal installation via Anaconda installer
installation using bundled Anaconda installer
Debian/Ubuntu via the package manager
Fedora/CentOS via the package manager
Mac OS X via Homebrew or MacPorts
Windows from a pre-build package (PyPI) or from source
FreeBSD via the package manager
NetBSD via the package manager
via PyPi or from source, applicable to Linux and OSX
into an existing Antelope 5.4 on RHEL/CentOS 6
for a reproducible installation mostly aimed at servers and clusters, have a look at the Salt formula for ObsPy
If you run into problems when following the above installation instructions, you can ask for help in our gitter chat room: https://gitter.im/obspy/obspy

If you intend on making changes to ObsPy or develop for it, read this:

Developer Installation
If you intend on performing parallel processing with Python and Obspy, please read the following:

Notes on Parallel Processing with Python and ObsPy
Stay Informed

If you are using ObsPy we strongly recommend you join the [obspy-announcements] and the [obspy-users] mailing lists. The [obspy-announcements] list will be the place where new additions, important changes and bug fixes will be announced and thus will be very low volume. The [obspy-users] list is used to contact other ObsPy users for questions and open discussions.

Please keep all conversations in English when using the ObsPy mailing lists, thanks!

[obspy-announcements]

Subscribe / Unsubscribe
Browse the archive
[obspy-users]

Subscribe / Unsubscribe
Post a message
Browse the archive
Follow us on Twitter

For more frequent news and general information on Python in seismology/science, follow us on twitter: @obspy

There also is a feed for commits. To get emails concerning issues make a GitHub login, 'watch' our repository and set up email notifications for your GitHub account.

Documentation

for the latest stable release
start page
overview of submodules
for the current developer version
archive for other versions
Use Cases / Applications Using ObsPy

ObsPyck
SeismicHandler
SeisHub
SeishubExplorer
HtoVToolbox
wavePicker
Antelope Python moment tensor code
Using ObsPy with py2exe
Whisper
Wavesdownloader (on GitHub)
ADMIRE project
pSysmon
ObsPyDMT
seedlink plotter
pyTDMT - Python Time Domain Moment Tensor (on GitHub)
MSNoise - Monitoring Seismic Velocity Changes using Ambient Seismic Noise (on GitHub)
Pisces: A practical seismological database library in Python (on GitHub)
HASHpy: Python wrapped fork of HASH first motion focal mechanism code
waveloc (on GitHub)
scisola (on GitHub)
instaseis - Instant Global High Frequency Seismograms
LASIF - Large-Scale Seismic Inversion Framework
pyflex - Enhanced port of FLEXWIN
hypoDDpy - Run hypoDD in a data driven manner.
wfs_input_generator - Generate input files for many waveform solvers directly from data.
rf - Calculate receiver functions.
Qopen - Separation of intrinsic and scattering Q by envelope inversion.
EQcorrscan - Match-filter earthquake detection
PhasePApy - a Seismic Phase Picker and Associator program package
Jane - Document database for Seismology
MouseTrap - A module for detecting a special type of disturbance (so called mouse, ping, or fling step) in seismic records.
Lazylyst - A GUI created for time series review, using a flexible framework for new workflows.
REDPy - A tool for automated detection and analysis of repeating earthquakes in continuous data.
CodaNorm - A software package for the body-wave attenuation calculation by the coda-normalization method
ISOLA-ObsPy - A seismic source inversion module. Events are described as point sources with centroid moment tensors.
pySW4 - Setup, run, post process, and visualize numerical simulations, primarily for SW4.
yam - Yet another monitoring tool using correlations of ambient noise.
PyWeed - a cross-platform downloadable app for retrieving event-based seismic data
SeisTomoPy - Fast visualization, comparison and calculations in global tomographic models
Detex - A Python package for subspace detection and waveform similarity clustering
miscellaneous..

https://github.com/ndperezg/taller_obspy
https://github.com/dansand/seismic
https://github.com/kallstadt-usgs/seisk
https://github.com/ovsm-dev/sdp
https://github.com/viictorjs/SEG2Py
https://github.com/xumi1993/seispy
https://github.com/rizac/stream2segment
https://github.com/pysit/pysit
https://github.com/lizstarin/earthquakemap
https://github.com/samhaug/seispy
https://github.com/oceanobservatories/mi-instrument
https://github.com/echavess/Focal-mechanisms-Pressure-and-Tension-Axis
Developer Corner

Style Guide
Docs or it doesn't exist!
ObsPy Git Branching Model
Doing a new ObsPy release
Known Python issues
Performance Tips:
Python
NumPy and ctypes
SciPy
NumPy Book
Testing, Debugging & Profiling
Sphinx Documentation
Notes on the performed svn to git migration
Interesting reading on git, github
Debian packaging
How to: Add a new Submodule
Affiliated Project Guidelines
