import wave
import numpy as np


def write_audio_file(path, freq, sample_rate, volume, duration):
    sound_array = volume * np.sin(2 * np.pi* freq * np.arange(0, duration, 1 / sample_rate))
    with open(path, "wb") as f:
        pass

    return path


if __name__ == "__main__":
    import os
    import logging
    import argparse

    logging.basicConfig(level=logging.INFO)

    logger = loggin.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument("audio_output_dir", type=str)

    args = parser.parse_args()

    for filename, freq in [
        ("6kHz.wav", 6000, ),
        ("10kHz.wav", 10000, ),
    ]:
        path = os.path.join(
            os.path.abspath(args.audio_output_dir),
            filename,
        )
        audio_path = write_audio_file(path, freq)
        logger.info("Wrote audio to: %s" % audio_path)
    
    logger.info("Finished generating assets.")