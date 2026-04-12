#!/usr/bin/env python3
"""
Validate a generated PPTX deck for common quality issues.
Checks slide count, font sizes, content density, and layout.

Usage:
    python validate-deck.py <deck.pptx> [--duration 30] [--verbose]

Dependencies:
    pip install python-pptx --break-system-packages
"""

import argparse
import json
import sys
import os

# Slide count guidelines by duration (minutes)
SLIDE_GUIDELINES = {
    5: (5, 7),
    10: (8, 12),
    15: (12, 18),
    20: (18, 25),
    30: (25, 35),
    45: (35, 50),
    60: (40, 60),
}

MIN_FONT_SIZE_PT = 14
MAX_BULLETS_PER_SLIDE = 6
MIN_BODY_FONT_PT = 18


def validate_deck(pptx_path, duration=None, verbose=False):
    """Validate a PPTX deck and return issues/warnings."""
    try:
        from pptx import Presentation
        from pptx.util import Pt, Emu
    except ImportError:
        print("Error: python-pptx is required. Install with:")
        print("  pip install python-pptx --break-system-packages")
        sys.exit(1)

    if not os.path.exists(pptx_path):
        print(f"Error: File not found: {pptx_path}")
        sys.exit(1)

    prs = Presentation(pptx_path)
    issues = []
    warnings = []
    stats = {
        "total_slides": len(prs.slides),
        "slides_with_small_fonts": 0,
        "slides_with_many_bullets": 0,
        "slides_with_no_title": 0,
        "total_images": 0,
        "total_text_elements": 0,
    }

    # Check slide count vs duration
    if duration and duration in SLIDE_GUIDELINES:
        min_slides, max_slides = SLIDE_GUIDELINES[duration]
        if stats["total_slides"] < min_slides:
            warnings.append(
                f"Slide count ({stats['total_slides']}) is below recommended "
                f"minimum ({min_slides}) for a {duration}-minute talk"
            )
        elif stats["total_slides"] > max_slides:
            warnings.append(
                f"Slide count ({stats['total_slides']}) exceeds recommended "
                f"maximum ({max_slides}) for a {duration}-minute talk"
            )

    # Check each slide
    for slide_num, slide in enumerate(prs.slides, 1):
        has_title = False
        bullet_count = 0
        small_fonts = []

        for shape in slide.shapes:
            if shape.has_text_frame:
                stats["total_text_elements"] += 1

                # Check for title
                if slide.shapes.title and shape.shape_id == slide.shapes.title.shape_id:
                    has_title = True

                for paragraph in shape.text_frame.paragraphs:
                    # Count bullets
                    if paragraph.text.strip():
                        if paragraph.level > 0 or len(shape.text_frame.paragraphs) > 1:
                            bullet_count += 1

                    # Check font sizes
                    for run in paragraph.runs:
                        if run.font.size:
                            size_pt = run.font.size.pt
                            if size_pt < MIN_FONT_SIZE_PT:
                                small_fonts.append(size_pt)

            # Count images
            if shape.shape_type == 13:
                stats["total_images"] += 1

        # Record issues
        if not has_title:
            stats["slides_with_no_title"] += 1
            if verbose:
                warnings.append(f"Slide {slide_num}: No title detected")

        if small_fonts:
            stats["slides_with_small_fonts"] += 1
            issues.append(
                f"Slide {slide_num}: Font size {min(small_fonts):.0f}pt is below "
                f"minimum {MIN_FONT_SIZE_PT}pt"
            )

        if bullet_count > MAX_BULLETS_PER_SLIDE:
            stats["slides_with_many_bullets"] += 1
            issues.append(
                f"Slide {slide_num}: {bullet_count} bullets exceeds maximum "
                f"of {MAX_BULLETS_PER_SLIDE}"
            )

    # Summary
    print(f"\n{'='*60}")
    print(f"DECK VALIDATION: {os.path.basename(pptx_path)}")
    print(f"{'='*60}")
    print(f"Total slides: {stats['total_slides']}")
    print(f"Total images: {stats['total_images']}")
    print(f"Text elements: {stats['total_text_elements']}")

    if duration:
        print(f"Target duration: {duration} minutes")

    if issues:
        print(f"\n❌ ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"  • {issue}")

    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  • {warning}")

    if not issues and not warnings:
        print(f"\n✅ All checks passed!")

    print(f"{'='*60}\n")

    return {"issues": issues, "warnings": warnings, "stats": stats}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a PPTX presentation deck")
    parser.add_argument("pptx_path", help="Path to the .pptx file")
    parser.add_argument("--duration", "-d", type=int, help="Expected talk duration in minutes")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all warnings")
    args = parser.parse_args()

    result = validate_deck(args.pptx_path, args.duration, args.verbose)
    sys.exit(1 if result["issues"] else 0)
