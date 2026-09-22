import cv2
from pathlib import Path


def extract_frames(video_path, output_dir, interval_seconds=5):
    """
    Extract one frame from the video every `interval_seconds`.

    Parameters
    ----------
    video_path : Path
        Path to the input video.

    output_dir : Path
        Folder where extracted frames will be saved.

    interval_seconds : int
        Time interval between extracted frames.
    """

    video_path = Path(video_path)
    output_dir = Path(output_dir)

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Open video
    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise ValueError(f"Could not open video: {video_path}")

    # Get video information
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if fps <= 0:
        cap.release()
        raise ValueError(f"Could not determine FPS for: {video_path}")

    duration = total_frames / fps

    print(f"Video       : {video_path.name}")
    print(f"FPS         : {fps:.2f}")
    print(f"Total frames: {total_frames}")
    print(f"Duration    : {duration:.2f} seconds")

    # Number of frames between extracted frames
    frame_interval = max(1, int(fps * interval_seconds))

    frame_number = 0
    saved_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Extract frame at the required interval
        if frame_number % frame_interval == 0:

            timestamp = frame_number / fps

            filename = f"{video_path.stem}_{timestamp:.1f}s.jpg"

            output_path = output_dir / filename

            cv2.imwrite(str(output_path), frame)

            saved_count += 1

        frame_number += 1

    cap.release()

    print(f"Frames saved: {saved_count}")
    print(f"Output      : {output_dir}")
    print("-" * 50)

    return saved_count


def extract_all_videos(video_dir, frame_dir, interval_seconds=5):
    """
    Extract frames from all MP4 videos in a directory.

    Each video gets its own output folder.

    Example:

        s-1.mp4
            ↓
        extracted_frames/s-1/

        s-2.mp4
            ↓
        extracted_frames/s-2/
    """

    video_dir = Path(video_dir)
    frame_dir = Path(frame_dir)

    frame_dir.mkdir(parents=True, exist_ok=True)

    video_files = sorted(video_dir.glob("*.mp4"))

    if not video_files:
        print(f"No MP4 videos found in: {video_dir}")
        return

    print(f"Found {len(video_files)} video(s)")
    print("=" * 50)

    total_saved = 0

    for video_path in video_files:

        session_name = video_path.stem

        output_dir = frame_dir / session_name

        saved_count = extract_frames(
            video_path=video_path,
            output_dir=output_dir,
            interval_seconds=interval_seconds
        )

        total_saved += saved_count

    print("\nAll videos processed.")
    print(f"Total frames saved: {total_saved}")