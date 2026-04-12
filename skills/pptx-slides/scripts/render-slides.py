#!/usr/bin/env python3
"""
Convert PPTX to per-slide PNG images for visual review.
Uses LibreOffice for PPTX→PDF conversion, then PyMuPDF for PDF→PNG.

Usage:
    python render-slides.py <deck.pptx> [--output-dir renders/] [--dpi 150]

Dependencies:
    pip install PyMuPDF --break-system-packages
    LibreOffice must be installed (libreoffice --headless)
"""

import argparse
import os
import subprocess
import sys
import tempfile


def render_slides(pptx_path, output_dir="renders/", dpi=150):
    """Convert PPTX → PDF → PNG per slide."""
    if not os.path.exists(pptx_path):
        print(f"Error: File not found: {pptx_path}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    # Step 1: PPTX → PDF via LibreOffice
    print(f"Converting {pptx_path} to PDF...")
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            subprocess.run([
                "libreoffice", "--headless", "--convert-to", "pdf",
                "--outdir", tmpdir, pptx_path
            ], check=True, capture_output=True, timeout=120)
        except FileNotFoundError:
            print("Error: LibreOffice not found. Install with:")
            print("  macOS: brew install --cask libreoffice")
            print("  Linux: sudo apt install libreoffice")
            sys.exit(1)
        except subprocess.TimeoutExpired:
            print("Error: LibreOffice conversion timed out (120s)")
            sys.exit(1)

        # Find the generated PDF
        pdf_name = os.path.splitext(os.path.basename(pptx_path))[0] + ".pdf"
        pdf_path = os.path.join(tmpdir, pdf_name)

        if not os.path.exists(pdf_path):
            print(f"Error: PDF not generated at {pdf_path}")
            sys.exit(1)

        # Step 2: PDF → PNG via PyMuPDF
        print(f"Rendering slides at {dpi} DPI...")
        try:
            import fitz  # PyMuPDF
        except ImportError:
            print("Error: PyMuPDF is required. Install with:")
            print("  pip install PyMuPDF --break-system-packages")
            sys.exit(1)

        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            zoom = dpi / 72
            matrix = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=matrix)

            output_path = os.path.join(output_dir, f"slide_{page_num + 1:03d}.png")
            pix.save(output_path)
            print(f"  Saved slide {page_num + 1}/{len(doc)}: {output_path}")

        doc.close()
        print(f"\nRendered {len(doc)} slides to {output_dir}")


def create_montage(output_dir, montage_path="montage.png", cols=4):
    """Create a contact sheet from rendered slides."""
    try:
        from PIL import Image
    except ImportError:
        print("Warning: Pillow not installed, skipping montage. Install with:")
        print("  pip install Pillow --break-system-packages")
        return

    images = sorted([
        os.path.join(output_dir, f)
        for f in os.listdir(output_dir)
        if f.endswith(".png") and f.startswith("slide_")
    ])

    if not images:
        print("No slide images found for montage")
        return

    # Load all images
    imgs = [Image.open(p) for p in images]
    thumb_w, thumb_h = 480, 270  # 16:9 thumbnails

    rows = (len(imgs) + cols - 1) // cols
    montage = Image.new("RGB", (thumb_w * cols, thumb_h * rows), "white")

    for i, img in enumerate(imgs):
        img.thumbnail((thumb_w, thumb_h))
        col = i % cols
        row = i // cols
        montage.paste(img, (col * thumb_w, row * thumb_h))

    montage.save(montage_path)
    print(f"Montage saved: {montage_path} ({cols}x{rows} grid)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render PPTX slides as PNG images")
    parser.add_argument("pptx_path", help="Path to the .pptx file")
    parser.add_argument("--output-dir", "-o", default="renders/", help="Output directory for PNGs")
    parser.add_argument("--dpi", "-d", type=int, default=150, help="Render DPI (default: 150)")
    parser.add_argument("--montage", "-m", action="store_true", help="Also create a contact sheet montage")
    args = parser.parse_args()

    render_slides(args.pptx_path, args.output_dir, args.dpi)

    if args.montage:
        create_montage(args.output_dir)
