import csv
import os

# Data for Fania Batch 0001
releases = [
    {
        "rel_id": "SRC0003-B0001-REL001",
        "title": "Siembra",
        "artist": "Willie Colón & Rubén Blades",
        "url": "https://fania.com/products/willie-colon-ruben-blades-siembra-1",
        "tracks": [
            ("A1", "Plástico", "Willie Colón & Rubén Blades"),
            ("A2", "Buscando Guayaba", "Willie Colón & Rubén Blades"),
            ("A3", "Pedro Navaja", "Willie Colón & Rubén Blades"),
            ("B1", "María Lionza", "Willie Colón & Rubén Blades"),
            ("B2", "Ojos", "Willie Colón & Rubén Blades"),
            ("B3", "Dime", "Willie Colón & Rubén Blades"),
            ("B4", "Siembra", "Willie Colón & Rubén Blades")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL002",
        "title": "Celia & Johnny",
        "artist": "Celia Cruz & Johnny Pacheco",
        "url": "https://fania.com/products/celia-johnny-celia-johnny-lp",
        "tracks": [
            ("A1", "Quimbara", "Celia Cruz & Johnny Pacheco"),
            ("A2", "Toro Mata", "Celia Cruz & Johnny Pacheco"),
            ("A3", "Vieja Luna", "Celia Cruz & Johnny Pacheco"),
            ("A4", "El Paso del Mulo", "Celia Cruz & Johnny Pacheco"),
            ("A5", "Tengo el Idde", "Celia Cruz & Johnny Pacheco"),
            ("B1", "Lo Tuyo es Mental", "Celia Cruz & Johnny Pacheco"),
            ("B2", "Canto a la Habana", "Celia Cruz & Johnny Pacheco"),
            ("B3", "Ño Mercedes", "Celia Cruz & Johnny Pacheco"),
            ("B4", "El Tumbao y Celia", "Celia Cruz & Johnny Pacheco"),
            ("B5", "El Pregón del Pescador", "Celia Cruz & Johnny Pacheco")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL003",
        "title": "Live At Yankee Stadium Vol. 1",
        "artist": "Fania All Stars",
        "url": "https://fania.com/products/fania-all-stars-live-at-yankee-stadium-vol-1-lp",
        "tracks": [
            ("A1", "Que Rico Suena Mi Tambor", "Fania All Stars (Vocals: Ismael Miranda)"),
            ("A2", "Soy Guajiro", "Fania All Stars (Vocals: Santos Colón)"),
            ("A3", "Diosa Del Ritmo", "Fania All Stars (Vocals: Celia Cruz)"),
            ("B1", "Pueblo Latino", "Fania All Stars (Vocals: Pete \"Conde\" Rodríguez)"),
            ("B2", "Mi Gente", "Fania All Stars (Vocals: Héctor Lavoe)")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL004",
        "title": "Live At Yankee Stadium Vol. 2",
        "artist": "Fania All Stars",
        "url": "https://fania.com/products/fania-all-stars-live-at-yankee-stadium-vol-2-lp",
        "tracks": [
            ("A1", "Hermandad Fania", "Fania All Stars (Vocals: Bobby Cruz)"),
            ("A2", "Bemba Colorá", "Fania All Stars (Vocals: Celia Cruz)"),
            ("B1", "Mi Debilidad", "Fania All Stars (Vocals: Ismael Quintana)"),
            ("B2", "Échate Pa'llá", "Fania All Stars (Vocals: Justo Betancourt)"),
            ("B3", "Congo Bongo", "Fania All Stars (Vocals: Cheo Feliciano & Héctor Lavoe)")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL005",
        "title": "Cosa Nuestra",
        "artist": "Willie Colón & Héctor Lavoe",
        "url": "https://fania.com/products/willie-colon-cosa-nuestra-lp",
        "tracks": [
            ("A1", "Che Che Colé", "Willie Colón & Héctor Lavoe"),
            ("A2", "No Me Llores Más", "Willie Colón & Héctor Lavoe"),
            ("A3", "Ausencia", "Willie Colón & Héctor Lavoe"),
            ("A4", "Te Conozco", "Willie Colón & Héctor Lavoe"),
            ("B1", "Juana Peña", "Willie Colón & Héctor Lavoe"),
            ("B2", "Sonero Mayor", "Willie Colón & Héctor Lavoe"),
            ("B3", "Sangrigorda", "Willie Colón & Héctor Lavoe"),
            ("B4", "Tú No Puedes Conmigo", "Willie Colón & Héctor Lavoe")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL006",
        "title": "Asalto Navideño",
        "artist": "Willie Colón & Héctor Lavoe",
        "url": "https://fania.com/products/willie-colon-asalto-navideno-lp",
        "tracks": [
            ("A1", "Introducción", "Willie Colón & Héctor Lavoe"),
            ("A2", "Canto a Borínquen", "Willie Colón & Héctor Lavoe"),
            ("A3", "Popurrí Navideño", "Willie Colón & Héctor Lavoe"),
            ("A4", "Traigo La Salsa", "Willie Colón & Héctor Lavoe"),
            ("B1", "Aires de Navidad", "Willie Colón & Héctor Lavoe"),
            ("B2", "La Murga", "Willie Colón & Héctor Lavoe"),
            ("B3", "Esta Navidad", "Willie Colón & Héctor Lavoe"),
            ("B4", "Vive Tu Vida Contento", "Willie Colón & Héctor Lavoe")
        ]
    },
    {
        "rel_id": "SRC0003-B0001-REL007",
        "title": "El Juicio",
        "artist": "Willie Colón & Héctor Lavoe",
        "url": "https://fania.com/products/willie-colon-el-juicio-lp",
        "tracks": [
            ("A1", "Ah-Ah / O-No", "Willie Colón & Héctor Lavoe"),
            ("A2", "Piraña", "Willie Colón & Héctor Lavoe"),
            ("A3", "Seguiré Sin Ti", "Willie Colón & Héctor Lavoe"),
            ("A4", "Timbalero", "Willie Colón & Héctor Lavoe"),
            ("B1", "Aguanile", "Willie Colón & Héctor Lavoe"),
            ("B2", "Soñando Despierto", "Willie Colón & Héctor Lavoe"),
            ("B3", "Si La Ves", "Willie Colón & Héctor Lavoe"),
            ("B4", "Pan y Agua (Bread & Water)", "Willie Colón & Héctor Lavoe")
        ]
    }
]

# Helper to split artists
def split_artists(text):
    # Basic split for &, Feat., (Vocals:)
    text = text.replace(" (Vocals: ", ", ").replace(" (vocals: ", ", ").replace(" Vocals: ", ", ").replace(" vocals: ", ", ").replace(")", "")
    text = text.replace(" & ", ", ").replace(" and ", ", ")
    artists = [a.strip() for a in text.split(",")]
    return artists

# Staging data
recordings = []
songs = []
artists = {} # name -> id
artist_list = []
rel_rec_song = []
rel_rec_art = []
rel_rec_rel = []
rel_rec_src = []

rec_count = 0
song_count = 0
art_count = 0

for rel in releases:
    for track_num, title, art_text in rel["tracks"]:
        rec_count += 1
        rec_id = f"SRC0003-B0001-REC{rec_count:03d}"
        
        song_count += 1
        song_id = f"SRC0003-B0001-SONG{song_count:03d}"
        
        side = track_num[0] if track_num[0] in "AB" else ""
        num = track_num[1:] if side else track_num
        
        # Recordings
        recordings.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0003",
            "source_name": "Fania Records",
            "source_url": rel["url"],
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "release_interpreter": rel["artist"],
            "release_genre": "Salsa / Latin Soul",
            "release_format": "LP",
            "release_year": "",
            "reference_number": "",
            "side": side,
            "track_number": num,
            "global_track_number": str(rec_count),
            "raw_track_title": title,
            "recording_title": title,
            "artist_text": art_text,
            "label_name": "Fania Records",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Songs
        songs.append({
            "batch_song_id": song_id,
            "source_id": "SRC0003",
            "source_name": "Fania Records",
            "source_url": rel["url"],
            "canonical_song_title_candidate": title,
            "raw_track_title": title,
            "release_candidate_id": rel["rel_id"],
            "release_title": rel["title"],
            "side": side,
            "track_number": num,
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Artists
        track_artists = split_artists(art_text)
        for a_name in track_artists:
            if a_name not in artists:
                art_count += 1
                art_id = f"SRC0003-B0001-ART{art_count:03d}"
                artists[a_name] = art_id
                artist_list.append({
                    "artist_candidate_id": art_id,
                    "source_id": "SRC0003",
                    "source_name": "Fania Records",
                    "source_url": rel["url"],
                    "raw_artist_text": a_name,
                    "candidate_artist_type": "group_candidate" if "All Stars" in a_name or "Sonora" in a_name or "Orquesta" in a_name else "performer_candidate_needs_review",
                    "release_candidate_id": rel["rel_id"],
                    "release_title": rel["title"],
                    "source_reference": rel["url"],
                    "evidence_text": f"Artist text appears on Fania official shop product page for release '{rel['title']}': {a_name}",
                    "confidence": "medium-high",
                    "review_status": "staged_for_review"
                })
            
            # Rec-Art Relationship
            rel_rec_art.append({
                "batch_recording_id": rec_id,
                "artist_candidate_id": artists[a_name],
                "raw_artist_text": a_name,
                "relationship_type": "credited_artist_candidate",
                "source_id": "SRC0003",
                "source_reference": f"{rel['url']}#track-{track_num}",
                "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
                "confidence": "high",
                "review_status": "staged_for_review"
            })
            
        # Rec-Song Relationship
        rel_rec_song.append({
            "batch_recording_id": rec_id,
            "batch_song_id": song_id,
            "relationship_type": "track_title_match",
            "source_id": "SRC0003",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Rec-Rel Relationship
        rel_rec_rel.append({
            "batch_recording_id": rec_id,
            "release_candidate_id": rel["rel_id"],
            "relationship_type": "track_of_release",
            "source_id": "SRC0003",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })
        
        # Rec-Src Relationship
        rel_rec_src.append({
            "batch_recording_id": rec_id,
            "source_id": "SRC0003",
            "source_url": rel["url"],
            "relationship_type": "primary_source",
            "source_reference": f"{rel['url']}#track-{track_num}",
            "evidence_text": f"Fania official shop product page: release='{rel['title']}', track='{track_num}', raw_track='{title}'",
            "confidence": "high",
            "review_status": "staged_for_review"
        })

# Write TSVs
def write_tsv(filename, data):
    if not data: return
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fieldnames = sorted(list(data[0].keys()))
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

write_tsv('authority/staging/src0003_batch0001_recordings.tsv', recordings)
write_tsv('authority/staging/src0003_batch0001_songs.tsv', songs)
write_tsv('authority/staging/src0003_batch0001_artist_candidates.tsv', artist_list)

write_tsv('relationships/staging/src0003_batch0001_recording_song.tsv', rel_rec_song)
write_tsv('relationships/staging/src0003_batch0001_recording_artist_candidate.tsv', rel_rec_art)
write_tsv('relationships/staging/src0003_batch0001_recording_release.tsv', rel_rec_rel)
write_tsv('relationships/staging/src0003_batch0001_recording_source.tsv', rel_rec_src)

print(f"Extraction complete: {len(releases)} releases, {rec_count} tracks, {len(artist_list)} artists.")
