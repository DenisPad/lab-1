"""
Скрипт для конвертации медиафайлов с помощью FFmpeg.
Вариант 4: MP3 -> WAV, MP4 -> MKV.
"""

import os
import shutil
import subprocess
import sys


def check_ffmpeg():
    """Проверяет наличие FFmpeg в системном PATH."""
    if shutil.which('ffmpeg') is None:
        print("Критическая ошибка: FFmpeg не найден в системе. Проверьте переменную PATH.")
        sys.exit(1)


def convert_file(input_path, output_path):
    """
    Конвертирует медиафайл с помощью FFmpeg.
    Поддерживаемые направления (Вариант 4): .mp3 -> .wav, .mp4 -> .mkv
    """
    if not os.path.exists(input_path):
        print(f"Ошибка: Исходный файл '{input_path}' не найден.")
        return False

    in_ext = os.path.splitext(input_path)[1].lower()
    out_ext = os.path.splitext(output_path)[1].lower()

    # Проверка допустимых пар конвертации для Варианта 4
    allowed_conversions = {
        '.mp3': '.wav',
        '.mp4': '.mkv'
    }

    if in_ext not in allowed_conversions or allowed_conversions[in_ext] != out_ext:
        print(f"Ошибка: Недопустимое направление конвертации ({in_ext} -> {out_ext}).")
        print("Для Варианта 4 поддерживаются только: .mp3 -> .wav и .mp4 -> .mkv")
        return False

    # Флаг -y позволяет перезаписывать выходной файл без подтверждения
    cmd = ['ffmpeg', '-i', input_path, '-y', output_path]
    
    print(f"Запуск конвертации: {input_path} -> {output_path}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Ошибка при выполнении FFmpeg:\n{result.stderr}")
        return False

    return True


def main():
    """Основная функция."""
    if len(sys.argv) < 3:
        print("Использование: python convert_media.py <входной_файл> <выходной_файл>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    check_ffmpeg()

    if convert_file(input_path, output_path):
        print(f"Успех! Файл сохранён как '{output_path}'.")
    else:
        print("Конвертация завершилась с ошибкой.")
        sys.exit(1)


if __name__ == '__main__':
    main()
