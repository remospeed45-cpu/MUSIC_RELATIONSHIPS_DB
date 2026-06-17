import csv
import os

# Data extracted from web_fetch for Batch 0004 (Unique releases)
releases = [
    {
        "rel_id": "SRC0002-B0004-REL001",
        "title": "Colección 100 Mejores Canciones de Música Colombiana del Siglo",
        "artist": "Varios Intérpretes",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-canciones-musica-colombiana/",
        "format": "USB",
        "ref": "GE5007",
        "tracks": [
            ("1", "Yo También Tuve Veinte Años", "Varios Intérpretes"),
            ("2", "Las Acacias", "Varios Intérpretes"),
            ("3", "Ayer Me Echaron Del Pueblo", "Varios Intérpretes"),
            ("4", "Un Recuerdo De Amor", "Varios Intérpretes"),
            ("5", "Grato Silencio", "Varios Intérpretes"),
            ("6", "Pesares", "Varios Intérpretes"),
            ("7", "Antioqueñita", "Varios Intérpretes"),
            ("8", "Tierra Labrantía", "Varios Intérpretes"),
            ("9", "Las Mirlas", "Varios Intérpretes"),
            ("10", "Huri", "Varios Intérpretes")
        ]
    },
    {
        "rel_id": "SRC0002-B0004-REL002",
        "title": "Colección 100 Éxitos del Siglo | Helenita Vargas",
        "artist": "Helenita Vargas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-exitos-helenita-vargas/",
        "format": "USB",
        "ref": "GE5034",
        "tracks": [
            ("1", "María de los Guardias", "Helenita Vargas"),
            ("2", "Señor", "Helenita Vargas"),
            ("3", "No Te Pido Más", "Helenita Vargas"),
            ("4", "Castiga Tirano", "Helenita Vargas"),
            ("5", "Señora", "Helenita Vargas"),
            ("6", "Mal Hombre", "Helenita Vargas"),
            ("7", "Propiedad Privada", "Helenita Vargas"),
            ("8", "La Hija del Penal", "Helenita Vargas"),
            ("9", "Me la Robaste", "Helenita Vargas"),
            ("10", "Nos Estorbó la Ropa", "Helenita Vargas")
        ]
    },
    {
        "rel_id": "SRC0002-B0004-REL004",
        "title": "Colección 100 Éxitos de Música Cubana",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-exitos-de-musica-cubana/",
        "format": "USB",
        "ref": "GE5029",
        "tracks": [
            ("1", "El Carretero", "Guillermo Portabales"),
            ("2", "Malao de Caña", "La Sonora Matancera"),
            ("3", "El Que Siembra Su Maíz", "Orquesta de Bebo Valdés"),
            ("4", "A San Lázaro (Babalú)", "Celina y Reutilio"),
            ("5", "Lupita", "Fruko y Orquesta"),
            ("6", "Yo Tengo Pena", "Los Compadres"),
            ("7", "Mira Que Eres Linda", "Roberto Ledesma"),
            ("8", "Alegre Petición", "Trío Matamoros"),
            ("9", "Nuevamente", "Orlando Contreras"),
            ("10", "Adiós Compay Gato", "Los Guaracheros de Oriente")
        ]
    },
    {
        "rel_id": "SRC0002-B0004-REL005",
        "title": "Colección 100 - Que Viva Diciembre",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-que-viva-diciembre/",
        "format": "USB",
        "ref": "GE5028",
        "tracks": [
            ("1", "Las Tapas", "Varios Artistas"),
            ("2", "Quiero Ser Feliz", "Varios Artistas"),
            ("3", "Amor Serrano", "Varios Artistas"),
            ("4", "Plegaria", "Varios Artistas"),
            ("5", "Capullo De Rosa Blanca", "Varios Artistas"),
            ("6", "El Bailador", "Varios Artistas"),
            ("7", "Cumbia Árabe", "Varios Artistas"),
            ("8", "La Boquitrompona", "Varios Artistas"),
            ("9", "El Porteñito", "Varios Artistas"),
            ("10", "La Cerveza", "Varios Artistas")
        ]
    },
    {
        "rel_id": "SRC0002-B0004-REL009",
        "title": "Colección 100 Cumbias, Porros y Gaitas del Siglo",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/usb-coleccion-100-cumbias-porros-y-gaitas-del-siglo/",
        "format": "USB",
        "ref": "GE5015",
        "tracks": [
            ("1", "La Sombra de Tu Sonrisa", "Pacho Galán y Su Orquesta"),
            ("2", "Santo Domingo", "Los Cumbiamberos de Pacheco"),
            ("3", "El Toro Miura", "Los Corraleros de Majagual"),
            ("4", "Cumbia en Do Menor", "Lito Barrientos y Su Orquesta"),
            ("5", "El Tirabuzón", "Clímaco Sarmiento y Su Orquesta"),
            ("6", "La Morena Encarnación", "Los Corraleros de Majagual"),
            ("7", "La Ñeca", "Pedro Laza y Sus Pelayeros"),
            ("8", "Cumbia Cienaguera", "Conjunto Típico Vallenato"),
            ("9", "En la Madrugá", "Pacho Galán y Su Orquesta"),
            ("10", "Cumbia Sampuesana", "Conjunto Típico Vallenato")
        ]
    },
    {
        "rel_id": "SRC0002-B0004-REL010",
        "title": "Colección 100 Canciones Infantiles",
        "artist": "Varios Artistas",
        "url": "https://tiendadiscosfuentes.com/productos/musica-memoria-usb/colecciones-usb/coleccion-100-canciones-infantiles/",
        "format": "USB",
        "ref": "GE5011",
        "tracks": [
            ("1", "El Barquito", "Varios Artistas"),
            ("2", "La Chivita", "Varios Artistas"),
            ("3", "Los Diez Perritos", "Varios Artistas"),
            ("4", "El Cucú", "Varios Artistas"),
            ("5", "La Gallinita Josefina", "Varios Artistas"),
            ("6", "Los Pollitos Dicen", "Varios Artistas"),
            ("7", "Arriba Juan", "Varios Artistas"),
            ("8", "La Mar", "Varios Artistas"),
            ("9", "Pulgarcito", "Varios Artistas"),
            ("10", "La Cucaracha", "Varios Artistas")
        ]
    }
]

# Helper to split artists
def split_artists(text):
    text = text.replace(" (Feat. ", ", ").replace(" (feat. ", ", ").replace(" Feat. ", ", ").replace(" feat. ", ", ").replace(")", "")
    text = text.replace(" y Su Conjunto", "").replace(" y Su Orquesta", "").replace(" con el Combo Caribe", "").replace(" y Sus Pelayeros", "")
    # Note: Keep the full text for candidate, but might split for multiple performers
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
        rec_id = f"SRC0002-B0004-REC{rec_count:03d}"
        
        song_count += 1
        song_id = f"SRC0002-B0004-SONG{song_count:03d}"
        
        # Recording Staging
        recordings_data.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0002",
            "source_name": "Discos Fuentes",
            "source_url": rel["url"],
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "release_interpreter": rel["artist"],
            "release_genre": "Tropical",
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
                art_id = f"SRC0002-B0004-ART{artist_count:03d}"
                artist_map[a_text] = art_id
                
                artists_data.append({
                    "artist_candidate_id": art_id,
                    "source_id": "SRC0002",
                    "source_name": "Discos Fuentes",
                    "source_url": rel["url"],
                    "raw_artist_text": a_text,
                    "candidate_artist_type": "group_candidate" if any(x in a_text for x in ["Conjunto", "Orquesta", "Combo", "Los ", "La ", "Trío", "Guaracheros", "Compadres"]) else "performer_candidate_needs_review",
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

write_tsv('authority/staging/src0002_batch0004_recordings.tsv', recordings_data)
write_tsv('authority/staging/src0002_batch0004_songs.tsv', songs_data)
write_tsv('authority/staging/src0002_batch0004_artist_candidates.tsv', artists_data)

write_tsv('relationships/staging/src0002_batch0004_recording_song.tsv', rel_rec_song)
write_tsv('relationships/staging/src0002_batch0004_recording_artist_candidate.tsv', rel_rec_artist)
write_tsv('relationships/staging/src0002_batch0004_recording_release.tsv', rel_rec_rel)
write_tsv('relationships/staging/src0002_batch0004_recording_source.tsv', rel_rec_src)

print(f"Processed {len(releases)} unique releases, {rec_count} tracks, {len(artists_data)} artists.")
