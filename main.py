from pathlib import Path

SCENE = (
    "My six-year-old saved her last pancake for Grandpa and cut it into \"equal\" halves — one much bigger.\n"
    "She gave him the big half: \"Old teeth need extra help.\""
)


def main() -> None:
    if not 1 <= len(SCENE) <= 280 or not SCENE.strip():
        raise ValueError("scene must be 1 to 280 characters and not only whitespace")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(SCENE, encoding="utf-8")


if __name__ == "__main__":
    main()
