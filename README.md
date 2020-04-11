# nosey_neighbour
<h2>Automated Basic Enumeration Tools for Penetration Testing.</h2>

<h5>Assumes Kali / ParrotOS distro which includes: Dirb, Nikto, Nmap, Enum4linux</h5>

**Installation is easy:**
`cd /opt; git clone https://github.com/stick-fish/nosey_neighbour.git ; cd /opt/nosey_neighbour; chmod 755 nosey.py`

**Basic Usage:**
`./nosey.py 10.10.10.123`

<h3>Recent changes made:</h3>

**V1.0**
- Segregated nikto and dirb scans into their own files, making the main script less clutterd.
- Added a little ASCII art because who doesnt like art.
  - ASCII ART: `http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20`

**V1.1**
- Added in Enum4linux
- Color to headings

 **V1.2** (Forked Version)
- Added options for non default ports for HTTP/HTTPS service scans

 **V1.3** (Forked Version)
- Added License
- Added Brute Force Functions
- Added More HTTP/HTTPS Scans
- Added More Directory Scans
- Added Eyewitness Screenshots for HTTP/HTTPS
- Added Windows Service Scans
- Updated Ascii Art

 
 **********************************************************************************************************
 
 TODO:
- Include additional scanning
- Incorporate pass the hash
- Include the option to change Nmap flags 
- Change to full class to remove if...else for every port
- Fix Brute Force
- Add More Intelligent WWW Enumeration & Scans
- Add More Active Directory Enumeration & Scans
