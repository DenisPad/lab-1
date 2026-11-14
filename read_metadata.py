"""
Скрипт для чтения метаданных аудио (MP3) и видео (MP4) файлов.
Вариант 4: длительность, битрейт.
"""

import os
import sys
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4


def read_audio_metadata(file_path):
    """Читает длительность и битрейт MP3-файла."""
    try:
        audio = MP3(file_path)
        return {
            "Тип файла": "Аудио (MP3)",
            "Длительность (сек)": round(audio.info.length, 2),
            "Битрейт (кбит/с)": round(audio.info.bitrate / 1000, 2)
        }
    except Exception as e:
        raise ValueError(f"Повреждённый MP3-файл или ошибка чтения: {e}")


def read_video_metadata(file_path):
    """Читает длительность и битрейт MP4-файла."""
    try:
        video = MP4(file_path)
        return {
            "Тип файла": "Видео (MP4)",
            "Длительность (сек)": round(video.info.length, 2),
            "Битрейт (кбит/с)": round(video.info.bitrate / 1000, 2)
        }
    except Exception as e:
        raise ValueError(f"Повреждённый MP4-файл или ошибка чтения: {e}")


def main():
    """Основная функция обработки аргументов и вывода метаданных."""
    if len(sys.argv) < 2:
        print("Использование: python read_metadata.py <путь_к_файлу>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден.")
        sys.exit(1)

    # Определение формата по расширению
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    try:
        if ext == '.mp3':
            metadata = read_audio_metadata(file_path)
        elif ext == '.mp4':
            metadata = read_video_metadata(file_path)
        else:
            print(f"Ошибка: Неподдерживаемый формат '{ext}'. Ожидаются .mp3 или .mp4.")
            sys.exit(1)

        print(f"\nМетаданные для файла '{file_path}':")
        for key, value in metadata.items():
            print(f"  - {key}: {value}")

    except ValueError as e:
        print(f"Ошибка обработки файла: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
