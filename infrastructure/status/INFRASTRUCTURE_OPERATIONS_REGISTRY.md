# INFRASTRUCTURE OPERATIONS REGISTRY

STATUS:
AUTHORITATIVE

PURPOSE:
Authoritative registry of machines, roles, access methods, canonical storage locations, project locations, and operational rules.

---

# MACHINES

## BOSGAME

Hostname:
remo-speed-Ecolite-Series

Role:
Canonical Storage Server

Primary Functions:
- Canonical storage
- Foundation storage
- Project archive storage
- PROJECT_DATA storage
- Photo review staging

Tailscale IPv4:
100.125.192.45

Tailscale IPv6:
fd7a:115c:a1e0::8436:c02d

User:
remo-speed

Home:
/home/remo-speed

---

## OPTIPLEX

Hostname:
remospeed-OptiPlex-7010

Role:
Primary Processing Workstation

Primary Functions:
- Active project work
- Repository maintenance
- Music authority workflows
- Infrastructure planning

Tailscale IPv4:
100.97.207.91

Tailscale IPv6:
fd7a:115c:a1e0::d036:cf5b

User:
remospeed

Home:
/home/remospeed

---

## LENOVO

Hostname:
remo-speed-Lenovo-G70-70

Role:
Continuity Workstation

Primary Functions:
- Operational continuity
- Secondary project workstation
- Remote administration

Tailscale IPv4:
100.79.167.69

Tailscale IPv6:
fd7a:115c:a1e0::5e36:a745

User:
remo-speed

Home:
/home/remo-speed

---

# CANONICAL STORAGE

Server:
BOSGAME

Root:
/srv/storage

Foundation:
/srv/storage/Foundation

Projects:
/srv/storage/Projects

Project Data:
/srv/storage/PROJECT_DATA

Music:
/srv/storage/Music

Photos:
/srv/storage/Fotos

---

# FOUNDATION LOCATIONS

Canonical:
 /srv/storage/Foundation

OPTIPLEX Local:
 /home/remospeed/Media/Operational_Foundation

Template:
 /srv/storage/Foundation/PROJECT00_TEMPLATE

---

# PROJECT REPOSITORY WORKING COPIES

OPTIPLEX:
 /home/remospeed/codex_work

LENOVO:
 /home/remo-speed/codex_work

Archive Copies:
 /srv/storage/Projects

---

# PROJECT DATA

Canonical Location:
 /srv/storage/PROJECT_DATA

Infrastructure Project:
 /srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION

Photo Review Staging:
 /srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION/staging/photo_review

---

# OPERATIONAL RULES

1. BOSGAME is the canonical storage server.

2. OPTIPLEX is the primary processing workstation.

3. LENOVO is the continuity workstation.

4. Repository synchronization occurs through Git/GitHub.

5. Canonical project storage resides on BOSGAME.

6. Repository working copies on OPTIPLEX and LENOVO are legitimate operational clones.

7. Copy completion alone does not authorize deletion.

8. Deletion requires:
   - verification
   - documented approval
   - execution logging

9. Photo consolidation does not authorize deletion of OPTIPLEX photo collections.

10. Music collections remain preserved on OPTIPLEX until a future music organization phase.

