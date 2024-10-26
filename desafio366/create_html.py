from typing import NamedTuple
import json

class VideoEntry(NamedTuple):
    youtube_id: str
    location: str
    is_special_event: bool = False
    event_name: str = ""

def generate_video_html(video: VideoEntry) -> str:
    """Generate HTML for a single video entry."""
    location_text = video.location
    if video.is_special_event and video.event_name:
        location_text += f" | ★ {video.event_name} ★"

    return f"""
        <article class="video-container">
            <h2 class="video-title"></h2>
            <iframe 
                class="video-frame"
                src="https://youtube.com/embed/{video.youtube_id}?autoplay=0&mute=1&loop=1&controls=1"
                title="Running Video"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
            <div class="video-meta">
                {location_text}
            </div>
        </article>
    """

def generate_full_html(videos: list[VideoEntry]) -> str:
    """Generate the complete HTML page with all video entries."""
    video_entries_html = "\n".join(generate_video_html(video) for video in videos)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 366 Corrida no Ar</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            background-color: #f1f1f1;
            font-family: monospace;
        }}

        header {{
            border: 4px solid #000;
            padding: 20px;
            margin-bottom: 40px;
            background: #fff;
        }}

        h1 {{
            margin: 0;
            font-size: 3em;
            text-transform: uppercase;
            letter-spacing: -2px;
        }}

        .description {{
            font-size: 1.2em;
            margin-top: 10px;
            font-style: italic;
        }}

        .video-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }}

        .video-container {{
            border: 4px solid #000;
            background: #fff;
            transition: transform 0.2s;
        }}

        .video-container:hover {{
            transform: translateY(-5px);
        }}

        .video-title {{
            padding: 15px;
            margin: 0;
            font-size: 1.2em;
            border-bottom: 4px solid #000;
        }}

        .video-frame {{
            aspect-ratio: 9/16;
            width: 100%;
            border: none;
            display: block;
        }}

        .video-meta {{
            padding: 15px;
            border-top: 4px solid #000;
            font-size: 0.9em;
        }}

        @media (max-width: 600px) {{
            body {{
                padding: 10px;
            }}
            
            h1 {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>Desafio 366 • Corrida no Ar</h1>
        <div class="description">Correndo todos os dias em 2024 e registrando (algumas) dessas corridas.</div>
        <div class="">Por <b>Tiago Maluta</b></div>
    </header>
    <div class="video-grid">
        {video_entries_html}
    </div>
</body>
</html>"""

def save_html(html: str, filename: str = "running_chronicles.html") -> None:
    """Save the generated HTML to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

def load_videos_from_json(filename: str) -> list[VideoEntry]:
    """Load video entries from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [VideoEntry(**entry) for entry in data]

# Example usage
if __name__ == "__main__":
    # Example video data
    videos = [
        VideoEntry("ruMGwjfzRdU", "São Paulo 🇧🇷"),
        VideoEntry("judDj0kpXvI", "São Paulo 🇧🇷"),
        VideoEntry("cuTsN5Can5c", "São Paulo 🇧🇷"),
        VideoEntry("sq3e_ooY4LA", "São Paulo 🇧🇷"),
        VideoEntry("ZKIac6Xc6do", "São Paulo 🇧🇷"),
        VideoEntry("2aA_2ZoCDiw", "São Paulo 🇧🇷"),
        VideoEntry("oNOyyLeoGOc", "São Paulo 🇧🇷"),
        VideoEntry("g2hw71-FyEE", "São Paulo 🇧🇷"),
        VideoEntry("XeE4pmYIR8c", "São Paulo 🇧🇷"),
        VideoEntry("OmCAMesq4PE", "São Paulo 🇧🇷"),
        VideoEntry("b3pyC-E3et0", "São Paulo 🇧🇷"),
        VideoEntry("J187EbVRkwA", "São José dos Campos 🇧🇷"),
        VideoEntry("gIWlIJAHgMs", "São José dos Campos 🇧🇷"),
        VideoEntry("yjvRsOG70vE", "São Paulo 🇧🇷"),
        VideoEntry("z8PyKYmkOhw", "São Paulo 🇧🇷"),
        VideoEntry("lG8gW5OtiBw", "São Paulo 🇧🇷"),
        VideoEntry("MvxupwXJuFI", "São Paulo 🇧🇷 | Troféu Cidade de São Paulo"),
        VideoEntry("vT9pAx7VtYE", "São Paulo 🇧🇷"),
        VideoEntry("m3t02lVXFZo", "São Paulo 🇧🇷"),
        VideoEntry("jN2wWAdRWaI", "São Paulo 🇧🇷"),
        VideoEntry("b-rjerzs_g8", "São Paulo 🇧🇷"),
        VideoEntry("AV_x0OAIkBY", "São Paulo 🇧🇷"),
        VideoEntry("B-uFYsp75-4", "São Paulo 🇧🇷"),
        VideoEntry("8QvPaZkTYTo", "São Paulo 🇧🇷"),
        VideoEntry("PPGHgpcP2_Y", "São Paulo 🇧🇷"),
        VideoEntry("B_02cbI6VHU", "São Paulo 🇧🇷"),
        VideoEntry("zuxaoMyGfN4", "São Paulo 🇧🇷"),
        VideoEntry("3bd00KM0vWw", "São Paulo 🇧🇷"),
        VideoEntry("cZi2-UiFxeM", "São Paulo 🇧🇷"),
        VideoEntry("PBnTmRezTe4", "São Paulo 🇧🇷"),
        VideoEntry("OB0neFzNjLI", "São Paulo 🇧🇷"),
        VideoEntry("sl0iHr3cKc8", "São Paulo 🇧🇷"),
        VideoEntry("jSx_YM0zFOk", "São Paulo 🇧🇷"),
        VideoEntry("tjB26Ab79So", "São Paulo 🇧🇷"),
        VideoEntry("IGKp9CTu95E", "São Paulo 🇧🇷"),
        VideoEntry("P02H6HvuRUs", "São Paulo 🇧🇷"),
        VideoEntry("sbbBWx8zzK8", "São Paulo 🇧🇷"),
        VideoEntry("cOCddx58E0o", "São Paulo 🇧🇷"),
        VideoEntry("h4uFMs8Thsk", "São Paulo 🇧🇷"),
        VideoEntry("Mmk6qJsTdA4", "São Paulo 🇧🇷"),
        VideoEntry("HWt9jbrchaY", "São Paulo 🇧🇷"),
        VideoEntry("wCRQhJG90w8", "São Paulo 🇧🇷"),
        VideoEntry("_nqqUT-Ejyg", "São Paulo 🇧🇷"),
        VideoEntry("Jr_hTkyIhJQ", "São Paulo 🇧🇷"),
        VideoEntry("9E-KE8Yvk_0", "São Paulo 🇧🇷"),
        VideoEntry("jCyi1BOkAjA", "São Paulo 🇧🇷"),
        VideoEntry("GGy__plPpTo", "São Paulo 🇧🇷"),
        VideoEntry("LN_l2lrezJg", "São Paulo 🇧🇷"),
        VideoEntry("Wvn3iUwjlrM", "São Paulo 🇧🇷"),
        VideoEntry("LXTdmykXcj8", "São Paulo 🇧🇷"),
        VideoEntry("gAtmMmMrcJo", "São Paulo 🇧🇷"),
        VideoEntry("Lb3frU5cCg4", "São Paulo 🇧🇷"),
        VideoEntry("SJodqtS7giY", "São Paulo 🇧🇷"),
        VideoEntry("xZNuWuSXGh8", "São Paulo 🇧🇷"),
        VideoEntry("h3fBzeALtG8", "São Paulo 🇧🇷"),
        VideoEntry("MCNRhEDQrjM", "São Paulo 🇧🇷"),
        VideoEntry("4pOKxrFxXQI", "São Paulo 🇧🇷"),
        VideoEntry("tiI-b7J2TF4", "São Paulo 🇧🇷"),
        VideoEntry("oMRBGZOauUk", "Tatuí - SP 🇧🇷"),
        VideoEntry("UG5OWP0mYZg", "São Paulo 🇧🇷"),
        VideoEntry("oUTwOeSz9Ng", "São Paulo 🇧🇷"),
        VideoEntry("bScEWqBkVuk", "São Paulo 🇧🇷"),
        VideoEntry("S-DD91cYSL0", "São Paulo 🇧🇷"),
        VideoEntry("OQEWh02PnF8", "São Paulo 🇧🇷"),
        VideoEntry("cXoXbxF-XMg", "São Paulo 🇧🇷"),
        VideoEntry("BgpWyaf-gPM", "São Paulo 🇧🇷"),
        VideoEntry("I-LLMnKA5F8", "São Paulo 🇧🇷"),
        VideoEntry("CRGf3vuBFdc", "São Paulo 🇧🇷"),
        VideoEntry("5N_dQn_sa08", "São Paulo 🇧🇷"),
        VideoEntry("iR0g6w-YSYk", "São Paulo 🇧🇷"),
        VideoEntry("B0q4oCHvt-A", "São José dos Campos 🇧🇷"),
        VideoEntry("vaJ46ZQ3CMo", "São Sebastião - Maresias - SP 🇧🇷"),
        VideoEntry("A-TFses-KJU", "São Sebastião - Maresias - SP 🇧🇷"),
        VideoEntry("uZj9E9KHKc4", "São Paulo 🇧🇷"),
        VideoEntry("9WzwOgoYy5U", "New York 🇺🇸"),
        VideoEntry("OUretnXA_VY", "New York 🇺🇸"),
        VideoEntry("DucvDbxs9rc", "São Paulo - SP 🇧🇷"),
        VideoEntry("KqXDcH3i594", "Itupeva - SP 🇧🇷"),
        VideoEntry("DmzWHtFiJoA", "São Paulo 🇧🇷"),
        VideoEntry("X9Gh8wJHykA", "São Paulo 🇧🇷 | Corrida Graac"),
        VideoEntry("o_9YqUg1Jl0", "Palo Alto 🇺🇸"),
        VideoEntry("UbrAifRMBWQ", "Brasília - DF 🇧🇷"),
        VideoEntry("iXKRUjvXnaE", "Recife - PE 🇧🇷"),
        VideoEntry("CiLYQPuNpMI", "São Paulo - SP 🇧🇷"),
        VideoEntry("iSJ1gC8mHFo", "Valladolid 🇪🇸"),
        VideoEntry("EUg2EnBb23A", "Valladolid 🇪🇸"),
        VideoEntry("l-kLecD8baw", "Salamanca 🇪🇸"),
        VideoEntry("R1R7wqnDEUo", "Bilbao 🇪🇸", True, "Bilbao Night Marathon 2024"),
        VideoEntry("1d_F_2H49yk", "Bilbao 🇪🇸"),
        VideoEntry("NcyAzlhIxLI", "Madrid 🇪🇸")
        # Add more videos here...
    ]
    
    # Generate and save HTML
    html_content = generate_full_html(videos)
    save_html(html_content)