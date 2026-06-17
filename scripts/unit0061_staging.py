import csv
import os

# Data extracted from web_fetch
releases = [
    {
        "rel_id": "SRC0002-B0003-REL001",
        "title": "LP - Cumbia y Nada Más",
        "artist": "Afrosound",
        "url": "https://tiendadiscosfuentes.com/productos/vinilos/lp-cumbia-y-nada-mas/",
        "format": "LP Estereo 33 RPM",
        "tracks": [
            ("A1", "La Danza del Mono", "Afrosound"),
            ("A2", "Cumbia y Nada Más", "Afrosound"),
            ("A3", "Trueno", "Afrosound (Feat. Fruko)"),
            ("A4", "Cumbia de Mis Penas", "Afrosound"),
            ("A5", "Afrocumbé", "Afrosound"),
            ("B1", "La Chula Loba", "Afrosound"),
            ("B2", "El Aguacero", "Afrosound"),
            ("B3", "Mardito", "Afrosound"),
            ("B4", "Cajita de Cumbia", "Afrosound"),
            ("B5", "Chiribiquete", "Afrosound"),
            ("B6", "Kadett Cabalga", "Afrosound (Feat. Chill Mafia y Ben Yart)")
        ]
    },
    {
        "rel_id": "SRC0002-B0003-REL002",
        "title": "LP - Historia Musical",
        "artist": "Los 50 de Joselito",
        "url": "https://tiendadiscosfuentes.com/productos/vinilos/lp-historia-musical-los-50-de-joselito/",
        "format": "LP Estereo 33 RPM",
        "tracks": [
            ("A1", "Dame Tu Mujer José", "Los 50 de Joselito"),
            ("A2", "El Pájaro Amarillo", "Los 50 de Joselito"),
            ("A3", "María Teresa", "Los 50 de Joselito"),
            ("A4", "El Aguacero", "Los 50 de Joselito"),
            ("A5", "El Ron de Vinola", "Los 50 de Joselito"),
            ("A6", "La Pringamoza", "Los 50 de Joselito"),
            ("A7", "Grito Vagabundo", "Los 50 de Joselito"),
            ("B1", "Las Mujeres a Mí No Me Quieren", "Los 50 de Joselito"),
            ("B2", "El Negro Picante", "Los 50 de Joselito"),
            ("B3", "Lo Gotereros", "Los 50 de Joselito"),
            ("B4", "Rosa María", "Los 50 de Joselito"),
            ("B5", "La Araña Picua", "Los 50 de Joselito"),
            ("B6", "Arbolito de Navidad", "Los 50 de Joselito")
        ]
    },
    {
        "rel_id": "SRC0002-B0003-REL003",
        "title": "Colección 100 Exitos de La Sonora Matancera",
        "artist": "La Sonora Matancera",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-exitos-de-la-sonora-matancera/",
        "format": "USB",
        "tracks": [
            ("1", "El Sofá", "La Sonora Matancera"),
            ("2", "Quién Será", "La Sonora Matancera"),
            ("3", "Burundanga", "La Sonora Matancera"),
            ("4", "Todo Me Gusta de Ti", "La Sonora Matancera"),
            ("5", "El Mambo es Universal", "La Sonora Matancera"),
            ("6", "Cuando Tú Seas Mía", "La Sonora Matancera"),
            ("7", "Oye Mima", "La Sonora Matancera"),
            ("8", "Desesperación", "La Sonora Matancera"),
            ("9", "Quedé Zaina", "La Sonora Matancera"),
            ("10", "Historia de Un Amor", "La Sonora Matancera")
        ]
    },
    {
        "rel_id": "SRC0002-B0003-REL004",
        "title": "Colección 100 Exitos del Siglo: Joe Arroyo",
        "artist": "Joe Arroyo",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-exitos-del-siglo-joe-arroyo/",
        "format": "USB",
        "tracks": [
            ("1", "A Mi Dios Todo le Debo", "Joe Arroyo"),
            ("2", "Confundido", "Joe Arroyo"),
            ("3", "El Arbol", "Joe Arroyo"),
            ("4", "El Caminante", "Joe Arroyo"),
            ("5", "El Centurión de la Noche", "Joe Arroyo"),
            ("6", "El Cocinero Mayor", "Joe Arroyo"),
            ("7", "El Son del Caballo", "Joe Arroyo"),
            ("8", "La Maestranza # 1", "Joe Arroyo"),
            ("9", "Por Ti No Moriré", "Joe Arroyo"),
            ("10", "Teresa Vuelve", "Joe Arroyo")
        ]
    },
    {
        "rel_id": "SRC0002-B0003-REL005",
        "title": "Colección 100 Exitos de Los Corraleros de Majagual",
        "artist": "Los Corraleros de Majagual",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-exitos-de-los-corraleros-de-majagual-usb-8-gb/",
        "format": "USB",
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
    },
    {
        "rel_id": "SRC0002-B0003-REL006",
        "title": "Colección 100 Exitos – Cuatro Grandes de la Música Tropical",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-exitos-cuatro-grandes-de-la-musica-tropical/",
        "format": "USB",
        "tracks": [
            ("1", "Festival en Guararé", "Los Corraleros de Majagual"),
            ("2", "Playas Marinas", "Calixto Ochoa y Su Conjunto"),
            ("3", "Te Llevaré", "Lisandro Meza y Su Conjunto"),
            ("4", "Celos de Amor", "Armando Hernández con el Combo Caribe"),
            ("5", "Esta Noche es Mía", "Alfredo Gutiérrez y Su Conjunto"),
            ("6", "Mata E Caña", "Calixto Ochoa y Su Conjunto"),
            ("7", "Entre Rejas", "Lisandro Meza y Su Conjunto"),
            ("8", "La Zenaida", "Armando Hernández con el Combo Caribe"),
            ("9", "Dos Mujeres", "Alfredo Gutiérrez y Su Conjunto"),
            ("10", "Los Sabanales", "Los Corraleros de Majagual")
        ]
    },
    {
        "rel_id": "SRC0002-B0003-REL007",
        "title": "Colección 100 - Homenaje a Toño Fuentes",
        "artist": "Toño Fuentes",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-homenaje-a-tono-fuentes/",
        "format": "USB",
        "tracks": [
            ("1", "Cosas Como Tu", "Toño Fuentes"),
            ("2", "Huri", "Toño Fuentes"),
            ("3", "La Cumparsita", "Toño Fuentes"),
            ("4", "Mis Flores Negras", "Toño Fuentes"),
            ("5", "Ojos Negros", "Toño Fuentes"),
            ("6", "Perdón", "Toño Fuentes"),
            ("7", "Prenda del Alma", "Toño Fuentes"),
            ("8", "Prisionero de Tus Brazos", "Toño Fuentes"),
            ("9", "Pueblito Viejo", "Toño Fuentes"),
            ("10", "Quiéreme Mucho", "Toño Fuentes")
        ]
    }
]

# Helper to split artists
def split_artists(text):
    # Very basic split for "Feat.", "(Feat.", etc.
    text = text.replace(" (Feat. ", ", ").replace(" (feat. ", ", ").replace(" Feat. ", ", ").replace(" feat. ", ", ").replace(")", "")
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
        rec_id = f"SRC0002-B0003-REC{rec_count:03d}"
        
        song_count += 1
        song_id = f"SRC0002-B0003-SONG{song_count:03d}"
        
        side = track_num[0] if track_num[0] in "AB" else ""
        num = track_num[1:] if side else track_num
        
        # Recording Staging
        recordings_data.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0002",
            "source_name": "Discos Fuentes",
            "source_url": rel["url"],
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "release_interpreter": rel["artist"],
            "release_genre": "Tropical", # Placeholder
            "release_format": rel["format"],
            "release_year": "",
            "reference_number": "",
            "side": side,
            "track_number": num,
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
            "side": side,
            "track_number": num,
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
                art_id = f"SRC0002-B0003-ART{artist_count:03d}"
                artist_map[a_text] = art_id
                
                artists_data.append({
                    "artist_candidate_id": art_id,
                    "source_id": "SRC0002",
                    "source_name": "Discos Fuentes",
                    "source_url": rel["url"],
                    "raw_artist_text": a_text,
                    "candidate_artist_type": "group_candidate" if "Conjunto" in a_text or "Combo" in a_text or "Los " in a_text or "La " in a_text else "performer_candidate_needs_review",
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
def write_tsv(filename, data, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

os.makedirs('authority/staging', exist_ok=True)
os.makedirs('relationships/staging', exist_ok=True)

write_tsv('authority/staging/src0002_batch0003_recordings.tsv', recordings_data, recordings_data[0].keys())
write_tsv('authority/staging/src0002_batch0003_songs.tsv', songs_data, songs_data[0].keys())
write_tsv('authority/staging/src0002_batch0003_artist_candidates.tsv', artists_data, artists_data[0].keys())

write_tsv('relationships/staging/src0002_batch0003_recording_song.tsv', rel_rec_song, rel_rec_song[0].keys())
write_tsv('relationships/staging/src0002_batch0003_recording_artist_candidate.tsv', rel_rec_artist, rel_rec_artist[0].keys())
write_tsv('relationships/staging/src0002_batch0003_recording_release.tsv', rel_rec_rel, rel_rec_rel[0].keys())
write_tsv('relationships/staging/src0002_batch0003_recording_source.tsv', rel_rec_src, rel_rec_src[0].keys())

print(f"Processed {len(releases)} releases, {rec_count} tracks, {len(artists_data)} artists.")
