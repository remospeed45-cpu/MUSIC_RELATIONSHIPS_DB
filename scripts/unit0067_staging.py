import csv
import os

# Data extracted from web_fetch for Batch 0005
releases = [
    {
        "rel_id": "SRC0002-B0005-REL001",
        "title": "Colección 100 Parranderas del Siglo",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-parranderas-del-siglo/",
        "format": "USB",
        "ref": "GE5018",
        "tracks": [
            ("1", "Echele Agua a la Sopa", "Los Alegres Parranderos"),
            ("2", "El Enredo", "Joaquín Bedoya y Su Conjunto"),
            ("3", "El Duende Alegre", "Los Alegres Parranderos"),
            ("4", "La Encomienda", "Agustín Bedoya y Su Conjunto"),
            ("5", "La Dulce Toma", "Los Alegres Parranderos"),
            ("6", "La Boquitrompona", "El Manicomio de Vargasvil"),
            ("7", "Que lo Diga Ella", "Los Alegres Parranderos"),
            ("8", "Las Piponchas", "Agustín Bedoya y Su Conjunto"),
            ("9", "Ya Voy Toño", "Los Alegres Parranderos"),
            ("10", "Mi Novia de Malas", "Los Integrados")
        ]
    },
    {
        "rel_id": "SRC0002-B0005-REL002",
        "title": "Colección 100 Exitos de Diciembre",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-exitos-de-diciembre-usb-8-gb/",
        "format": "USB",
        "ref": "GE5017",
        "tracks": [
            ("1", "Feliz Nochebuena", "Los Hispanos"),
            ("2", "Bella es la Navidad", "Ricardo Ray - Bobby Cruz"),
            ("3", "En la Nochebuena", "La Sonora Matancera"),
            ("4", "Ron de Vinola", "Guillermo Buitrago"),
            ("5", "El Hijo Ausente", "Pastor López y Su Combo"),
            ("6", "Maldita Navidad", "Gabriel Romero y Su Orquesta"),
            ("7", "El Pesebre", "Afrosound"),
            ("8", "Aires de Navidad", "Los Titanes"),
            ("9", "Grito Vagabundo", "Guillermo Buitrago"),
            ("10", "Pascua en Navidad", "Luis Felipe González")
        ]
    },
    {
        "rel_id": "SRC0002-B0005-REL003",
        "title": "Colección 100 Villancicos del Siglo",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-villancicos-del-siglo-usb-8-gb/",
        "format": "USB",
        "ref": "GE5013",
        "tracks": [
            ("1", "Niño del Alma Mía", "Varios Artistas"),
            ("2", "Feliz Navidad", "Varios Artistas"),
            ("3", "Tutaina", "Varios Artistas"),
            ("4", "Salve Reina y Madre", "Varios Artistas"),
            ("5", "Zagalillo", "Varios Artistas"),
            ("6", "Antón", "Varios Artistas"),
            ("7", "La Nanita Nana", "Varios Artistas"),
            ("8", "Vamos Vamos Pastorcitos", "Varios Artistas"),
            ("9", "El Burrito de Belén", "Varios Artistas"),
            ("10", "Dónde Están Mis Juguetes", "Varios Artistas")
        ]
    },
    {
        "rel_id": "SRC0002-B0005-REL004",
        "title": "Colección 100 Exitos de Pastor López",
        "artist": "Pastor López",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-exitos-de-pastor-lopez-usb-8-gb/",
        "format": "USB",
        "ref": "GE5012",
        "tracks": [
            ("1", "Solo Un Cigarro", "Pastor López"),
            ("2", "Tempestad", "Pastor López"),
            ("3", "Traicionera", "Pastor López"),
            ("4", "El Hijo Ausente", "Pastor López"),
            ("5", "Golpe con Golpe", "Pastor López"),
            ("6", "Fue Por Una Cerveza", "Pastor López"),
            ("7", "Añoranza Febril", "Pastor López"),
            ("8", "Brisas del Valle", "Pastor López"),
            ("9", "Cállate Corazón", "Pastor López"),
            ("10", "El Ausente", "Pastor López")
        ]
    },
    {
        "rel_id": "SRC0002-B0005-REL005",
        "title": "Colección 100 Exitos de Los Corraleros de Majagual",
        "artist": "Los Corraleros de Majagual",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-exitos-de-los-corraleros-de-majagual-usb-8-gb/",
        "format": "USB",
        "ref": "GE5009",
        "tracks": [
            ("1", "Los Sabanales", "Los Corraleros de Majagual"),
            ("2", "La Yerbita", "Los Corraleros de Majagual"),
            ("3", "No Me Busques", "Los Corraleros de Majagual"),
            ("4", "Suéltala Pa' Que Se Defienda", "Los Corraleros de Majagual"),
            ("5", "Tres Tigres", "Los Corraleros de Majagual"),
            ("6", "Cumbiamberita", "Los Corraleros de Majagual"),
            ("7", "Cumbia Saramuya", "Los Corraleros de Majagual"),
            ("8", "El Bailador", "Los Corraleros de Majagual"),
            ("9", "El Pasmao", "Los Corraleros de Majagual"),
            ("10", "El Tamarindo", "Los Corraleros de Majagual")
        ]
    }
]

# Helper to split artists (extended for this batch)
def split_artists(text):
    text = text.replace(" - ", ", ")
    text = text.replace(" y Su Conjunto", "").replace(" y Su Combo", "").replace(" y Su Orquesta", "")
    artists = [a.strip() for a in text.split(",")]
    return artists

# Prepare artist candidates
artist_map = {}
artist_count = 0

# Staging data containers
recordings_data = []
songs_data = []
artists_data = []
rel_rec_song = []
rel_rec_artist = []
rel_rec_rel = []
rel_rec_src = []

rec_count = 0
song_count = 0

for rel in releases:
    for track_num, track_title, artist_text in rel["tracks"]:
        rec_count += 1
        rec_id = f"SRC0002-B0005-REC{rec_count:03d}"
        
        song_count += 1
        song_id = f"SRC0002-B0005-SONG{song_count:03d}"
        
        # Recording Staging
        recordings_data.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0002",
            "source_name": "Discos Fuentes",
            "source_url": rel["url"],
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "release_interpreter": rel["artist"],
            "release_genre": "Tropical/Seasonal",
            "release_format": rel["format"],
            "release_year": "",
            "reference_number": rel["ref"],
            "side": "",
            "track_number": track_num,
            "global_track_number": str(rec_count),
            "raw_track_title": track_title,
            "recording_title": track_title,
            "artist_text": artist_text,
            "label_name": "Discos Fuentes",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Song Staging
        songs_data.append({
            "batch_song_id": song_id,
            "source_id": "SRC0002",
            "source_name": "Discos Fuentes",
            "source_url": rel["url"],
            "canonical_song_title_candidate": track_title,
            "raw_track_title": track_title,
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "side": "",
            "track_number": track_num,
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Artist Candidates
        current_artists = split_artists(artist_text)
        for a_text in current_artists:
            if a_text not in artist_map:
                artist_count += 1
                art_id = f"SRC0002-B0005-ART{artist_count:03d}"
                artist_map[a_text] = art_id
                
                artists_data.append({
                    "artist_candidate_id": art_id,
                    "source_id": "SRC0002",
                    "source_name": "Discos Fuentes",
                    "source_url": rel["url"],
                    "raw_artist_text": a_text,
                    "candidate_artist_type": "group_candidate" if any(x in a_text for x in ["Conjunto", "Orquesta", "Combo", "Los ", "La ", "El Manicomio", "Integrados", "Niños Cantores"]) else "performer_candidate_needs_review",
                    "release_candidate_id": rel["rel_id"],
                    "release_title": rel["title"],
                    "source_reference": rel["url"],
                    "evidence_text": f"Artist text appears on Discos Fuentes shop product page for release '{rel['title']}': {a_text}",
                    "confidence": "medium-high",
                    "review_status": "staged_for_review"
                })
            
            art_id = artist_map[a_text]
            rel_rec_artist.append({
                "batch_recording_id": rec_id,
                "artist_candidate_id": art_id,
                "raw_artist_text": a_text,
                "relationship_type": "credited_artist_candidate",
                "source_id": "SRC0002",
                "source_reference": f"{rel['url']}#track-{track_num}",
                "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
                "confidence": "high",
                "review_status": "staged_for_review"
            })
            
        # Relationships
        rel_rec_song.append({
            "batch_recording_id": rec_id,
            "batch_song_id": song_id,
            "relationship_type": "track_title_match",
            "source_id": "SRC0002",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        rel_rec_rel.append({
            "batch_recording_id": rec_id,
            "release_candidate_id": rel["rel_id"],
            "relationship_type": "track_of_release",
            "source_id": "SRC0002",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        rel_rec_src.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0002",
            "source_url": rel["url"],
            "relationship_type": "primary_source",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Discos Fuentes shop product page: release='{rel['title']}', track='{track_num}', raw_track='{track_title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })

# Write TSVs
def write_tsv(filename, data):
    if not data: return
    fieldnames = sorted(list(data[0].keys()))
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

os.makedirs('authority/staging', exist_ok=True)
os.makedirs('relationships/staging', exist_ok=True)

write_tsv('authority/staging/src0002_batch0005_recordings.tsv', recordings_data)
write_tsv('authority/staging/src0002_batch0005_songs.tsv', songs_data)
write_tsv('authority/staging/src0002_batch0005_artist_candidates.tsv', artists_data)

write_tsv('relationships/staging/src0002_batch0005_recording_song.tsv', rel_rec_song)
write_tsv('relationships/staging/src0002_batch0005_recording_artist_candidate.tsv', rel_rec_artist)
write_tsv('relationships/staging/src0002_batch0005_recording_release.tsv', rel_rec_rel)
write_tsv('relationships/staging/src0002_batch0005_recording_source.tsv', rel_rec_src)

print(f"Processed {len(releases)} releases, {rec_count} tracks, {len(artists_data)} artists.")
